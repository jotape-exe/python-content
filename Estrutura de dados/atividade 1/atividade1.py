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

#teste se um numero é divisivel por outro, e informa o resultado

    c += 1
    
#contador para while


print('QUESTÃO 2')

print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('FAÇA O DOWLOAD DO WINDOWS 7 !')

print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('TAMANHO DO ARQUIVO: 8.000 Mb ou 8GB')
print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

#Introdução ao problema

print('Use um dos links para download: ')
print('LINK 1: 100 Mbps')
print('LINK 2: 30 Mbps')

#Informa os links para download

print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
temp = int(input('LINK 1 (DIGITE "1") OU LINK 2 (DIGITE "2") ? '))
print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

#Input para escolher os links

mb = 8000
one = int((mb / 100) / 60)
two = int((mb / 30) / 60)

#Calculo do tempo em minutos

if temp == 1:
    print('SEU DOWNLOAD TEM UM TEMPO ESTIMADO DE {} MINUTOS.....'.format(one))
else:
    print('SEU DOWNLOAD TEM UM TEMPO ESTIMADO DE {} MINUTOS.....'.format(two))
    
#Mostra os dois resultados possíveis

print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('QUESTÃO 3')
print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

print('PAÍS A: POPULAÇÃO DE 80.000 HABITANTES')

print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('PAÍS B: POPULAÇÃO DE 200.000 HABITANTES')
print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('O tempo passa..........')
print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

#Mostra a população atual dos Países A & B

pa = 80000
pb = 200000
anos = 0
while pa <= pb:
    pa = (0.3 * pa) + pa
    anos += 1
    pb = (0.15 * pb) + pb

    if pa > pb:

#Calcula a população de A & B, e calcula a quantidade de anos

        print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('A população do país A é de {} habitantes! '.format(int(pa)))
        print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('A população do país B é de {} habitantes! '.format(int(pb)))
        print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('Demorou {} anos para que a polução A ultrapasasse a população B '.format(anos))
        print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
#Mostra o resultado final

print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

print('QUESTÃO 4')

print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('Responda com "sim" ou "não": ')
print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

sus = 0
#Variavel para medir seu nível de 'suspeito'

p1 = input(str("Telefonou para a vítima? "))
if p1 == 'sim':
    sus += 1
print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

p2 = input(str("Esteve no local do crime? "))
if p2 == 'sim':
    sus += 1
print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

p3 = input(str("Mora perto da vítima? "))
if p3 == 'sim':
    sus += 1
print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

p4 = input(str("Devia para a vítima? "))
if p4 == 'sim':
    sus += 1
print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

p5 = input(str("Já trabalhou com a vítima? "))
if p5 == 'sim':
    sus += 1
print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

#De p1 até p5 são perguntas que adiciona pontução a variavel 'sus', teto de 5pts/ piso de 0pts
#Deve haver um jeito mais simples do que simplismente usar vários (IF'S)...
if sus == 2:
    print('SUSPEITO -_-')

elif 4>= sus >=3:
    print('CUMPLICE °-°')

elif sus == 5:
    print('ASSASINO! x_x')

elif sus == 0:
    print('INOCENTE :)')

#Mostra sua classificação de acordo com as perguntas que você respondeu

print('Pontuação final: {} pontos!'.format(sus))
print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('FIM DO PROGRAMA !')
#Pontuação final do usuário
