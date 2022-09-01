def espaço():
    print(30*'-')

aluno_qtd = int(input('QUANTOS ALUNOS SUA TURMA TEM? '))
espaço()
medias = []
x = 1
while x <= aluno_qtd:
    med = float(input('MÉDIA DO {}º ALUNO: '.format(x)))
    espaço()
    x += 1
    medias.append(med)
print('MÉDIA GERAL:',sum(medias)/aluno_qtd)
espaço()
print('MAIOR MÉDIA: ',max(medias))
espaço()
print('MENOR MÉDIA: ',min(medias))