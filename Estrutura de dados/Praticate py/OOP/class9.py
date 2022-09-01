'''
Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:

A - Possua uma classe chamada Ponto, com os atributos x e y.
B - Possua uma classe chamada Retangulo, com os atributos largura e altura.
C - Possua uma função para imprimir os valores da classe Ponto
D - Possua uma função para encontrar o centro de um Retângulo.
E - Você deve criar alguns objetos da classe Retangulo.
F - Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, 
que deve ser um objeto da classe Ponto.
G - A função para encontrar o centro do retângulo deve retornar 
o valor para um objeto do tipo ponto que indique os valores de x e y para o centro do objeto.
H - O valor do centro do objeto deve ser mostrado na tela
I - Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.
'''

def div():
    print(15*" - ")

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    

class Retangulo:
    def __init__(self, largura, altura):
        self.altura = altura
        self.largura = largura
    
    def center_rtgl(self):
        x_centro = (self.altura.x + self.largura.x)/2 #calcula o primeiro vertice, denominado "inferior"
        y_centro = (self.altura.y + self.largura.y)/2 #calcula o segundo vertice, denominado "superior"
        return "X=" + str(x_centro) + "Y=" + str(y_centro) #retorna as variaveis como string


while loop == 0: #um loop mal feito
    x_ie = float(input("Valor do canto x, inferior esquerdo: "))
    div()
    y_ie = float(input("Valor do canto y, inferior esquerdo: "))
    div()
    canto1 = Ponto(x_ie, y_ie) #calcula o primeiro ponto
    x_sd = float(input("Valor do canto x, superior direito: "))
    div()
    y_sd = float(input("Valor do canto y, superior direito: "))
    div()
    canto2 = Ponto(x_sd, y_sd) #calcula o segundo ponto

    retangle = Retangulo(canto1, canto2)

    print("O ponto central do retangulo é %s"%retangle.center_rtgl()) #calcula o centro do retangulo (X, Y)
    div()

    loop = str(input("Deseja continuar? ").lower())
    div()

    if loop != "sim":
        loop = 1
    elif loop == "sim":
        loop = 0
