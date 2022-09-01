lista = []
n = 1

def msg():
    print(30*'-')

print('QUESTÃO 2')
msg()

for x in range(0,5):
    num = int(input('DIGITE O {}º NÚMERO: '.format(n)))
    msg()
    n += 1
    lista.append(num)
#Entrada de 5 números, adicionados a lista: 'lista'

print('SOMA:',sum(lista))
msg()
#Comando 'sum', mostra a soma dos números na lista

print('MÉDIA: ',sum(lista) / 5)
#'sum' da lista divido por 5 é a média