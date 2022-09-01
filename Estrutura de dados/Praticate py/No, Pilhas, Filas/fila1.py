def div():
    print(16*" - ")

#Esse modelo de lista segue o FIFO, First in, First out

class Fila:
    def __init__(self):
        self.list_nomes = []
    
    #elementos inseridos no topo da lista
    def enfileirar(self, elemento):
        self.list_nomes.append(elemento)

    #remover sempre o elemento do topo da fila
    def desenfileirar(self):
        if not self.fila_vazia():
            self.list_nomes.pop(0)

    #verifica se existe se algum elemto na fila
    def fila_vazia(self):
        return len(self.list_nomes) == 0

    #mais um print...
    def mostra_fila(self):
        if self.fila_vazia():
            print("Fila vazia. Insira algum valor!")
        else:
            for i in self.list_nomes:
                print(i)
        div()

fila1 = Fila()

fila1.mostra_fila()

fila1.enfileirar("João")
fila1.enfileirar("Karine")
fila1.enfileirar("Rafaela")
fila1.enfileirar("Carlos")
fila1.enfileirar("Juliana")

fila1.mostra_fila()

fila1.desenfileirar()
fila1.desenfileirar()
fila1.desenfileirar()

fila1.mostra_fila()