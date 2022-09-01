print('EXERCÍCIO')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('QUESTÃO 5')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

name = str(input('SEU NOME: '))
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
mf = str(input('QUAL O SEU SEXO (M) OU (F): ')).upper
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
h = float(input('QUAL SUA ALTURA EM METROS: '))
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
peso = int(input('QUAL O SEU PESO EM QUILOS: '))
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

#Variáveis que recebem as pgts 

pesoidm = int((72.7*h) - 58)
pesoidf = int((62.1*h) - 44.7)

#Calculo do de peso ideal

if mf == 'F' or 'FEMININO':
    if peso == pesoidf:
        print(name,'VOCÊ TEM O PESO IDEAL!')
    elif peso > pesoidf:
        print(name,'VOCÊ ESTÁ ACIMA DO PESO IDEAL, PESO IDEAL:',pesoidf,'KG')
    else:
        print(name,'VOCÊ ESTÁ ABAIXO DO PESO IDEAL, PESO IDEAL:',pesoidf,'KG')

#retorna o resultado caso seja feminino

elif mf == 'M' or 'MASCULINO':
    if peso == pesoidm:
        print(name,'VOCÊ TEM O PESO IDEAL!')
    elif peso > pesoidm:
        print(name,'VOCÊ ESTÁ ACIMA DO PESO IDEAL, PESO IDEAL:',pesoidm,'KG')
    else:
        print(name,'VOCÊ ESTÁ ABAIXO DO PESO IDEAL, PESO IDEAL:',pesoidm,'KG')

#retorna o resultado caso seja masculino
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')