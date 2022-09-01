class No:
    def __init__(self, descricao, tipo, proximo=None):
        self.descricao = descricao
        self.tipo = tipo
        self.proximo = proximo

class Imovel:

    #O head é a cabeça de um nó
    def __init__(self):
        self.head = None

    #Inicia o nó declarando o tipo e a descrição do nó atual
    def inserir(self, tipo, descricao):
        if self.head is None:
            self.head = No(tipo, descricao)
            return #por que esse return?

    #Elemento atual é colocado no head do nó
        atual = self.head

    #Se existe um item na sequencia torne o item atual, o proximo item
        while atual.proximo is not None:
            atual = atual.proximo
        
        atual.proximo = No(tipo, descricao)

    #Função para apagar um nó
    def apagar(self, tipo, descricao):
        if self.head is None:
            return
        
        atual = self.head

        #Se a descrição e o tipo do nó atual forem iguais a descrição e tipos especificados ...
        # ... o head se torna o proximo
        if atual.tipo and atual.descricao == tipo and descricao:
            self.head = atual.proximo
        
        #Não é necessario verificar o item anterior
        anterior = None

        while True:
            #Sempre torne o anterior = ao atual
            #E o atual = ao proximo
            anterior = atual
            atual = atual.proximo
        
            if atual is None:
                break
            #Quando não houver nenhum na posição atual, pare

            if atual.tipo and atual.descricao == tipo and descricao:
                anterior.proximo = atual.proximo
            #Se a descrição e o tipo do nó atual forem iguais a descrição e tipos especificados
            #Elimine o anterior e substitua pelo proximo
            
    #Função para printar na tela
    def imprimir(self):
        atual = self.head

        while atual is not None:
            print("Descrição:",atual.descricao," -  Tipo:",atual.tipo)
            atual = atual.proximo

    #size?
    def size(self):
        count1 = 0
        count2 = 0
        atual = self.head

        while atual != None:
            if atual.tipo == "residencial":
                count1 += 1
            elif atual.tipo == "comercial":
                count2 += 1
            atual = atual.proximo

        print('-----------------------------')
        print("Imóveis residenciais:",count1)
        print('-----------------------------')
        print("Imóveis comercias:", count2)


imoveis =Imovel()

imoveis.inserir("Casa", "comercial")
imoveis.inserir("Apartamento", "residencial")
imoveis.inserir("Chacara", "residencial")
imoveis.inserir("Casa1", "comercial")
imoveis.inserir("Apartamento1", "residencial")
imoveis.inserir("Chacara1", "residencial")
imoveis.inserir("Casa2", "comercial")
imoveis.inserir("Apartamento2", "residencial")
imoveis.inserir("Chacara2", "residencial")

imoveis.apagar("Casa", "comercial")

print('IMÓVEIS')
print('--------------------')
imoveis.imprimir()

imoveis.size()
