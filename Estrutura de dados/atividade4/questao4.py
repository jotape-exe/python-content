num = int(input('QUANTOS NÚMEROS VOCÊ QUER DIGITAR? '))
s = []
x = 1

while x <= num:
    numero = int(input('DIGITE O {}º NUMERO: '.format(x)))
    x += 1
    s.append(numero)
    print(30*'-')

s.sort()
print('ORDEM CRESCENTE:',s)