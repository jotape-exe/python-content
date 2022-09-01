'''
Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. 

Ele deve pedir ao usuário que informe as medidades de um local. 
Depois, deve criar um objeto com as medidas e 
calcular a quantidade de pisos e de rodapés necessárias para o local.
'''

def div():
    print(20*"- ")

class Retangle:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def muda_lados(self):
        self.comprimento = float(input("Digite o comprimento (m): "))
        div()

        self.largura = float(input("Digite a largura (m): "))
        div()


    def prin_lados(self):
        print("Comprimento: {} cm // Largura {} m".format(self.comprimento, self.largura))
        div()

    #Calcula a área
    def areadef(self, area):
        area = self.comprimento * self.largura
        print("Area do retangulo: {} m^2".format(area))
        div()
    
    def perimetro(self):
        print("Perimetro do retangulo {} m".format(self.comprimento + self.largura))
        
    #Calcula a quantidade de pisos
    def qtd_piso(self, area, pisos):
        self.pisos = pisos
        self.pisos = float(input("Qual o tamanho dos pisos? em (cm)"))
        div()
        self.pisos / 100
        area = self.comprimento * self.largura

        print("Você precisará de aproximadamente {}".format(int(area / self.pisos )))


print("Informe as medidas do seu imóvel: \n")

retangulo = Retangle(0,0)

retangulo.muda_lados()

retangulo.areadef(0)

retangulo.qtd_piso(0,0)

