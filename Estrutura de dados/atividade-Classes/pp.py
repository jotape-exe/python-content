class Pilha:

    def __init__(self):
        self.dados = []

    def empilhar(self, elemento):
        self.dados.append(elemento)

    def desempilhar(self):
        if not self.vazia():
            return self.dados.pop(-1)

    def vazia(self):
        return len(self.dados) == 0

    def imprimir(self):
        if self.vazia():
            print('A pilha está vazia!')
        else:
            print('-----------------')
            for i in range(len(self.dados) - 1, -1, -1):
                print(self.dados[i])
            print('-----------------')

p = Pilha()

p.imprimir()

p.empilhar(10)
p.empilhar(7)
p.empilhar(3)
p.empilhar(101)
p.empilhar(99)

p.imprimir()

p.desempilhar()
p.desempilhar()

p.imprimir()