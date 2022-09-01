def msg():
    print(50*'-')

lista = [[], []]
num = 0
c = 1

while c < 21:
    num = int(input('DIGITE O {}º NÚMERO: '.format(c)))
    c += 1
#input para os 20 números, contador 'c' para organizar
    if num % 2 == 0:
        lista[0].append(num)
#Divide e diciona a lista dos pares, caso o resro seja: 0
    else:
        lista[1].append(num)
#Caso contrário vai para a lista ímpar

print('LISTA COMPLETA:',lista)
msg()
print('LISTA DE PARES:', lista[0])
msg()
print('LISTA DE ÍMPARES:', lista[1])
#Mostra todas as listas