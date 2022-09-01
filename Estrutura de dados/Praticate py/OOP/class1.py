# Classe Bola: Crie uma classe que modele uma bola:
# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor

class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    
    def trocaCor(self):
        nova_cor = str(input("Digite a nova cor: "))
        
        self.cor = nova_cor

    def mostraCor(self):
        print(self.cor)

    #Esse bloco sempre vai mostrar a cor atual da bola, e vai perguntar se o usuário quer trocar de cor
    def contin(self):
        sn = 0
        while True:
            print("Cor atual: {}".format(self.cor))
            print(20*"- ")
            sn = input("Deseja mudar a cor da bola? ".lower())
            print(20*"- ")
            if sn == "sim":
                ball.trocaCor()
                print(20*"- ")
            else:
                break




ball = Bola("Azul", "20cm", "Polietileno")

ball.contin()



