class No:

    def __init__(self, nome, media, proximo=None):
        self.nome = nome
        self.proximo = proximo
        self.media = media


class Lista:
    def __init__(self):
        self.head = None

    def inserir(self, nome, media):
        if self.head is None:
            self.head = No(nome, media)
            return
        
        atual = self.head

        while atual.proximo is not None:
            atual = atual.proximo
        
        atual.proximo = No(nome, media)
    
    def apagar(self, nome, media):
        if self.head is None:
            return
        
        atual = self.head

        if atual.nome and atual.media == nome and media:
            self.head = atual.proximo
        
        anterior = None

        while True:
            anterior = atual
            atual =atual.proximo
        
            if atual is None:
                break

            if atual.nome and atual.media == nome and media:
                anterior.proximo = atual.proximo
            
    
    def imprimir(self):
        atual = self.head

        while atual is not None:
            print("Aluno:",atual.nome,", Média:",atual.media)
            atual = atual.proximo


chamada = Lista()

print('        Dia 1')
print('------------------------')

chamada.inserir("João", 10)
chamada.inserir("Pedro", 8.9)
chamada.inserir("Santana", 9.6)
chamada.inserir("Veríssimo", 8)

chamada.apagar("João", 10)

chamada.imprimir()