class Error(Exception):
    pass
class InputError(Error):
#Para criar uma classe personalizada você deve criar uma classe Exeption 1º
    def __init__(self, message):
        self.message = message
        
while True:
#Loop infinito até o requisito ser atendido
    try:
        x = int(input('DIGITE UM NÚMERO: '))
        print(x)
        if x > 10:
            raise InputError('ERRO: NUMERO MAIOR QUE 10!')
        elif x < 0:
            raise InputError('ERRO: NUMERO MENOR QUE 0!')
        break
    except ValueError:
        print('ERRO: Digite apenas números.')
#Retorna erro de valores: (int, float, str....)
    except InputError as ex:
        print(ex)
#retorna o erro de acordo com a entrada do usuário