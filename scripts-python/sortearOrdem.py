from random import shuffle

aluno1 = str(input('Digite o nome do primeiro aluno'))
aluno2 = str(input('Digite o nome do segundo aluno'))
aluno3 = str(input('Digite o nome do terceiro aluno'))
aluno4 = str(input('Digite o nome do quarto aluno'))

alunos = [aluno1, aluno2, aluno3, aluno4]

shuffle(alunos)

print('Ordem de apresentação: {}'.format(alunos))