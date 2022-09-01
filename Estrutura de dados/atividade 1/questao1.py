print('EXERCICIOS')
print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

print('QUESTÃO 1')

print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
num1 = int(input('DIGITE O 1º NUMERO: '))
print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
num2 = int(input('DIGITE O 2º NUMERO: '))
print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
num3 = int(input('DIGITE O 3º NUMERO: '))
print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

#input para receber os três numeros

c = 0

#contador para o while

while c < 2:

#while vai rodar 2X, a vai mostrar 6 resultados

    if num1 % num2 == 0:
        print (num1,'É MULTIPLO DE',num2)
        print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        num1, num2 = num2, num1

    else:
        print (num1,'NÃO É MULTIPLO DE',num2)
        print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        num1, num2 = num2, num1

    if num3 % num2 == 0:
        print (num3,'É MULTIPLO DE',num2)       
        print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        num1, num3 = num3, num1
    else:
        print (num3,'NÃO É MULTIPLO DE',num2)
        print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        num1, num3 = num3, num1

    if num3 % num1 == 0:
        print (num3,'É MULTIPLO DE',num1)       
        print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        num3, num2 = num2, num3
    else:
        print (num3,'NÃO É MULTIPLO DE',num1)
        print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')     
        num3, num2 = num2, num3

#teste se um numero é divisivel por outro

    c += 1

#contador para while



        