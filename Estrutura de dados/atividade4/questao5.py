num = int(input('DIGITE UM NÚMERO: '))
print(30*'-')
prim = []
c = 1
while c < num:
    if num % c == 0:
        prim.append(c)
    c += 1

if sum(prim) == num:
    print(num,'É UM NÚMERO PERFEITO!')
else:
    print(num,'NÃO É UM NÚMERO PERFEITO!')