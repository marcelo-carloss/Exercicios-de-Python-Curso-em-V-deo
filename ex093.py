jogador = {}
gols = list()
jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
for g in range(0,partidas):
  gols.append(int(input(f'  Quantos gols ele marcou na partida {g + 1}? ')))
jogador['gols'] = gols
jogador['total'] = sum(gols)
print('=-' * 30)
print(f'Nome do Jogador: {jogador["nome"]}')
print(f'Gols nas Partidas: {jogador["gols"]}')
print(f'Total de Gols: {jogador["total"]}')
print('=-' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for p, g in enumerate(jogador['gols']):
  print(f'{'=>':>4} Na partida {p + 1}, fez {g} gols.')
