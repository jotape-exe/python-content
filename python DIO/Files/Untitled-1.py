def msg():
    print(40*'-')


print("Qual o melhor Sistema Operacional para uso em servidores?")
msg()

print('Escolha uma da opções:')
msg()
print('1- Windows Server \n2- Unix \n3- Linux \n4- Netware \n5- Mac OS \n6- Outro\n0-Finalizar')
msg()
value = int(input('Digite aqui: '))
msg()

while 0 < value > 6:
    print('Dados inválidos!')
    msg()
    value = int(input('Digite aqui: '))
    msg()
while value != 0:
    votos = []
    if value == 1:
        windows = int(input('Quantidade de votos na opção (1): '))
        votos.insert(windows, 0)
        msg()
        print('Escolha uma da opções:')
        msg()
        print('1- Windows Server \n2- Unix \n3- Linux \n4- Netware \n5- Mac OS \n6- Outro \n0-Finalizar')
        msg()
        value = int(input('Digite a proxima opção: '))
        msg()
        while 0 < value > 6:
            print('Dados inválidos!')
            msg()
            value = int(input('Digite aqui: '))
            msg()
    elif value == 2:
        Unix = int(input('Quantidade de votos na opção (2): '))
        votos.insert(Unix, 1)
        msg()
        print('Escolha uma da opções:')
        msg()
        print('1- Windows Server \n2- Unix \n3- Linux \n4- Netware \n5- Mac OS \n6- Outro \n0-Finalizar')
        msg()
        value = int(input('Digite a proxima opção: '))
        msg()
        while 0 < value > 6:
            print('Dados inválidos!')
            msg()
            value = int(input('Digite aqui: '))
            msg()
        
    elif value == 3:
        Linux = int(input('Quantidade de votos na opção (3): '))
        votos.insert(Linux, 2)
        msg()
        print('Escolha uma da opções:')
        msg()
        print('1- Windows Server \n2- Unix \n3- Linux \n4- Netware \n5- Mac OS \n6- Outro \n0-Finalizar')
        msg()
        value = int(input('Digite a proxima opção: '))
        msg()
        while 0 < value > 6:
            print('Dados inválidos!')
            msg()
            value = int(input('Digite aqui: '))
            msg()
    elif value == 4:
        Netware = int(input('Quantidade de votos na opção (4): '))
        votos.insert(Netware, 3)
        msg()
        print('Escolha uma da opções:')
        msg()
        print('1- Windows Server \n2- Unix \n3- Linux \n4- Netware \n5- Mac OS \n6- Outro \n0-Finalizar')
        msg()
        value = int(input('Digite a proxima opção: '))
        msg()
        while 0 < value > 6:
            print('Dados inválidos!')
            msg()
            value = int(input('Digite aqui: '))
            msg()
    elif value == 5:
        MacOS = int(input('Quantidade de votos na opção (5): '))
        votos.insert(MacOS, 4)
        msg()
        print('Escolha uma da opções:')
        msg()
        print('1- Windows Server \n2- Unix \n3- Linux \n4- Netware \n5- Mac OS \n6- Outro \n0-Finalizar')
        msg()
        value = int(input('Digite a proxima opção: '))
        msg()
        while 0 < value > 6:
            print('Dados inválidos!')
            msg()
            value = int(input('Digite aqui: '))
            msg()
    elif value == 6:
        Outro = int(input('Quantidade de votos na opção (6): '))
        votos.insert(Outro, 5)
        msg()
        print('Escolha uma da opções:')
        msg()
        print('1- Windows Server \n2- Unix \n3- Linux \n4- Netware \n5- Mac OS \n6- Outro \n0-Finalizar')
        msg()
        value = int(input('Digite a proxima opção: '))
        msg()
        while 0 < value > 6:
            print('Dados inválidos!')
            msg()
            value = int(input('Digite aqui: '))
            msg()
    elif value == 0:
        print('Dados armazenados!')
        msg()
        break;

total = Linux + MacOS + windows + Outro + Netware + Unix
print(total)