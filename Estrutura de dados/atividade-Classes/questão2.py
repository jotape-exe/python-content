class Paciente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

fila = []

p1 = Paciente('Pedro', 35)
p2 = Paciente('Maria', 20)
p3 = Paciente('Marcos', 25)
p4 = Paciente('Ana', 29)
p5 = Paciente('José', 70)
p6 = Paciente('Mariana', 65)
p7 = Paciente('Sandra', 61)
p8 = Paciente('Marcelo', 71)
p9 = Paciente('Jonas', 60)

fila.append(p1)
fila.append(p2)
fila.append(p3)
fila.append(p4)
fila.append(p5)
fila.append(p6)
fila.append(p7)
fila.append(p8)
fila.append(p9)

print('   Pacientes acima de 60 anos')
print('--------------------------------')

for x in fila:
    if x.idade >= 60:
        print('Nome: {}, Idade: {}'.format(x.nome, x.idade))
        print('--------------------------------')