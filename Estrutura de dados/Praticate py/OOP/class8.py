'''
Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) 
e pelo menos os métodos comer(), verBucho() e digerir(). 
Faça um programa ou teste interativamente, 
criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes 
e verificando o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o outro. 
É possível criar um macaco canibal?
'''


#Esse código tem um problema fatal
#Eu posso fazer um macaco comer outro, e em seguida digeri-lo
#Mas ainda posso usar comandos no macaco ja digerido ;-;

def div():
    print(18*" - ")

class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []
    
        #come o alimento
    def comer(self, alimento):
        self.bucho.append(alimento)
        print("{} comeu {}".format(self.nome, alimento))
        div()

    def digerir(self):
        #Criei um indice para o macaco digerir o que ele comeu primeiro, ou seja
        #o ultimo elemto da lista
        #Ele tambem impede que o macaco de digerir de barriga vazia
        indice = len(self.bucho) - 1
        if len(self.bucho) > 0:
            print("{} digeriu {}".format(self.nome, self.bucho[indice]))
            self.bucho.pop()
        else:
            print("{} esta de barriga vazia!".format(self.nome))
        div()

        #Olha o conteudo do bucho
    def verBucho(self):
        if self.bucho == []:
            print("{} esta de barriga vazia!".format(self.nome))
            div()
        else:
            print("bucho do {} :".format(self.nome))
            for x in range(0, len(self.bucho)):
                print(self.bucho[x])
                x += 1
            div()
        


macaco1 = Macaco("Mico")
macaco2 = Macaco("Tito")

macaco1.verBucho()
macaco1.comer("Banana")
macaco1.comer("Manga")
macaco1.comer("Maracuja")
macaco1.verBucho()
macaco1.digerir()
macaco1.verBucho()

macaco1.comer(macaco2)
macaco1.digerir()
macaco1.digerir()
macaco1.digerir()
macaco1.digerir()
macaco1.digerir()
macaco1.verBucho()

macaco2.comer("Batata")