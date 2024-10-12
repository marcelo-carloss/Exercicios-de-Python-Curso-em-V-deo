vel = int(input('Qual a sua velocidade? '))
if vel > 80:
  multa = (vel - 80) * 7
  print('Você ultrapassou o limte de 80km/h e foi multado em: {} reais'.format(multa))
print('Bom dia, tome cuidado durante a viagem e não ultrapasse os limites de velocidade!')