def shell_sort(inp, n):
 
    h = n // 2
    #define o intervalo das sublistas
    #h = 4
    while h > 0:
        #laço de repetição para ver se h é maior que zero
        for i in range(h, n):
            t = inp[i]
            #elemento atual
            j = i
            #indice
            while j >= h and inp[j - h] > t:
                #enquanto o indice for >= ao intervalo & a o antecessore forem maiores que o vetor
                inp[j] = inp[j - h]
                #muda j "h" casas
                j -= h 
            inp[j] = t
            print(inp, "intervalo:",h)
        h = h // 2
        #drecrementa o h
 
 
inp = [6, 3, 2, 1, 4, 7, 5, 8]
n = len(inp)
print('Array antes do Sorting:')
print(inp)
shell_sort(inp, n)
print('Array depois do Sorting:')
print(inp)

'''
função shell_sort():

Esta função recebe uma lista e seu tamanho como parâmetros
O intervalo ' h' é inicializado com metade do tamanho da lista
Agora, siga os passos abaixo até que o valor de h se torne menor que zero
Iterar o formulário de lista h até o final
Armazene cada elemento em uma variável temporária
Compare os elementos que estão em um intervalo de h e troque se necessário
Finalmente, o valor de h é atualizado e o processo continua até que a lista esteja completamente ordenada
'''