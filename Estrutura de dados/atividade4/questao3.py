def espaço():
    print(30*'-')

nums = []
num = int(input('DIGITE UM NÚMERO: '))
espaço()
divisão = 0

for x in range(1, num + 1):
    if num % x == 0:
        divisão += 1
        nums.append(x)
if divisão > 2:
    print(num,'NÃO É PRIMO')
    espaço()
    print('LISTA DE DIVISIVEIS:',nums)
elif divisão == 2:
    print(num,'É PRIMO')