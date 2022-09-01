def msg():
    print(30*'-')

print('QUESTÃO 3')
msg()

tbd = int(input('QUAL TABUADA VOCÊ QUER VER: '))
msg()
#Input para número da tabuada

c = 0
for x  in range(0,11):
    print(c,'X',tbd,'=',(c * tbd))
    c += 1
#print da tabuada completa de 0 até 10