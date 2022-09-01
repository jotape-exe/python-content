index = int(input('DIGITE O 1º NÚMERO: '))
end = int(input('DIGITE O 2º NÚMERO: '))
#Início e fim da contagem com 'X' números no intervalo

for x in range(index, end - 1):
    index += 1
    print(index)
#conta de index até end - 1(menos um para não mostrar o 'end')
#Index += 1, conta de um em um [1,2,3....x]