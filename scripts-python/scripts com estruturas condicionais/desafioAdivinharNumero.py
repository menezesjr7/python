from random import choice

lista = [0, 1, 2, 3, 4, 5]

print('O computador pensou em um número de 0 a 5.')

chute = int(input('Que número você acha que foi escolhido?'))

numero = choice(lista)

if numero == chute :
    print('Você acertou! O numero escolhido realmente era {}'.format(numero))
else:
    print('Você errou! O numéro escolhido foi {}'.format(numero))
