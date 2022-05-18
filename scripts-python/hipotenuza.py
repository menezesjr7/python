import math
catOposto = float(input('Digite o comprimento do cateto oposto:'))
catAdjascente = float(input('Digite o comprimento do cateto adjascnte:'))
print('O comprimento da hipotenuza é de {}'.format(math.hypot(catAdjascente, catOposto)))