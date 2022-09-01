def div():
    print(13*" - ")

class No:
    def __init__(self, nome, media, proximo=None):
        self.nome = nome
        self.proximo = proximo
        self.media = media

class Lista:
    def __init__(self):
        self.principal = None
    
    def append_aluno_media(self, nome, media):
        if self.principal == None:
            self.principal = No(nome, media)
            return
        
        atual = self.principal

        while atual.proximo is not None:
            atual = atual.proximo
        
        atual.proximo = No(nome, media)
    
    def remove_aluno_media(self, nome, media):
        if self.principal is None:
            return
        
        atual = self.principal

        if atual.nome == nome and atual.media == media:
            atual = atual.proximo
        
        anterior = None

        while True:
            anterior = atual
            atual = atual.proximo

            if atual is None:
                break

            if atual.nome == nome and atual.media == media:
                anterior.proximo = atual.proximo
    
    def mostrar(self):
        atual = self.principal

        while atual is not None:
            print(atual.nome,", sua média é:",atual.media)
            atual = atual.proximo
        div()

sala1 = Lista()

sala1.append_aluno_media("João Pedro", 10)
sala1.append_aluno_media("Carlos", 9)
sala1.append_aluno_media("Julia", 10)
sala1.append_aluno_media("André", 8)
sala1.append_aluno_media("Fernanda", 8.9)

sala1.mostrar()

sala1.remove_aluno_media("Julia", 10)

sala1.mostrar()