velocidade = int(input('Digite a velocidade do veículo:'))

if velocidade > 80 :
    print("Você foi multado!")
    multa = (velocidade - 80)*7
    print('Valor da multa: R$ {}'.format(multa))
else:
    print('Velocidade permitida no trecho.')