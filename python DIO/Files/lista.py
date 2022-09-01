listanum = [12, 34, 56, 99]
listaname = ['Jonas','Ana','Mariana']

#print(listanum[0], listaname[0])
#localizar um elemento específico na lista

def mult():
    print(75 * '-')
#Função para printar um divisão no código

mult()
print(sum(listanum))

#Soma os números de uma lista (sum)
mult()
print(max(listaname))
mult()
#Maior número da lista/ maior string da lista

print(min(listaname))
#Menor número da lista/ menor string da lista

if 'Marco' in listaname:
    print('Marco está na lista!')
    mult()
else:
    listaname.append('Marco')
    mult()
    print('Marco não está na lista')
    mult()
    print('Marco será adicionado a lista: {}'.format(listaname))
    mult()
#Encontrando um elemento string usando 'if'

listaname.pop()
print('Marco foi removido da lsita: {}'.format(listaname))
mult()

list3 = listanum * 3
print(list3)
mult()
#Multiplica os elementos da lista x3, não os valores(també multiplica strings)