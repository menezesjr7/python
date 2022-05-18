reais = float(input('Quantos reais você tem na carteira? R$ '))
print('Com R$ {:.2f} você consegue comprar U$ {:.2f} dólares ou E$ {:.2f}.'.format(reais, (reais/5.14),(reais/5.33)))