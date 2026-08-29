from __future__ import annotations
from typing import Any
from dataclasses import dataclass

@dataclass
class No:
    '''Representa um nó de uma árvore. Contém uma chave (dado de
    algum tipo sujeito a uma relação de ordem) e as referências 
    para subárvore esquerda e subárvore direita.'''
    chave: Any
    esquerda: No | None = None
    direita: No | None = None
    altura: int = 1  

class ArvoreAVL:
    '''Estrutura que mantém a propriedade da árvore AVL, que é uma
    árvore binária de busca balanceada.'''

    def __init__(self):
        '''Cria uma árvore AVL sem elementos.'''
        self.raiz = None

    def vazia(self) -> bool:
        '''Verifica se a árvore está vazia.
        
        Exemplos:
        >>> arvore = ArvoreAVL()
        >>> arvore.vazia()
        True
        >>> arvore.inserir(10)
        >>> arvore.vazia()
        False
        '''
        return self.raiz is None

    def altura(self, no: No | None) -> int:
        '''Retorna a altura de um nó.'''
        if no is None:
            return 0
        return no.altura

    def fator_balanceamento(self, no: No | None) -> int:
        '''Calcula o fator de balanceamento de um nó.'''
        if no is None:
            return 0
        return self.altura(no.esquerda) - self.altura(no.direita)

    def rotacionar_direita(self, y: No) -> No:
        '''Realiza uma rotação à direita em torno do nó y.'''
        x = y.esquerda
        T2 = x.direita

        x.direita = y
        y.esquerda = T2

        y.altura = (self.altura(y.esquerda) + 1) if (y.esquerda is not None) else 1
        y.altura = (self.altura(y.direita) + 1) if (y.direita is not None) else 1
        x.altura = (self.altura(x.esquerda) + 1) if (x.esquerda is not None) else 1
        x.altura = (self.altura(x.direita) + 1) if (x.direita is not None) else 1

        return x

    def rotacionar_esquerda(self, x: No) -> No:
        '''Realiza uma rotação à esquerda em torno do nó x.'''
        y = x.direita
        T2 = y.esquerda

        y.esquerda = x
        x.direita = T2

        x.altura = (self.altura(x.esquerda) + 1) if (x.esquerda is not None) else 1
        x.altura = (self.altura(x.direita) + 1) if (x.direita is not None) else 1
        y.altura = (self.altura(y.esquerda) + 1) if (y.esquerda is not None) else 1
        y.altura = (self.altura(y.direita) + 1) if (y.direita is not None) else 1

        return y

    def inserir(self, chave: Any) -> None:
        '''Insere uma nova chave na árvore AVL.
        
        Exemplos:
        >>> arvore = ArvoreAVL()
        >>> arvore.inserir(10)
        >>> arvore.inserir(20)
        >>> arvore.inserir(30)
        >>> arvore.raiz.chave
        20
        >>> arvore.raiz.esquerda.chave
        10
        >>> arvore.raiz.direita.chave
        30
        '''
        self.raiz = self._inserir(self.raiz, chave)

    def _inserir(self, no: No | None, chave: Any) -> No:
        '''Função auxiliar para inserir uma nova chave na árvore AVL.'''
        if no is None:
            return No(chave)

        if chave < no.chave:
            no.esquerda = self._inserir(no.esquerda, chave)
        else:
            no.direita = self._inserir(no.direita, chave)

        no.altura = 1
        if no.esquerda is not None:
            no.altura += self.altura(no.esquerda)
        if no.direita is not None:
            no.altura = max(no.altura, 1 + self.altura(no.direita))

        balanceamento = self.fator_balanceamento(no)

        if balanceamento > 1 and chave < no.esquerda.chave:
            return self.rotacionar_direita(no)

        if balanceamento < -1 and chave > no.direita.chave:
            return self.rotacionar_esquerda(no)

        if balanceamento > 1 and chave > no.esquerda.chave:
            no.esquerda = self.rotacionar_esquerda(no.esquerda)
            return self.rotacionar_direita(no)

        if balanceamento < -1 and chave < no.direita.chave:
            no.direita = self.rotacionar_direita(no.direita)
            return self.rotacionar_esquerda(no)

        return no

    def exibir_pre_ordem(self, no: No | None) -> str:
        '''Exibe a árvore em pré-ordem.
        
        Exemplos:
        >>> arvore = ArvoreAVL()
        >>> arvore.inserir(10)
        >>> arvore.inserir(20)
        >>> arvore.inserir(30)
        >>> arvore.exibir_pre_ordem(arvore.raiz)
        '(20 (10  ) (30  ))'
        '''
        if no is None:
            return ''
        return f'({no.chave} {self.exibir_pre_ordem(no.esquerda)} {self.exibir_pre_ordem(no.direita)})'

    def remover(self, chave: Any) -> None:
        '''Remove uma chave da árvore AVL.
        
        Exemplos:
        >>> arvore = ArvoreAVL()
        >>> arvore.inserir(10)
        >>> arvore.inserir(20)
        >>> arvore.inserir(30)
        >>> arvore.remover(10)
        >>> arvore.exibir_pre_ordem(arvore.raiz)
        '(20  (30  ))'
        '''
        self.raiz = self._remover(self.raiz, chave)

    def _remover(self, no: No | None, chave: Any) -> No | None:
        '''Função auxiliar para remover uma chave da árvore AVL.'''
        if no is None:
            return no

        if chave < no.chave:
            no.esquerda = self._remover(no.esquerda, chave)
        elif chave > no.chave:
            no.direita = self._remover(no.direita, chave)
        else:
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda

            temp = self._minimo(no.direita)
            no.chave = temp.chave
            no.direita = self._remover(no.direita, temp.chave)

        no.altura = 1
        if no.esquerda is not None:
            no.altura += self.altura(no.esquerda)
        if no.direita is not None:
            no.altura = max(no.altura, 1 + self.altura(no.direita))
        balanceamento = self.fator_balanceamento(no)

        if balanceamento > 1 and self.fator_balanceamento(no.esquerda) >= 0:
            return self.rotacionar_direita(no)

        if balanceamento < -1 and self.fator_balanceamento(no.direita) <= 0:
            return self.rotacionar_esquerda(no)

        if balanceamento > 1 and self.fator_balanceamento(no.esquerda) < 0:
            no.esquerda = self.rotacionar_esquerda(no.esquerda)
            return self.rotacionar_direita(no)

        if balanceamento < -1 and self.fator_balanceamento(no.direita) >  0:
            no.direita = self.rotacionar_direita(no.direita)
            return self.rotacionar_esquerda(no)

        return no

    def _minimo(self, no: No) -> No:
        '''Retorna o nó com a menor chave na árvore.'''
        if no is None or no.esquerda is None:
            return no
        return self._minimo(no.esquerda)

    def menor_ancestral_comum(self, n1: Any, n2: Any) -> No | None:
        '''Encontra o menor ancestral comum de n1 e n2.'''

        return self._menor_ancestral_comum(self.raiz, n1, n2)

    def _menor_ancestral_comum(self, no: No | None, n1: Any, n2: Any) -> No | None:
        '''Função auxiliar para encontrar o menor ancestral comum.'''
        if no is None:
            return None

        if no.chave > n1 and no.chave > n2:
            return self._menor_ancestral_comum(no.esquerda, n1, n2)

        if no.chave < n1 and no.chave < n2:
            return self._menor_ancestral_comum(no.direita, n1, n2)

        return no

def main():
    arvore = ArvoreAVL()
    elementos = [20, 10, 30, 5, 15, 25, 35]
    for elemento in elementos:
        arvore.inserir(elemento)

    n1 = 5
    n2 = 15
    ancestral_comum = arvore.menor_ancestral_comum(n1, n2)
    if ancestral_comum:
        print(f'O menor ancestral comum de {n1} e {n2} é: {ancestral_comum.chave}')
    else:
        print('Ancestral comum não encontrado.')

if __name__ == "__main__":
    main()