from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    cliente: Cliente
    anterior: No | None = None
    proximo: No | None = None


class Cliente:
    ''''
    inicia/cria a classe Cliente que armazena dados como idade, identificaçao e trocas, que é utilizado na funçao __pode_trocar, que verifica quantas vezes um cliente(nao idoso) ja trocou de lugar com outro (idoso). Ou seja, esse trocas é apenas um contador associado a cada cliente.
    '''
    def __init__(self,ident, idade):
        self.ident = ident
        self.idade = idade
        self.trocas = 0
        
    def __repr__(self):
        '''
        retorna uma string legivel dos dados de cliente para ser possivel vizualizar a ordem da fila
        '''
        return f"(cliente: {self.ident}, idade: {self.idade})"


class Encadupla:
    def __init__(self):
        '''
        cria uma lista duplamente encadeada
        '''
        self.__inicio = None
        self.__fim = None

    def enfileira(self,cliente)->None:
        '''
        Essa funçao ela vai enfileirar os clientes, porém para que os clientes obedeçam a ordem da fila, que é: apenas dois idosos podem passar na frente de um nao idoso, ela chama a funçao __verifica_troca, que faz a troca dos clientes, caso seja necessário.
        >>> fila = Encadupla()
        >>> fila.enfileira(Cliente('1', 21))
        >>> fila.enfileira(Cliente('2', 34))
        >>> fila.enfileira(Cliente('3', 65))
        >>> fila.mostrar_fila()
        '(cliente: 3, idade: 65), (cliente: 1, idade: 21), (cliente: 2, idade: 34)'
        '''

        novo_no = No(cliente)
        if self.vazia():
            self.__inicio = novo_no
            self.__fim = novo_no

        else:
            novo_no.anterior = self.__fim
            self.__fim.proximo = novo_no
            self.__fim = novo_no
            
        self.__verifica_troca(novo_no)

    def __verifica_troca(self, novo_no):
        '''
        verifica se a troca dos clientes pode ocorrer(chamando a funçao __pode_trocar), se for possivel ela efetua a troca dos clientes, caso nao ela mantem o cliente na posiçao que foi inserido, ela é bem semelhante com a funçao _pode_trocar, porem ela insere o cliente. Em outras palavras, essa funçao gerencia o processo de troca dos clientes.
        '''
        atual = self.__fim
        while atual and atual.anterior:
            cliente_novo = atual.cliente
            cliente_antigo = atual.anterior.cliente
            if cliente_novo.idade > 60:
                if self.__pode_trocar(cliente_antigo):
                    novox = atual.cliente
                    antigoy = atual.anterior.cliente
                    
                    atual.cliente = antigoy
                    atual.anterior.cliente = novox

                    cliente_novo.trocas += 1
                    cliente_antigo.trocas += 1
            atual = atual.anterior

    def __pode_trocar(self,cliente)-> bool:
        '''
        essa funçao vai verificar se o cliente que ja esta na fila pode trocar de lugar com o cliente que esta sendo inserido, ou seja, se o cliente que esta na fila nao excedeu o limite de vezes que pode trocar de posiçao (2) com pessoas idosas, essa funçao vai retornar True permitindo que ocorra o enfileiramento coreto, caso o cliente tenha feito 2 trocas, a funçao retorna False, nao permitindo que o cliente efetue a troca de lugar.
        '''
        limite_troca = 2
        if cliente != None and cliente.idade < 60:
            return cliente.trocas < limite_troca    
        

    def desenfileira(self):
        ''''
        Remove e retorna o primeiro cliente da fila.
        >>> fila = Encadupla()
        >>> fila.enfileira(Cliente('1', 29))
        >>> fila.enfileira(Cliente('2', 56))
        >>> fila.desenfileira()
        (cliente: 1, idade: 29)
        >>> fila.mostrar_fila()
        '(cliente: 2, idade: 56)'
        '''
        if self.vazia():
            raise ValueError('a fila está vazia')
        cliente_remov = self.__inicio.cliente
        self.__inicio = self.__inicio.proximo
        if self.__inicio != None:
            self.__inicio.anterior = None
        else:
            self.__fim = None
        
        return cliente_remov
        
    def mostrar_fila(self):
        '''
        Retorna uma string legivel de todos os clientes na fila
        '''
        if self.vazia():
            raise ValueError('a fila esta vazia')
        resultado = ''
        atual = self.__inicio
        while atual:
            resultado += str(atual.cliente)
            atual = atual.proximo
            if atual:
                resultado += ', '
        return resultado
    
    def primeiro_elemen(self):
        ''''
        retorna o primeiro elemento da fila sem remove-lo
        >>> fila = Encadupla()
        >>> fila.enfileira(Cliente('1', 55))
        >>> fila.enfileira(Cliente('2', 75))
        >>> fila.enfileira(Cliente('3', 80))
        >>> fila.mostrar_fila()
        '(cliente: 2, idade: 75), (cliente: 3, idade: 80), (cliente: 1, idade: 55)'
        >>> fila.primeiro_elemen()
        (cliente: 2, idade: 75)
        '''
        if self.__inicio != None:
            return self.__inicio.cliente
    

    def vazia(self) -> bool:
        '''
        essa funçao ira retornar se a fila esta vazia
        >>> fila = Encadupla()
        >>> fila.vazia()
        True
        >>> fila.enfileira(Cliente('1', 50))
        >>> fila.vazia()
        False
        '''
        return self.__inicio == None
    
    def __len__(self) -> int:
        '''
        essa funçao vai retornar a quantidade de elementos que tem na fila
        >>> fila = Encadupla()
        >>> fila.enfileira(Cliente('1', 79))
        >>> fila.enfileira(Cliente('2', 32))
        >>> len(fila)
        2
        '''
        if self.vazia():
            return 0
        contador = 0
        atual = self.__inicio
        while atual:
            contador += 1
            atual = atual.proximo
        return contador
    
    def esvazia(self) -> None:
        '''
        descarta os elementos da fila
        >>> fila = Encadupla()
        >>> fila.enfileira(Cliente('1', 79))
        >>> fila.enfileira(Cliente('2', 32))
        >>> fila.esvazia()
        >>> fila.mostrar_fila()
        Traceback (most recent call last):
            ...
        ValueError: a fila esta vazia
        '''
        self.__inicio = None
        self.__fim = None
            

def main():
    lista = Encadupla()
    Cliente1 =Cliente('1', 21)
    Cliente2 = Cliente('2', 34)
    cliente3 = Cliente('3', 67)
    cliente4 = Cliente('4', 61)
    cliente5 = Cliente('5', 72)
    cliente6 = Cliente('6', 54)
    cliente7 = Cliente('7', 75)
    lista.enfileira(Cliente1)
    lista.enfileira(Cliente2)
    lista.enfileira(cliente3)
    lista.enfileira(cliente4)
    lista.enfileira(cliente5)
    lista.enfileira(cliente6)
    lista.enfileira(cliente7)
    print(lista.mostrar_fila())
  



if __name__ == "__main__":
    main()