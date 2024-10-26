from random import randint
computador = randint(0, 10)
tentivas = 0
print('\nTente adivinha no número que pensei entre 1 e 10! \n')
acertou = False
while not acertou:
  jogador = int(input('Qual número você pensou? '))
  if jogador == computador:
    acertou = True
  if jogador > computador:
    print('É MENOS. Tente de novo')
  elif jogador < computador:
    print('É MAIS. Tente de novo')
  tentivas += 1
print('Você acertou, o número que eu pensei foi {}, você precisou de {} chances.'.format(computador, tentivas))