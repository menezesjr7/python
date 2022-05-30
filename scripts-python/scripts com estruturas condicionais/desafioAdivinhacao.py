from random import randint
from time import sleep

computador = randint(0,5)

print ('-=-' * 13)
print ('VOU PENSAR EM UM NÚMERO ENTRE 0 E 5 !')
print ('-=-' * 13)
print('Pensando...')
sleep(2)
print ('-=-' * 13)

jogador = int(input('Em que número eu pensei?'))
print ('-=-' * 13)

if jogador == computador :
    print('Você acertou!')
else:
    print('Eu escolhi {}, não {}'.format(computador, jogador))