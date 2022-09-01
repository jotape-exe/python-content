def div():
    print(15*" - ")

#Essa pilha segue o LIFO, First in - Last out
class Pilha:
    def __init__(self):
        self.pilha_nomes = []
    
    def empilhar(self, nome):
        self.pilha_nomes.append(nome)
    
    def desempilhar(self):
        #desempilha os primeiros elementos
        if not self.vazia():
            return self.pilha_nomes.pop(-1)
    
    def vazia(self):
        #retorna a pilha vazia
        return len(self.pilha_nomes) == 0
    
    def mostre(self):
        if self.vazia():
            print("A pilha esta vazia!")
            
        else:
            #Isso inverte a ordem da lista, usando: start, stop, step
            for i in range(len(self.pilha_nomes)-1, -1, -1):
                print(self.pilha_nomes[i])
        div()
                

names1 = Pilha()

names1.mostre()

names1.empilhar("joão")
names1.empilhar("Ana")
names1.empilhar("Pedro")
names1.empilhar("Crhistina")
names1.empilhar("Marcos")
names1.empilhar("Manu")

names1.mostre()

names1.desempilhar()
names1.desempilhar()
names1.desempilhar()

names1.mostre()
