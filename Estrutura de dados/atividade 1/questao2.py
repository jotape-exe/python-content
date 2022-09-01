print('EXERCICIOS')
print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

print('QUESTÃO 2')

print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('= FAÇA O DOWLOAD DO WINDOWS 7 !                   =')

print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('= TAMANHO DO ARQUIVO: 8.000 Mb ou 8GB             =')
print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

#Introdução ao problema

print('= Use um dos links para download:                 =')
print('= LINK 1: 100 Mbps                                =')
print('= LINK 2: 30 Mbps                                 =')

#Informa os links para download

print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
temp = int(input('= LINK 1 (DIGITE "1") OU LINK 2 (DIGITE "2") ? '))
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