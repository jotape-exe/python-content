class Paciente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

fila = []

p1 = Paciente('Pedro', '18')
p2 = Paciente('Maria', '20')
p3 = Paciente('Marcos', '22')
p4 = Paciente('Ana', '29')

fila.append(p1)
fila.append(p2)
fila.append(p3)
fila.append(p4)

print('        Pacientes')
print('-------------------------')

for x in fila:
    print('Nome: {}, Idade: {}'.format(x.nome, x.idade))
    print('-------------------------')