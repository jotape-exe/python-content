def div():
    print(13*" - ")

class No:
    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo = proximo

class Lista:
    def __init__(self):
        self.principal = None
    
    def inserir(self, valor):
        if self.principal is None:
            self.principal = No(valor) #insere um valor na lista
            return
        
        atual = self.principal #valor inserido fica na posição atual

        while atual.proximo is not None:
            atual = atual.proximo #cria um nó entre o valor atual e o proximo
        
        atual.proximo = No(valor) #Se mais um valor for inserido criara um nó com o proximo
    
    def remover(self, valor):
        if self.principal is None:
            return
        
        atual = self.principal #valor atual é o no principal

        if atual.valor == valor: #Se o valor atual é o valor indicado, cria um nó com o proximo
            atual = atual.proximo
        
        anterior = None

        while True:
            anterior = atual 
            atual = atual.proximo

            if atual is None:
                break

            if atual.valor == valor:
                anterior.proximo = atual.proximo
    
    def imprimir(self):
        atual = self.principal

        while atual is not None:
            print(atual.valor)
            atual = atual.proximo
        div()

lista_node = Lista()

lista_node.imprimir()

lista_node.inserir(123)
lista_node.inserir(43)
lista_node.inserir(789)
lista_node.inserir(98)
lista_node.inserir(65)

lista_node.imprimir()

lista_node.remover(123)
lista_node.remover(65)
lista_node.remover(98)

lista_node.imprimir()