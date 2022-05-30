largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
print('A parede possui as dimensões de {} mts x {} mts, possuindo uma área de {} mts².\n Serão necessários {} litros de tinta para pintá-la.'.format(largura, altura, area, (area/2)))
