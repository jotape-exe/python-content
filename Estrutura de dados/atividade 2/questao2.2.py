print('EXERCÍCIO')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('QUESTÃO 2')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

num = int(input('DIGITE SEU NUMERO DA SORTE: '))
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

#input para algum numero

while num % 2 == 0:
    num = int(input('SÓ NUMEROS IMPARES SÃO PERMITIDOS: '))
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

#divide 'num' por 2, se der zero continua perguntando até um número impar ser digitado

else:
    print('PARABÉNS, O NUMERO',num,'É UM NUMERO DE SORTE!')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
#print o número impar