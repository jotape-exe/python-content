"""
Crie uma classe chamada Imóvel que deve conter os atributos "descricao" e “tipo”
(residencial ou comercial). Depois, você deve criar uma lista encadeada com vários imóveis.
Por fim, seu algoritmo deve retornar quantos imóveis existem de cada tipo (residencial ou
comercial) armazenados na lista.
"""

class No:
    def __init__(self, descricao, tipo, proximo=None):
        self.descricao = descricao
        self.tipo = tipo
        self.proximo = proximo

class Imovel:

    def __init__(self):
        self.principal = None

    def novo_imovel(self, descricao, tipo):
        if self.principal == None:
            self.principal = No(descricao, tipo)
            return
        
        atual = self.principal

        while atual.proximo is not None:
            atual = atual.proximo
        
        atual.proximo = No(descricao, tipo)


    def remover_imovel(self, descricao, tipo):
        if self.principal == None:
            return

        atual = self.principal

        if atual.descricao == descricao and atual.tipo == tipo:
            atual = atual.proximo
        
        anterior = None

        while True:
            anterior = atual
            atual = atual.proximo

            if atual is None:
                break

            if atual.descricao == descricao and atual.tipo == tipo:
                anterior.proximo = atual.proximo


    def mostrar_imoveis(self):
        atual = self.principal

        print(20*" - ")

        while atual is not None:
            print("O Imóvel {}, e do tipo {}".format(atual.descricao, atual.tipo))
            print(" ")
            atual = atual.proximo

    def contar_imoveis(self):
        print(20*" - ")
        comercial = 0
        residencial = 0
        atual = self.principal

        while atual != None:
            if atual.tipo == "residencial":
                residencial +=1
            elif atual.tipo == "comercial":
                comercial +=1
            atual = atual.proximo
        print("imoveis comerciais: {}".format(comercial))
        print(" ")
        print("Imoveis residenciais: {}".format(residencial))
        print(" ")

mrv = Imovel()

mrv.novo_imovel("Apartamento", "residencial")
mrv.novo_imovel("Loja Box", "comercial")
mrv.novo_imovel("Kitnet", "residencial")
mrv.novo_imovel("Predio", "comercial")
mrv.novo_imovel("Casa", "residencial")
mrv.novo_imovel("Loja", "comercial")
mrv.novo_imovel("Sitio", "residencial")

mrv.mostrar_imoveis()
mrv.contar_imoveis()

mrv.remover_imovel("Sitio", "residencial")
mrv.remover_imovel("Loja Box", "romercial")

mrv.mostrar_imoveis()
mrv.contar_imoveis()
