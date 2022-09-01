#Crie uma corrida em que os carros usem um nitro na velocidade X
car1 = 300
car2 = 295
car3 = 290

voltas = 0

while voltas < 11:
    print('VOLTA:',voltas)
    print(20*'-')
    print('KMH CARRO 1:',car1)
    print(20*'-')
    print('KMH CARRO 2:',car2)
    print(20*'-')
    print('KMH CARRO 3:',car3)
    print(20*'-')
    car1 += 2.5
    car2 += 2.25
    car3 += 2
    if car2 > car1 < car2:
        car1 += 1.3
        print('NITRO DO CARRO 1 USADO!!!')
        print(20*'-')
    if car1 > car2 < car3:
        car2 += 1.9
        print('NITRO DO CARRO 2 USADO!!!')
        print(20*'-')
    if car1 > car3 < car2:
        car3 +=2.5
        print('NITRO DO CARRO 3 USADO!!!')
        print(20*'-')
    voltas += 1


camp = (car1, car2, car3)

print('O CAMPEÃO É {}'.format(max(camp)))
print('CARRO 1:\n',car1)
print('CARRO 2:\n',car2)
print('CARRO 3:\n',car3)