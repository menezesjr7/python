ano = int(input('Digite o ano:'))

stringAno = str(ano)
stringDigitosFinais = stringAno[2] + stringAno[3]
digitosFinais = int(stringDigitosFinais)

moduloAno = ano % 4
moduloAno00 = ano % 400

if digitosFinais != 0 and moduloAno == 0 :
    print('{} é um ano bissexto.'.format(ano))
elif digitosFinais == 0 and moduloAno00 == 0:
    print('{} é um ano bissexto.'.format(ano))
else:
    print('{} não é um ano bissexto.'.format(ano))