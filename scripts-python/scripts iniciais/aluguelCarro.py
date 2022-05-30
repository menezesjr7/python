kmPercorridos = float(input('Digite a quantidade de KM percorridos:'))
diasAlugado = int(input('Digite a quantidade de dias que o carro ficou alugado:'))

precoKm = kmPercorridos * 0.15
precoDias = diasAlugado * 60

precoFinal = precoKm + precoDias

print('Com {}km rodados, em {} dias de aluguel, você deverá pagar R$ {}'.format(kmPercorridos, diasAlugado, precoFinal))