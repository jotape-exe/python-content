class Paciente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
#Cria os atributos de "nome" e "idade"

fila = []
#Fila para armazenar os pacientes

p1 = Paciente('Pedro', 35)
p2 = Paciente('Maria', 20)
p3 = Paciente('Marcos', 25)
p4 = Paciente('Ana', 29)
p5 = Paciente('José', 70)
p6 = Paciente('Mariana', 65)
p7 = Paciente('Sandra', 61)
p8 = Paciente('Marcelo', 71)
p9 = Paciente('Jonas', 60)
#Adiciona valores aos atributos (nome, idade)

fila.append(p1)
fila.append(p2)
fila.append(p3)
fila.append(p4)
fila.append(p5)
fila.append(p6)
fila.append(p7)
fila.append(p8)
fila.append(p9)
#Adiciona os pacientes na fila

print('   Pacientes acima de 60 anos')
print('--------------------------------')

for x in fila:
    if x.idade >= 60:
#Só printa nome e idade dos Pacientes se tiverem 60 ou mais anos
        print('Nome: {}, Idade: {}'.format(x.nome, x.idade))
        print('--------------------------------')