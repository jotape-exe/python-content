def msg():
    print(30*'-')

print('QUESTÃO 1')
msg()
nota = int(input('DIGITE SUA NOTA (0 A 10): '))
msg()
#input para nota

while nota < 0 or nota > 10:
    nota = int(input('ERROR! TRY AGAIN: '))
    msg()
#teto/piso para entrada de dados
#se a 0< nota > 10 continua até o número correto ser inserido

else:
    print('VOCÊ É NOTA {} !'.format(nota))
#se numero dentro do limite mostra a nota