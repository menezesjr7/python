numero = int(input('Digite um número:'))
resultado = numero % 2
if resultado == 0 :
    print('{} é um número par.'.format(numero))
else:
    print('{} é um número ímpar'.format(numero))