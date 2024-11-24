import random
from time import sleep
jogos = list()

nPalpites = int(input('Quantos palpites você deseja? '))
print('=-' * 40 )
print(f'Esses são os meus {nPalpites} palpites.')
print('=-' * 40 )

for p in range(0, nPalpites):
  jogos.append(random.sample(range(1,60), k=6))
  sleep(1)
  jogos.sort()
  print(f'Palpite número {p + 1}: {jogos[p]}')
