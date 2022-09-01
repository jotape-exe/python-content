def cont_letras(lista_palavras):
    contador = []
    for x in lista_palavras:
        qtd = len(x)
        contador.append(qtd)
    return contador

if __name__ == '__main__':
    lista = ['Cabeça', 'de', 'Lampada']
    print(cont_letras(lista))