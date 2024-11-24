from random import randint
from time import sleep
sorteio = {}
for i in range(0,3):
  sorteio['jogador1'] = randint(1,6)
  sorteio['jogador2'] = randint(1,6)
  sorteio['jogador3'] = randint(1,6)
  sorteio['jogador4'] = randint(1,6)
print('Valores sorteados:')
for j , n in sorteio.items():
  print(f'{'':>1} O {j} tirou {n}')
print('Ranking dos jogadores:')
cont = 1
for i in sorted(sorteio, key = sorteio.get, reverse=True):
  print(f'{cont:>3}° lugar: {i} com {sorteio[i]}')
  cont += 1