import sys
import os
import io

def leia_cabecalho(arquivo):
    '''
    Lê o cabeçalho do arquivo, que contém o ponteiro para o início da LED.
    '''
    arquivo.seek(0)
    return int.from_bytes(arquivo.read(4), byteorder='big', signed=True)

def escreve_cabecalho(arquivo, pos):
    '''
    Escreve o ponteiro da LED no início do arquivo (cabeçalho).
    '''
    arquivo.seek(0)
    arquivo.write(pos.to_bytes(4, byteorder='big', signed=True))

def leia_registro(arquivo):
    '''
    Lê um registro do arquivo, retornando sua posição e os dados decodificados.
    Retorna (None, None) se não houver mais registros.
    '''
    pos = arquivo.tell()
    tamanho_bytes = arquivo.read(2)
    if not tamanho_bytes or len(tamanho_bytes) < 2:
        return None, None
    
    tamanho = int.from_bytes(tamanho_bytes, byteorder='big')
    dados = arquivo.read(tamanho)
    if not dados or len(dados) < tamanho:
        return None, None
    return pos, dados.decode(errors='ignore')

def buscar(filmes: io.BufferedReader, id_procurado: str) -> tuple:
    """
    Essa funcao deve receber um arquivo com registros de filmes e um id, fazer uma busca sequencial
    no arquivo e localizar o registro referente ao id retornando uma mensagem padrao, este registro, e seu offset.
    Caso o registro nao tenha sido encontrado, retorna uma mensagem padrao e erro.
    """
    filmes.seek(0, io.SEEK_END)
    fim_do_arquivo = filmes.tell()

    filmes.seek(4) # Pula o cabeçalho
    offset_atual = filmes.tell()
    
    while offset_atual < fim_do_arquivo:
        offset_do_registro = offset_atual
        
        tamanho_bytes = filmes.read(2)
        if not tamanho_bytes:
            break
        tamanho = int.from_bytes(tamanho_bytes, byteorder='big')
        
        if tamanho == 0: 
             offset_atual += 2
             continue

        registro = filmes.read(tamanho)

        if not registro or len(registro) < tamanho:
            break # Fim do arquivo ou registro corrompido

        if registro.startswith(b'*'):
            # Pula para o próximo registro
            offset_atual += 2 + tamanho
            filmes.seek(offset_atual)
            continue
        
        try:
            registro_decodificado = registro.decode('utf-8')
            campos = registro_decodificado.split('|')
            
            if campos[0] == id_procurado:
                achado = True
                registro_formatado = '|'.join(campos[:8]) 
                mensagem_padrao = f'Busca pelo registro de chave "{id_procurado}"'
                esperado = f"{registro_formatado} ({tamanho} bytes)"
                local = f"Local: offset = {offset_do_registro} bytes ({hex(offset_do_registro)})"
                return mensagem_padrao, esperado, local

        except UnicodeDecodeError:
            pass

        offset_atual += 2 + tamanho
        filmes.seek(offset_atual)

    mensagem_padrao = f'Busca pelo registro de chave "{id_procurado}"'
    erro = "Erro: registro nao encontrado!"
    return mensagem_padrao, erro

def remover(f, chave):
    '''
    Remove logicamente o registro com a chave especificada.
    Encadeia o espaço liberado na LED.
    '''
    f.seek(0)
    led = leia_cabecalho(f)
    f.seek(4)
    while True:
        pos, registro = leia_registro(f)
        if registro is None:
            break
        if registro.startswith('*'):
            continue
        campos = registro.split('|')
        if not campos or not campos[0].isdigit():
            continue
        if int(campos[0]) == chave:
            f.seek(pos)
            tamanho_bytes = f.read(2)
            tamanho_registro = int.from_bytes(tamanho_bytes, byteorder='big')
            
            if tamanho_registro < 5:
                print("Erro: Registro muito pequeno para ser removido logicamente.")
                return

            f.seek(pos + 2)
            f.write(b'*')

            f.write(led.to_bytes(4, byteorder='big', signed=True))
            escreve_cabecalho(f, pos)
            print(f'Registro com ID {chave} removido.')
            return
    print(f'Filme com ID {chave} não encontrado para remoção.')

