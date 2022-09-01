def espaço():
    print(37*'-')

cars = ['FUSCÃO', 'GOL', 'GOLF', 'UNO', 'PARATI']
consu = [10, 14, 9, 8, 7]

print('         MODELOS')
espaço()

for x in range(0, len(cars)):
    print(cars[x],'- CONSUMO:',consu[x],'KM POR LITRO')
    espaço()

print('         MODELO ECONOMICO')
espaço()

for x in range(0, len(cars)):
    if consu[x] == max(consu):
        print(cars[x],'- CONSUMO:',consu[x],'KM POR LITRO')

espaço()
print('       CONSUMO POR 1.000 KM')
espaço()

for x in range(0, len(cars)):
    print(cars[x],'-',int(((1000 / consu[x])*6.25)), 'R$ POR 1.000 KM')
    print('LITROS GASTOS:',int(1000/consu[x]))
    espaço()