print('EXERCICIOS')

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

        print('A população do país A é de {} habitantes! '.format(int(pa)))
        print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('A população do país B é de {} habitantes! '.format(int(pb)))
        print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('Demorou {} anos para que a polução (A) ultrapasasse ou igualasse a população (B) '.format(anos))
        print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
#Mostra o resultado final