def inserir(f, dados):
    """Insere um novo filme no arquivo, reaproveitando espaço da LED se disponível."""
    dados = dados.strip()
    
    registro_bytes = dados.encode("utf-8")
    tamanho_novo = len(registro_bytes)

    f.seek(0)
    ponteiro_led = int.from_bytes(f.read(4), byteorder="big", signed=True)

    pos_insercao = -1
    encontrou_espaco = False

    if ponteiro_led != -1:
        f.seek(ponteiro_led)
        tamanho_disponivel = int.from_bytes(f.read(2), byteorder="big")
        
        if tamanho_novo <= tamanho_disponivel:
            f.seek(ponteiro_led + 2 + 1)
            proximo_led = int.from_bytes(f.read(4), byteorder="big", signed=True)
            pos_insercao = ponteiro_led
            encontrou_espaco = True
            escreve_cabecalho(f, proximo_led)
            print(f"Espaço reutilizado na posição {pos_insercao} com tamanho {tamanho_disponivel}.")

    if encontrou_espaco:
        f.seek(pos_insercao)
        f.write(tamanho_disponivel.to_bytes(2, byteorder="big")) 
        f.write(registro_bytes)
        espaco_restante = tamanho_disponivel - tamanho_novo
        if espaco_restante > 0:
            f.write(b'\0' * espaco_restante)
        print(f"Inserido em espaço reutilizado na posição {pos_insercao}.")
    else:
        f.seek(0, 2)
        pos_insercao = f.tell()
        f.write(tamanho_novo.to_bytes(2, byteorder="big"))
        f.write(registro_bytes)
        print(f"Inserido no final do arquivo na posição {pos_insercao}.")

def imprimir_led(f):
    '''
    Imprime os ponteiros dos espaços disponíveis na LED.
    '''
    pos = leia_cabecalho(f)
    print('LED:', end=' ')
    while pos != -1:
        print(pos, end=' ')
        f.seek(pos + 2 + 1) 
        prox_bytes = f.read(4)
        if not prox_bytes or len(prox_bytes) < 4:
            break
        pos = int.from_bytes(prox_bytes, byteorder='big', signed=True)
    print()

def compactar(nome_arquivo):
    '''
    Compacta o arquivo, removendo fisicamente registros marcados como removidos.
    '''
    registros_validos = []
    with open(nome_arquivo, 'rb') as f:
        f.seek(4) # Pula o cabeçalho inicial
        while f.tell() < os.fstat(f.fileno()).st_size: 

            resultado = leia_registro(f)
            
            if resultado[0] is None:
                break
            
            pos, dados_str = resultado
            
            if not dados_str.startswith('*'):
                registros_validos.append(dados_str)

    # Reescreve o arquivo apenas com os registros válidos
    with open(nome_arquivo, 'wb') as f:
        # Escreve um novo cabeçalho limpo, com a LED vazia
        f.write((-1).to_bytes(4, byteorder='big', signed=True))
        
        for reg_str in registros_validos:
            dados_bytes = reg_str.encode('utf-8')
            tamanho = len(dados_bytes)
            f.write(tamanho.to_bytes(2, byteorder='big'))
            f.write(dados_bytes)
            
    print('Arquivo compactado com sucesso.')

def processar_operacoes(arquivo_dados, arquivo_operacoes):
    '''
    Executa as operações descritas no arquivo de operações sobre o arquivo de dados.
    '''
    try:
        with open(arquivo_dados, 'r+b') as f:
            with open(arquivo_operacoes, 'r', encoding='utf-8') as op:
                for linha_op in op:
                    linha_op = linha_op.strip()
                    if not linha_op:
                        continue
                    print(f"\n-> Executando: {linha_op}")
                    operacao, *args = linha_op.split(' ', 1)
                    
                    if operacao == 'b':
                        if not args: continue
                        id_str = args[0]
                        resultado_busca = buscar(f, id_str)
                        for linha_res in resultado_busca:
                            print(linha_res)
                            
                    elif operacao == 'r':
                        if not args: continue
                        remover(f, int(args[0]))
                        
                    elif operacao == 'i':
                        if not args: continue
                        inserir(f, args[0])
    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo_dados}' ou '{arquivo_operacoes}' não encontrado.")

def main():
    '''
    Interpreta os argumentos da linha de comando e chama as funções apropriadas.
    '''
    if len(sys.argv) < 3:
        print('Uso: python programa.py [-e|-p|-c] <arquivo_de_dados> [arquivo_de_operacoes]')
        return
    
    flag = sys.argv[1]
    nome_arquivo_dados = sys.argv[2]
    
    if not os.path.exists(nome_arquivo_dados):
        print(f'Arquivo de dados {nome_arquivo_dados} não encontrado.')
        return
        
    if flag == '-e':
        if len(sys.argv) != 4:
            print('Uso para -e: python programa.py -e <arquivo_de_dados> <arquivo_de_operacoes>')
            return
        nome_arquivo_operacoes = sys.argv[3]
        if not os.path.exists(nome_arquivo_operacoes):
            print(f'Arquivo de operações {nome_arquivo_operacoes} não encontrado.')
            return
        processar_operacoes(nome_arquivo_dados, nome_arquivo_operacoes)
        
    elif flag == '-p':
        with open(nome_arquivo_dados, 'rb') as f:
            imprimir_led(f)
            
    elif flag == '-c':
        compactar(nome_arquivo_dados)
        
    else:
        print('Flag inválida. Use -e, -p ou -c.')

if __name__ == '__main__':
    main()