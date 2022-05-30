nota1 = int(input('Digite a primeira nota:'))
nota2 = int(input('Digite a segunda nota:'))
media = (nota1 + nota2)/2
print('Sua média obtida foi: {} '.format(media))
if media >= 6.0 :
    print ('Aprovado.')
else:
    print('Reprovado.')