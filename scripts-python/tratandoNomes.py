nome = (input('Digite seu nome completo:'))
print(nome.upper())
print(nome.lower())
nomeSemEspaco = nome.replace(' ','')
print(len(nomeSemEspaco))
primeiroNome = nome.split()
print(len(primeiroNome[0]))