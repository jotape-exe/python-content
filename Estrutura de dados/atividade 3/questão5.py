def msg():
    print(30*'-')

nota1=float(input("NOTA 1: "))
msg()
nota2=float(input("NOTA 2: "))
msg()
#input para as duas notas

media=(nota1+nota2)/2
#Calcula média das notas

if nota1 < 0 or nota1 >10 or nota2 <0 or nota2 >10:
    print('DADOS INVALIDOS')
#Nota maior que 10 esperto? acho que não...

else:
    if 10<= media >9:
        let = "A"
    elif 9<= media > 7.5:
        let = "B"
    elif 7.5<= media >6:
        let = "C"
    elif 6<= media > 4:
        let = "D"
    elif 4<= media >= 0:
        let = "E"
#Variavel 'let' recebe o conceito de acordo com a média

    print('SUA MÉDIA:',media)
    msg()
    print('NOTA:',let)
#print da média e da nota(conceito, A, B, C, D, E)