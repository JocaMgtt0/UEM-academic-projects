from enum import Enum, auto
from dataclasses import dataclass

class usuarios (Enum):
    universitarios = 1
    colab_3mil = 2
    colab_acima_3mil = 3
    docentes = 4
    externo = 5

class Pagamento(Enum):
    pix = auto()
    cartao = auto() 
    dinheiro = auto()

class Escolha(Enum):
    um = auto()
    dois = auto()
    tres = auto()

def pessoas(usuario1 : usuarios) -> float:
    '''Essa função vai identificar o tipo de usuário do cliente, retornando o valor do ticket com base nisso. O usuário
    que pode ser *universitários, colaboradores ate 3 mil,
    colaboradores acima de 3 mil, docentes, pessoas externas*,
    sabendo que o RU da UEM cobra um valor dependendo da relação
    do usuário com a universidade.
    >>> pessoas(usuarios.universitarios)
    5
    >>> pessoas(usuarios.colab_3mil)
    5
    >>> pessoas(usuarios.colab_acima_3mil)
    10
    >>> pessoas(usuarios.docentes)
    10
    >>> pessoas(usuarios.externo)
    19
    ''' 

    if usuario1 == usuarios.universitarios:
        preco = 5
    elif usuario1 == usuarios.colab_3mil:
        preco = 5
    elif usuario1 == usuarios.colab_acima_3mil:
        preco = 10
    elif usuario1 == usuarios.docentes:
        preco = 10
    else:
        preco = 19
    return preco

def forma_pagamento(recibo : Pagamento) -> Pagamento:
    ''' Essa função vai receber três formas de pagamento e devolver a que for escolhida pelo cliente
    sendo *dinheiro, cartao e pix*
    Exemplo:
    >>> forma_pagamento('dinheiro')
    'dinheiro'
    >>> forma_pagamento('cartao')
    'cartao'
    >>> forma_pagamento('pix')
    'pix'
    '''
    if recibo == 'dinheiro':
        return 'dinheiro'
    elif recibo == 'cartao':
        return 'cartao'
    else:
        return 'pix'


@dataclass
class final:
    usuario2: usuarios 
    tickets: int
    pagamento: Pagamento
    valor: int

def ticket(usuario2: usuarios, tickets: int) -> final:
    '''
    essa função de classe composta retornara o valor total da venda com base no tipo de usuario
    e a quantidade de tickets por ele soliçitado.
    Levando em conta o valor variado de usuario para o outro, como ja apresentado na funçao (pessoas) acima.
    Exemplo:
    >>> ticket(usuarios.universitarios, 1)
    5
    >>> ticket(usuarios.colab_acima_3mil, 5)
    50
    >>> ticket(usuarios.externo,1)
    19
    '''

    if usuario2 == usuarios.universitarios:
        total = tickets * 5
    elif usuario2 == usuarios.colab_3mil:
        total = tickets * 5
    elif usuario2 == usuarios.colab_acima_3mil:
        total = tickets * 10
    elif usuario2 == usuarios.docentes:
        total = tickets * 10
    else:
        total = tickets * 19
    return total

from dataclasses import dataclass

@dataclass
class Relatório:
    tickets_final: int
    receita_final: int

def relatorio(lista_tickets: list, lista_receita:list) -> Relatório:
    '''Essa função vai receber duas listas e retornar um relatorio
    com o total de tickets vendidos e a receita do dia
    exemplo:
    >>> relatorio([10,2,1], [50,10,19])
    Relatório(tickets_final=13, receita_final=79)
    >>> relatorio([10,10,10], [50,50,50])
    Relatório(tickets_final=30, receita_final=150)
    '''
    tickets_final = 0
    receita_final = 0
    for tickets in lista_tickets:
        tickets_final = tickets_final + tickets
    for receita in lista_receita:
        receita_final = receita_final + receita
    relatorio = Relatório(tickets_final, receita_final)
    return relatorio
    
class Escolha(Enum):
    um = auto()
    dois = auto()
    tres = auto()

def grafico(lista):

    total = len(lista)
    porcentagens = {}
    for item in lista:
        conta = lista.count(item)
        porcentagem = (conta / total)*100
        porcentagens[item] = porcentagem 
    
    for item, porcentagem in porcentagens.items():
        traço = '[' + ("▃" * int(porcentagem)) + ']'
        print(f"{item.name}: {porcentagem: .2f}% {traço}")
        


def main():
    lista_receita = list()
    lista_tickets = list()
    lista_usuario = []
    lista_pagamento = []
    escolha = 0
    while escolha != 3:
        print('[1] Registro de venda')
        print('[2] Relatório de venda')
        print('[3] Encerrar')
        print()
        escolha: Escolha = int(input('Digite a opção escolhida: \n '))
        print('_'*43)
        if escolha == 1:
            print('[1] Universitarios')
            print('[2] Colab_3mil')
            print('[3] Colab_acima_3mil')
            print('[4] Docentes')
            print('[5] Externo')
            usuario1: pessoas = int(input('Qual o tipo de usuário? \n '))
            print('_'*25)
            usuario1: pessoas 
            usuario1 =  usuarios(usuario1)
            lista_usuario.append(usuario1)
            tickets: int = int(input('Quantos tickets deseja comprar: \n'))
            print('_'*25)
            lista_tickets.append(tickets)
            print('[1] Pix ')
            print('[2] Cartão')
            print('[3] Dinheiro')
            recibo: forma_pagamento = int(input('Qual a forma de pagamento? \n'))
            recibo = Pagamento(recibo)
            lista_pagamento.append(recibo)
            print('_'*25)
            registra = ticket(usuario1, tickets)
            lista_receita.append(registra)
        elif escolha == 2:
            Relatorio = relatorio(lista_tickets, lista_receita)
            print(Relatorio)
            print('Gráfico, lista de usuário: \n')
            grafico(lista_usuario)
            print('Gráfico, formas de pagamento: \n')
            grafico(lista_pagamento)
            print( '_'*43 )

if __name__ == '__main__':
    main()