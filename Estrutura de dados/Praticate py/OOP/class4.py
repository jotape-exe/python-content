'''
Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. 
Obs: Por padrão, a cada ano que nossa pessoa envelhece, 
sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
'''

def div():
    print(20*"- ")


class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1

    def engordar(self):
        self.peso += 2

    def emagrecer(self):
        self.peso -= 1

    def crescer(self):
        if self.idade <= 21:
            self.altura += 0.5
        else:
            pass

    def imprimir(self):
        print("- - - - - - Dados de {} - - - - - - -".format(self.nome))
        print(self.nome,"sua idade atual é de",self.idade,"anos")
        div()
        print(self.nome,"seu peso atual é de",self.peso,"Kg")
        div()
        print(self.nome,"sua altura atual é de",self.altura,"cm")
        div()

user1 = Pessoa("João", 19, 80, 185)
user2 = Pessoa("Ana", 16, 46, 163)
user3 = Pessoa("Fernando", 20, 60, 170)
user4 = Pessoa("Marcos", 24, 90, 187)

user1.envelhecer()
user1.crescer()
user1.envelhecer()
user1.crescer()
user1.envelhecer()
user1.crescer()

user1.engordar()

user1.imprimir()

user2.envelhecer()
user2.crescer()
user2.envelhecer()
user2.crescer()
user2.envelhecer()
user2.crescer()

user2.emagrecer()
user2.emagrecer()
user2.emagrecer()

user2.imprimir()

