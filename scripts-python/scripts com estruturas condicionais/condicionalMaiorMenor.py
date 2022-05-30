numero1 = int(input('Digite o primeiro número:'))
numero2 = int (input('Agora digite o segundo número:'))
numero3 = int (input('E por fim, digite o terceiro número:'))

if numero1 >= numero2 and numero1 >= numero3 :
    maior = numero1
elif numero2 >= numero1 and numero2 >= numero3 :
    maior = numero2
elif numero3 >= numero1 and numero3 >= numero2 :
    maior = numero3
else:
    print('Não é possível identificar o maior número.')

print('{} é o maior número'.format(maior))

if numero1 <= numero2 and numero1 <= numero3 :
    menor = numero1
elif numero2 <= numero1 and numero2 <= numero3 :
    menor = numero2
elif numero3 <= numero1 and numero3 <= numero2 :
    menor = numero3
else:
    print('Não é possível identificar o menor número.')
print('{} é o menor número'.format(menor))