totalMinutos = int(input('Qual o total de minutos:'))
horas: int = totalMinutos//60
minutos: int = totalMinutos % 60
print('Você fez {} horas e {} minutos de estágio.'.format(horas,minutos))