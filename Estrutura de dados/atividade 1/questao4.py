print('EXERCICIOS')
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

#Pontuação final do usuário
