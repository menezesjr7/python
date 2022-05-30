from random import shuffle

candidato1 = str('Bolsonaro')
candidato2 = str('Ciro')
candidato3 = str('Lula')

candidatos = [candidato1, candidato2, candidato3]

shuffle(candidatos)

print('Ordem de apresentação: {}'.format(candidatos))