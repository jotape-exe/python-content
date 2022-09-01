#Objetivo: crie um sistema de loja que possa controlar a entrada e saida de celulares do estoque
#Ex: Xiaomi note 11, Iphone 12, Sansung S22, Motog 100
#Manipule a entrada e saida desses aparelhos por meio de classes
#voce deve especificar o tipo do aparelho e seus componentes

def sep():
    print(20*"- - ")

class No:
    def __init__(self, modelo, ram, rom, proximo=None):
        self.modelo = modelo
        self.ram = ram
        self.rom = rom
        self.proximo = proximo

class Smartphone:
    def __init__(self):
        self.head = None
    
    def cadastro(self, modelo, ram, rom):
        if self.head is None:
            self.head = No(modelo, ram, rom)
            return

        atual = self.head

        while atual.proximo is not None:
            atual = atual.proximo
        
        atual.proximo = No(modelo, ram, rom)
    
    def remover(self, modelo, ram, rom):
        if self.head is None:
            return

        atual = self.head

        if atual.modelo and atual.ram and atual.rom == modelo and ram and rom:
            self.head = atual.proximo

        anterior = None

        while True:
            anterior = atual
            atual = atual.proximo
            
            if atual is None:
                break

            elif atual.modelo == modelo: #tentei usar o 'and', para comparar 3 elemetos, mas não funcionou
                anterior.proximo = atual.proximo
            
    
    def mostrar(self):
        atual = self.head

        while atual is not None:
            print("Modelo:",atual.modelo,"/ componentes /","Ram:",atual.ram,"Rom:",atual.rom,)
            atual = atual.proximo
            sep()

celular = Smartphone()

print(28*" ","Aparelhos cadastrados\n")

celular.cadastro("Iphone 13", "16GB", "256GB")
celular.cadastro("Iphone 11", "8GB", "126GB")
celular.cadastro("Moto G 100", "8GB", "126GB")
celular.cadastro("Sansumg S22 ultra", "16GB", "256GB")
celular.cadastro("Sansung Note 22", "8GB", "126GB")

celular.mostrar()

#simulação de aparelho indevido na lista
print(" ")
print(20*"+ + ")
print(17*" ","Erro, 'Moto G 100' não pertence ao sistema!\n")
print(20*" ","Intruções: Remove-lo imediatamente")
print(20*"+ + ","\n")

celular.remover("Moto G 100", "8GB", "126GB")

celular.mostrar()