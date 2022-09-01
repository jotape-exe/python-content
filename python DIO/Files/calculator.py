'''
class Calculadora:

    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2

    def soma(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def divis(self):
        return self.a / self.b

    def mult(self):
        return self.a * self.b

calculadora = Calculadora(12, 2)
print(calculadora.soma())
print(calculadora.sub())
print(calculadora.divis())
print(calculadora.mult())
'''
class Calculadora:

    def soma(self, a, b):
    #self muda a = a, b = b
        return a + b

    def sub(self, a, b):
        return a - b

    def divis(self, a, b):
        return a / b

    def mult(self, a, b):
        return a * b

calculadora = Calculadora()
#instanciei a classe 'Calculadora', como variável calculadora
print(calculadora.soma(12, 2))
print(calculadora.sub(12, 2))
print(calculadora.divis(12, 2))
print(calculadora.mult(12, 2))
#12 e 2 representam a e b, respectivamente

