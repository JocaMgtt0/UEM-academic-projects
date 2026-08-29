import sys
sys.setrecursionlimit(10**4)



def le_arquivo(nome: str) -> list[list[str]]:
    '''
    Lê o conteúdo do arquivo *nome* e devolve uma lista onde cada elemento é
    uma lista com os valores das colunas de uma linha (valores separados por
    vírgula). A primeira linha do arquivo, que deve conter o nome das
    colunas, é descartado.

    Por exemplo, se o conteúdo do arquivo for

    tipo,cor,ano
    carro,verde,2010
    moto,branca,1995

    a resposta produzida é
    [['carro', 'verde', '2010'], ['moto', 'branca', '1995']]
    '''
    try:
        with open(nome) as f:
            tabela = []
            linhas = f.readlines()
            for i in range(1, len(linhas)):
                tabela.append(linhas[i].split(','))
            return tabela
    except IOError as e:
        print(f'Erro na leitura do arquivo "{nome}": {e.errno} - {e.strerror}.')
        return []
    
tabela = le_arquivo('medals.csv')



#função para organizar o pais extraido da tabela, com o numero de medalhas, e o genero, armazenando no sistema

def matriz2(tabela: list, resultado: list):
    '''
    vai percorrer a matriz *tabela* e para cada linha vai extrair o elemento 10, que é o tipo de pais, e o emento 0 que é o tipo de medalha, apos isso vai fazer uma
    estrutura de repetição para ler a lista *resultado*, caso o pais ja esteja na lista resultado, ele vai atualizar o numero de medalha, se é prata, ouro ou bronze, se ele
    nao esta na lista resultado a função ira aidicionar o pais a lista e autualiazar os dados de medalha armazenado, fazendo o sistema guardar somente o nome do pais, e o tipo de medalha que
    o pais possui, separando por pais, e por genero, para nao ficar desorganizado. Passei *resultado* como parametro para fazer uma função com para fazer uma função com passsagem por referência.
    Ou seja, a função vai receber a lista tabela, extrair o pais, genero, o tipo de medalha e adicionar na lista resultado, nesse caso, a lista resultado vai ficar separado com pais o genero
    e o tipo de medalha, e caso o pais ja estiver na lista, e for genero *M* ele soma a medalha apenas na sublista em questão, caso nao estiver, ele adiciona o pais e o genero novamente.

    >>> resultado=[]
    >>> matriz2([['Gold Medal', '1', '2024-07-27', 'Remco EVENEPOEL', 'M', 'Cycling Road', "Men's Individual Time Trial", 'ATH', '/en/paris-2024/results/cycling-road/men-s-individual-time-trial/fnl-000100--', '1903136', 'BEL', 'Belgium', 'Belgium'], ['Gold Medal', '1', '2024-07-27', 'Remco EVENEPOEL', 'W', 'Cycling Road', "Men's Individual Time Trial", 'ATH', '/en/paris-2024/results/cycling-road/men-s-individual-time-trial/fnl-000100--', '1903136', 'BEL', 'Belgium', 'Belgium']], resultado)
    >>> resultado
    [['BEL', 'M', 1, 0, 0], ['BEL', 'W', 1, 0, 0]]
    >>> matriz2([['Silver Medal', '2', '2024-07-27', 'United States', 'W', 'Diving', "Women's Synchronised 3m Springboard", 'TEAM', '/en/paris-2024/results/diving/women-s-synchronised-3m-springboard/fnl-000100--', 'DIVW3MTEAM2-USA01', 'USA', 'United States', 'United States of America']], resultado)
    >>> resultado
    [['BEL', 'M', 1, 0, 0], ['BEL', 'W', 1, 0, 0], ['USA', 'W', 0, 1, 0]]

    '''

    for i in range(len(tabela)):
        pais = tabela[i][10]
        medalha = tabela[i][0]
        genero = tabela[i][4]

        encontrado = False
        for j in range(len(resultado)):
            if resultado[j][0] == pais and resultado[j][1] == genero:
                if medalha == 'Gold Medal':
                    resultado[j][2] += 1
                elif medalha == 'Silver Medal':
                    resultado[j][3] +=1
                elif medalha == 'Bronze Medal':
                    resultado[j][4] +=1
                encontrado = True

        if encontrado == False:
            if medalha == 'Gold Medal':
                resultado.append([pais, genero, 1, 0, 0])
            elif medalha == 'Silver Medal':
                resultado.append([pais, genero, 0, 1, 0])
            elif medalha == 'Bronze Medal':
                resultado.append([pais, genero, 0, 0, 1])


 #somar todas as medalhas de um pais               
