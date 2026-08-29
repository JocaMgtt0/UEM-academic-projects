from arranjo import Array
class Cliente:
    ''''
    inicia/cria a classe Cliente que armazena dados como idade, identificaçao e trocas, que é utilizado na funçao __pode_trocar, que verifica quantas vezes um cliente(nao idoso) ja trocou de lugar com outro (idoso). Ou seja, esse trocas é apenas um contador associado a cada cliente.
    '''
    def __init__(self,ident, idade):
        self.ident = ident
        self.idade = idade
        self.trocas = 0
        
    def __repr__(self):
        ''''
        retorna uma string legivel dos dados de cliente para ser possivel vizualizar a ordem da fila
        '''
        return f"(cliente: {self.ident}, idade: {self.idade})"


class Arranjo:
    def __init__(self, tamanho):
        '''
        metodo construtor que inicia a classe arranjo.
        '''
        self.__inicio = 0
        self.__fim = 0 
        self.__tamanho = tamanho
        self.__lista = Array(tamanho +1)
        

    def enfileira(self,elemento)->None:
        '''
        enfileira elementos na fila
        >>> Fila = Arranjo(7)
        >>> Fila.enfileira(Cliente('1', 21))
        >>> Fila.enfileira(Cliente('2', 34))
        >>> Fila.enfileira(Cliente('3', 67))
        >>> Fila.enfileira(Cliente('4', 61))
        >>> Fila.enfileira(Cliente('5', 72))
        >>> Fila.enfileira(Cliente('6', 54))
        >>> Fila.enfileira(Cliente('7', 75))
        >>> Fila.mostrar_fila()
        [(cliente: 3, idade: 67), (cliente: 4, idade: 61), (cliente: 1, idade: 21), (cliente: 2, idade: 34), (cliente: 5, idade: 72), (cliente: 7, idade: 75), (cliente: 6, idade: 54)]
        '''
        if self.cheia():
            raise ValueError('fila cheia')
        else:

            self.__lista[self.__fim] = elemento
            self.__fim += 1
            

            for i in range(self.__fim -1, -1, -1):
                cliente_novo = self.__lista[i]
                cliente_antigo = self.__lista[i-1]
                if cliente_novo.idade > 60:
                    if self.__pode_trocar(cliente_antigo):
                        self.__lista[i] = cliente_antigo
                        self.__lista[i-1] = cliente_novo
                        cliente_novo.trocas += 1
                        cliente_antigo.trocas += 1


    def __pode_trocar(self,cliente)-> bool:
        '''
        essa funçao vai verificar se o cliente que ja esta na fila pode trocar de lugar com o cliente que esta sendo inserido, ou seja, se o cliente que esta na fila nao excedeu o limite de vezes que pode trocar de posiçao (2) com pessoas idosas, essa funçao vai retornar True permitindo que ocorra o enfileiramento coreto, caso o cliente tenha feito 2 trocas, a funçao retorna False, nao permitindo que o cliente efetue a troca de lugar.
        '''
        limite_troca = 2
        if cliente != None and cliente.idade < 60:
            return cliente.trocas < limite_troca    
        

    def desenfileira(self):
        ''''
        retira um elemento da fila.
        >>> Fila = Arranjo(3)
        >>> Fila.enfileira(Cliente('1', 29))
        >>> Fila.enfileira(Cliente('2', 56))
        >>> Fila.enfileira(Cliente('3', 70))
        >>> Fila.mostrar_fila()
        [(cliente: 3, idade: 70), (cliente: 1, idade: 29), (cliente: 2, idade: 56)]
        >>> Fila.desenfileira()
        (cliente: 3, idade: 70)
        >>> Fila.mostrar_fila()
        [(cliente: 1, idade: 29), (cliente: 2, idade: 56)]
        '''
        if self.vazia():
            raise ValueError('a fila está vazia')
        else:
            elemento = self.__lista[self.__inicio] 
            self.__inicio +=1
            return elemento

    def mostrar_fila(self):
        '''
        funçao que exibe a fila no terminal para poder ser vizualizado a ordem da mesma
        '''
        return self.__lista[self.__inicio:self.__fim]
    
    def primeiro_elemen(self):
        ''''
        retorna o primeiro elemento da fila sem remove-lo
        >>> Fila = Arranjo(3)
        >>> Fila.enfileira(Cliente('1', 55))
        >>> Fila.enfileira(Cliente('2', 75))
        >>> Fila.enfileira(Cliente('3', 80))
        >>> Fila.mostrar_fila()
        [(cliente: 2, idade: 75), (cliente: 3, idade: 80), (cliente: 1, idade: 55)]
        >>> Fila.primeiro_elemen()
        (cliente: 2, idade: 75)
        '''
        return self.__lista[self.__inicio]
    

    def vazia(self) -> bool:
        '''
        essa funçao ira retornar se a fila esta vazia
        >>> Fila = Arranjo(3)
        >>> Fila.vazia()
        True
        >>> Fila.enfileira(Cliente('1', 50))
        >>> Fila.vazia()
        False
        '''
        return self.__inicio == self.__fim
    
    def cheia(self) -> bool:
        '''
        verifica se a fila está cheia
        >>> Fila = Arranjo(3)
        >>> Fila.enfileira(Cliente('1', 79))
        >>> Fila.enfileira(Cliente('2', 32))
        >>> Fila.cheia()
        False
        >>> Fila.enfileira(Cliente('3', 21))
        >>> Fila.cheia()
        True

        '''
        return self.__fim == self.__tamanho
    def __len__(self) -> int:
        '''
        essa funçao vai retornar a quantidade de elementos que tem na fila
        >>> Fila = Arranjo(3)
        >>> Fila.enfileira(Cliente('1', 79))
        >>> Fila.enfileira(Cliente('2', 32))
        >>> Fila.__len__()
        2
        '''
        if self.vazia():
            return 0
        if self.__fim >= self.__inicio:
            return self.__fim - self.__inicio
    
    def esvazia(self) -> None:
        '''
        descarta os elementos da fila
        >>> Fila = Arranjo(3)
        >>> Fila.enfileira(Cliente('1', 79))
        >>> Fila.enfileira(Cliente('2', 32))
        >>> Fila.esvazia()
        >>> Fila.mostrar_fila()
        []
        '''
        self.__inicio = 0
        self.__fim = 0
            

def main():
    lista = Arranjo(7)
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