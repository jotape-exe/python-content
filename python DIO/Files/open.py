def escrever (texto):
    archive = open('teste.txt', 'w')
    archive.write(texto)
    archive.close()

def atualizar (name_arch, texto):
    archive = open(name_arch, 'a')
    archive.write(texto)
    archive.close()

def ler_archive (name_arch):
    archive = open(name_arch, 'r')
    texto = archive.read()
    print(texto)

def media (name_arch):
    archive = open(name_arch, 'r')
    aluno_nota = archive.read()
    print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')

for x in aluno_nota:
    print(x)

if __name__ == '__main__':
    media('notas.txt')
    aluno = '\noiiii\n'
    escrever('Primeira Linha\n')
    atualizar('notas.txt',aluno)
    ler_archive("teste.txt")



'''
archive = open('teste.txt', 'a')
for i in range(0, 200):
    print(archive.write('\nlinha - {}'.format(i)))
'''