def soma(resultado: list)->list:
    '''
    essa função vai receber a lista resultado e vai extrair apenas os paises e o numero de medalhas de ouro, prata ou bronze para fazer a soma total dessas medalhas.
    definimos uma lista chamada paises para armazenar esses dados, e ira fazer a leitura da list aresultado e atribuir os indicies, começamos falando que o pais nao esta na lista
    paises, para que ele execute a estrutura de repetição, a mesma percorre essa lista paises verificando se o pais que esta na lista de resultado é o mesmo que esta na lista de paises,
    se for ele soma as medalahas e encerra, se nao for o mesmo ele adiciona o pais na lista de paises. Ela tambem é responsavel por fazer a soma de todas as medalhar e mostrar o total
    de medalhas de cada pais logo apos a contagem de ouro, prata e bronze.
    >>> soma([['BEL', 'M', 1, 0, 0], ['BEL', 'W', 1, 0, 0], ['USA', 'W', 0, 1, 0]])
    [['BEL', 2, 0, 0, 2], ['USA', 0, 1, 0, 1]]
    
    '''
    paises = []
    for i in range(len(resultado)):
        pais = resultado[i][0]
        ouro = resultado[i][2]
        prata = resultado[i][3]
        bronze = resultado[i][4]

        atribuido = False
        for j in range(len(paises)):
            if paises[j][0] == pais:
                paises[j][1] += ouro
                paises[j][2] += prata
                paises[j][3] += bronze
                atribuido = True
        if atribuido == False:
            paises.append([pais, ouro, prata, bronze])

    for i in range(len(paises)):
        total = paises[i][1] + paises[i][2] + paises[i][3]
        paises[i].append(total)

    return paises 


def ordem(paises:list) -> list:
    '''
    essa função vai receber a lista paises e vai percorrer a mesma fazendo a comparação das medalhas, quem ficou com mais medalhas de ouro
    vem primeiro, se houver empate entre as medalhas de ouro o desempate ocorre nas medalhas de prata, se houver empate novamente nas 
    medalahas de prata, o desempate ocorre nas medalhas de bronze, eu defini uma variavel auxiliar para fazer a interação e a troca
    dos paises, para obedecer a condição dita a cima. Ou seja, se o numero de medalhas de ouro do elemento j for menor que o numero
    de medalhas de ouro da chav, ele move j para a direita, assim faz a mesma coisa com os outros elementos.
    
    '''

    for i in range(1,len(paises)):
        aux = paises[i]
        j = i-1
        while j >=0 and (paises[j][1] < aux[1] or (paises[j][1] == aux[1] and paises[j][2] < aux[2]) or (paises[j][1] == aux[1] and paises[j][2] == aux[2] and paises[j][3] < aux[3])):
            paises[j+1] = paises[j]
            j-=1
        paises[j+1] = aux
    return paises


def final(paises:list)->list:
    '''
    essa função vai apresentar a tabela final dos valores que vamos adicionar na tabela final.
    '''
    ordenação = ordem(paises)
    print(f"{'país':<5} {'ouro':<5} {'prata':<6} {'bronze':<6} {'Total':<6}")
    print('-=' * 30)
    for pais in ordenação:
        print(f"{pais[0]:<5} {pais[1]:<5} {pais[2]:<5} {pais[3]:<6} {pais[4]:<6}")



def Genero(resultado:list, indicie:int=0, lista_nova: list = []):
    '''
    essa função vai percorrer a lista resultado e verificar quais sao os paises contemplados com um unico genero e adicionar eles na lista_nova. 
    '''


    if indicie == len(resultado):
        return lista_nova
    
    pais = resultado[indicie][0]
    genero = resultado[indicie][1]

    if genero not in ['M', 'W']:
        return Genero(resultado, indicie + 1, lista_nova)

    def verificar(lista, pais, ind=0):
        if ind== len(lista):
            return -1
        if lista[ind][0] == pais:
            return ind
        return verificar(lista, pais, ind+1)
    encontrado = verificar(lista_nova, pais)

    if encontrado != -1:
        if lista_nova[encontrado][1] != genero:
            lista_nova.pop(encontrado)
    else:
        lista_nova.append([pais,genero])

    return Genero(resultado, indicie + 1, lista_nova)


def ordem2(lista_nova:list):
    gnr = Genero(lista_nova)
    print(f"{'país':<5} {'gênero':<5}")
    print('-='*30)
    for gen in gnr:
        print(f"{gen[0]:<5} {gen[1]:<5}")



def main():
    arquivo = 'medals.csv'
    tabela = le_arquivo(arquivo)
    resultado = []
    matriz2(tabela, resultado)
    paises = soma(resultado)
    final(paises)
    lista_nova = []
    Genero(resultado, 0, lista_nova)
    print('-='*30)
    ordem2(lista_nova)

if __name__ == '__main__':
    main()
            
    



    
    
        

    
