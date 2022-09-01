#from cont import cont_letras


cont_letras = lambda lista: [len(x) for x in lista]
#função anomima, mais simples e limpo

lista_doido = ['MALUCO', 'DOIDO', 'DE PEDRA']
print(cont_letras(lista_doido))