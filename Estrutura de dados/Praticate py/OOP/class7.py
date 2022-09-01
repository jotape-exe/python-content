'''
Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

Atributos: Nome, Fome, Saúde e Idade 

Métodos: Alterar Nome, Fome, Saúde e Idade; 
Retornar Nome, Fome, Saúde e Idade Obs: Existe mais uma informação que devemos levar em consideração, 
o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, 
então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.
'''

def div():
    print(20*" - ")

class Tamagushi:
    def __init__(self, nome=0, fome=50, saude=50, idade=99): #defini os valores para ficar semelhante aos jogos
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    #Apenas muda o nome
    def muda_nome(self, novo_nome): 
        self.nome = novo_nome
        print("O nome do seu pet é: {}".format(novo_nome))
        div()
    
    #dar alimento diminui a fome, se der alimento demais a fome vai a zero
    def muda_fome(self, alimento): 
        if alimento <= self.fome:
            self.fome -= alimento
        
        #piso de fome: 0
        elif alimento > self.fome:
            self.fome = 0
        print("A fome de {} está em {}% ".format(self.nome, self.fome))
        div()

        #O humor é inversamente proporcional a fome, quanto - fome + humor
        print("O humor de {} está em {}%".format(self.nome, (self.saude - self.fome)))
        div()
    
    def muda_saude(self, hp):
        if hp <= self.saude:
            self.saude += hp
            print("A saude de {} está em {}% ".format(self.nome, self.saude))
            div()
        
        #teto de HP: 100hp
        elif hp > self.saude:
            self.saude = 100
            print("A saude de {} está em {}% ".format(self.nome, self.saude))
            div()

        #O humor é diretamente proporcional a saude, quanto + saude + humor
        print("O humor de {} está em {}%".format(self.nome, (self.saude - self.fome)))
        div()
    
    def envelhecer(self):
        if self.idade < 100:
            self.idade += 1
            print("{} tem {} anos!".format(self.nome, self.idade))
            div()
        
        #teto de idade: 100 anos
        elif self.idade == 100:
            print("{} atingiu a idade máxima: {} anos".format(self.nome, self.idade))
            div()

pet = Tamagushi()

pet.muda_nome("Tamagushi")
pet.muda_fome(19)
pet.muda_saude(50)
pet.envelhecer()
pet.envelhecer()
pet.envelhecer()
pet.envelhecer()
