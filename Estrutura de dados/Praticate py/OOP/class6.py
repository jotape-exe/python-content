'''
Classe TV: Faça um programa que simule um televisor criando-o como um objeto. 
O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. 
Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.
'''

def div():
    print(14*" - ")

class Tv:
    def __init__(self, canal=49, volume=1):
        self.canal = canal
        self.volume = volume

    #Aumenta +1 canal até o teto do canal 50
    def canal_up(self):
        self.canal += 1
        if self.canal > 50:
            self.canal = 1
        print("Você esta no canal {}".format(self.canal))
        div()
    
    #Dimunui -1 canal até o piso do canal 1
    def canal_down(self):
        self.canal -= 1
        if self.canal < 0:
            self.canal = 50
        print("Você esta no canal {}".format(self.canal))
        div()

    #Aumenta o volume até o teto de 100
    def sound_up(self):
        if  self.volume < 100:
            self.volume += 1
            print("volume: {}".format(self.volume))
            div()
        else:
            print("Volume máximo!")
            div()

    #Diminui o volume até o piso 0 "Zero"
    def sound_down(self):
        if  self.volume > 0:
            self.volume -= 1
            print("volume: {}".format(self.volume))
            div()
        else:
            print("Volume mínimo!")
            div()
    
televisao = Tv()

televisao.canal_up()
televisao.canal_up()
televisao.canal_up()
televisao.canal_up()

televisao.sound_down()
televisao.sound_down()

televisao.sound_up()
televisao.sound_up()
televisao.sound_up()
televisao.sound_up()
televisao.sound_up()