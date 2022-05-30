lado1 = int(input('Digite o tamanho do primeiro lado:'))
lado2 = int (input('Agora digite o tamanho do segundo lado:'))
lado3 = int (input('E por fim, digite o tamanhho do terceiro lado:'))

if lado1 >= lado2 and lado1 >= lado3 :
    maior = lado1
    somaDosMenores = lado2 + lado3
elif lado2 >= lado1 and lado2 >= lado3 :
    maior = lado2
    somaDosMenores = lado1 + lado3
elif lado3 >= lado1 and lado3 >= lado2 :
    maior = lado3
    somaDosMenores = lado1 + lado2
else:
    print('Não é possível identificar o maior lado.')

if somaDosMenores == maior :
    print('Não é possivel formar um triângulo com essas retas.')
else:
    print('É possivel formar um triângulo com essas retas.')