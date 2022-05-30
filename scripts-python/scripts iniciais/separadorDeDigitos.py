numero = input('Digite um número entre 0 e 9999:')
numero = numero.strip()
qtdCasas = len(numero)

if (int(numero) < 0 or int(numero) > 9999):
    print('Número inválido.')
    qtdCasas = 0

if (qtdCasas == 1):
    print('Unidade:',numero[0])

if (qtdCasas == 2):
    print('Unidade:', numero[1],
          '\n Dezena:',numero[0])

if (qtdCasas == 3):
    print('Unidade:', numero[2],
          '\n Dezena:', numero[1],
          '\nCentena:', numero[0])

if (qtdCasas == 4):
    print('Unidade:', numero[3],
          '\n Dezena:', numero[2],
          '\n Centena:', numero[1],
          '\n Milhar:',numero[0])