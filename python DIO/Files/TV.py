class Tv:
    
    def __init__(self):
        self.ligada = False
#False é a tv desligada
        self.canal = 11
#numero do canal da tv
    
    def power(self):
        if self.ligada:
            self.ligada = False
#se tv = true/ tv = false
#liga a tv
        else:
            self.ligada = True
#senão tv = true
    def up_button(self):
        if self.ligada:
            self.canal += 1
#botão para aumentar o canal
    def down_button(self):
        if self.ligada:
            self.canal -= 1
#botão para diminuir o canal

television = Tv()
print('TV LIGADA: ',television.ligada)
television.power()
print('TV LIGADA: ',television.ligada)
television.power()
print('TV LIGADA: ',television.ligada)
#Checando se a tv está ligada ou não
print(26*'-')

print('CANAL ATUAL:',(television.canal))
television.power()
#ligo a tv com o power
print('TV LIGADA: ',television.ligada)
television.up_button()
television.up_button()
#Aumenta 2x o canal
print('CANAL ATUAL:',(television.canal))
television.down_button()
#Diminui 1x o canal
print('CANAL ATUAL:',(television.canal))
#Por fim mostra o canal atual