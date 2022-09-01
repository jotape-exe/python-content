'''
Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. 
A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. 
Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, 
com valor default zero e os demais atributos são obrigatórios.
'''

def div():
    print(28*" - ")

class ContaCorerente:
        #Saldo = 0 por quê esse atributo não é obrigatório
    def __init__(self, num, nome, saldo=0):
        self.num = num
        self.nome = nome
        self.saldo = saldo

        #Obriga o usuário a digitar algo nestes dois campos
        if self.nome == None: 
            print("Campo obrigatório!")
            div()
        else:
            pass

        if self.num == None:
            print("Numero da conta incorreto!")
            div()
        else:
            pass
    
        #Apenas muda o atributo nome
    def muda_nome(self,new_name):
        print("{} agora seu nome é {}".format(self.nome, new_name))
        div()
        self.nome = new_name

        #Define um piso para o deposito: >= 11
        #Se for menor impede a ação
    def deposito(self, valor):
        if self.saldo < 10:
            print("Depósito invalido, tente com valores maiores que 10 R$")
            div()
        elif self.saldo >= 11:
            self.saldo += valor
            print("Voce depositou {} R$, seu saldo é de {} R$".format(valor, self.saldo))
            div()
    
    #Permite o saque e impede que o esperto saque mais do que ele tem
    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print("Você sacou {} R$, seu saldo é de {} R$".format(valor, self.saldo))
            div()
        else:
            print("Operação Inválida! Você tentou sacar {} R$, mas seu saldo é {} R$".format(valor, self.saldo))
            div()


user1 = ContaCorerente(12345, "João Pedro", 1000)
user2 = ContaCorerente(34412, "Anderson", 23400)

#Este usuário não possui sado na conta, mas possui conta e nome
user3 = ContaCorerente(45697, "Beatriz")
user4 = ContaCorerente(23578, "Marina", 789)

#Esse usuário tentou entrar sem os dados obrigatórios
userx = ContaCorerente(None, None) 


user1.saque(200)
user1.deposito(11)
user1.muda_nome("João Pedro Veríssimo")
user1.saque(100000)


user3.saque(300)
user3.deposito(3456)
user3.saque(3455)
user3.muda_nome("Bia")
