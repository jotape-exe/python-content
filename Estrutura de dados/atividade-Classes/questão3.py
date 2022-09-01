class Medico:
    def __init__(self, nome, crm):
        self.nome = nome
        self.crm = crm

fila = ['José - Professor', 'Daniel - Policial', 'Jenifer - Dentista', 'Alex - Juiz',
        'Marcos- Professor', 'jonas - Policial', 'Marina - Dentista', 'Roberto - Juiz']
med = []

m1 = Medico('Mathias', 123876)
m2 = Medico('Ana', 634987)
m3 = Medico('Joao', 5298745)

med.append(m1)
med.append(m2)
med.append(m3)

print('     MÉDICOS')
print('------------------')
for i in med:
    print(i.nome,'/crm:',i.crm)

print('------------------')
print('       FILA')
print('------------------')

x = 0
for a in med:
    fila.insert(x, m1.nome)
    x += 2
for a in med:
    fila.insert(x, m2.nome)
    x += 2
for a in med:
    fila.insert(x, m3.nome)
    x += 2
for x in range(0, len(fila)):
    print(fila[x])