def ficha(nome='<desconhecido>', gols=0):
  print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

n = str(input('Nome do Jogador: '))
gol = str(input('Número de Gols: '))
if gol.isnumeric():
  gol = int(gol)
else:
  gol = 0
if n.strip() == '':
  ficha(gols=gol)
else:
  ficha(n, gol)


