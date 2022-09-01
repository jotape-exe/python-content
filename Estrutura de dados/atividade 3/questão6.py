def msg():
    print(30*'-')
lname = []
n = 1

for x in range(0,5):
    name = input('DIGITE O {}º NOME: '.format(n))
    msg()
    n +=1
    lname.append(name)
#Recebe 5 nomes e armazena na lista 'lname'

print('---NOMES ABAIXO DE 5 LETRAS---')
msg()

for x in range(0, len(lname)):
    if len(lname[x]) < 5:
        print(lname[x])
        msg()
#Mostra os nomes menores que 5 letras