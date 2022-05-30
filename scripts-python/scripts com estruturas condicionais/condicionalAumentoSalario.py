salarioAtual = int(input('Digite o salário atual:'))

if salarioAtual > 1250 :
    aumento = 0.10
else:
    aumento = 0.15

salarioNovo = salarioAtual + (salarioAtual * aumento)

print('O salário atual de R$ {}, sofrerá um aumento de {}%, equivalente a R$ {}, e passará a ser de R$ {}.'.format(salarioAtual, (aumento*100), (salarioAtual * aumento), salarioNovo ))