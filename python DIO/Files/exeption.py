lista = [1, 10]
try:
    arquivo = open('teste.txt', 'r')
    texto = arquivo.read()
    divida = 10/0
    num = lista[1]
except ZeroDivisionError:
#Except para tratamneto de erros
    print('NÃO SE PODE DIVIDIR UM NÚMERO POR ZERO!')
except ArithmeticError:
    print('OCORREU UM ERRO ARITMETICO!')
except IndexError:
    print('INDICE DA LISTA INVÁLIDO!')
except Exception as ex:
    print('ERRO NO SITEMA:',ex)
else:
    print('PROGRAMA EXECUTADO COM SUCESSO!')
finally:
    print('PROGRAMA EXECUTADO COM ERROS!')
    arquivo.close()
    print('ARQUIVO FECHADO')