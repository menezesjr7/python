distancia = int(input('Digite a distância em km da sua viagem:'))

if distancia <= 200:
    taxa = 0.50
else:
    taxa = 0.45

precoViagem = distancia * taxa

print('A viagem de {} km, terá uma taxa de R${} por km rodado, perfazendo um total de R$ {} de custo.'.format(distancia, taxa, precoViagem))