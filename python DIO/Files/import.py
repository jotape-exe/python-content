from TV import Tv
from cont import cont_letras

if __name__ == '__main__':
    lista = ['Cabeça', 'de', 'Lampada', 'kkkkkkkkkkkk']
    print(cont_letras(lista))
    television = Tv()
    print('TV LIGADA: ',television.ligada)
    television.power()
    print('TV LIGADA: ',television.ligada)