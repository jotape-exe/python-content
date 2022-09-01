# Classe Quadrado: Crie uma classe que modele um quadrado:

# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def muda_lado(self):
        novo_lado = float(input("Digite o valor do lado do quadrado em (cm): "))
        self.lado = novo_lado

    def print_lado(self):
        print("Os lados do quadrado tem: {}".format(self.lado),"cm")

    def area(self):
        print("A area do seu quadrado é de {} ".format(self.lado**2),"cm")

def div():
    print(20*"- ")

quad = Quadrado(0) #Usei esse zero por que estou usando input, mas deve outro jeito....

quad.muda_lado()
div()
quad.print_lado()
div()
quad.area()