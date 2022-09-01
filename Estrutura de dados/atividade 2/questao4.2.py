print('EXERCÍCIO')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('QUESTÃO 4')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

peso = int(input('QUANTOS QUILOS DE PEIXE VC PESCOU: '))
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

mult = 4

#Valor da multa que será paga por quilo a mais

cont = 0

#Conta quantas vezes a multa será aplicada

while peso > 50:
    cont += 1

#Para cada quilo maior que 50 adiciona +1 ao contador 

    if cont + 50 == peso:
        #mult = cont * 4
        print('VOCÊ PAGARÁ {}R$ DE MULTA!'.format(mult))
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

#Calcula o contador * valor da multa, e printa na tela

else:
    print('VOCÊ NÃO PAGARÁ MULTA!')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

#Aplicado a números menores que 50