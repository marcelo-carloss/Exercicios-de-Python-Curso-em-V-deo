aproveitamento = list()
jogador = {}
gols = list()
while True:
  total = 0
  jogador['nome'] = str(input('Nome do Jogador: '))
  partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
  for g in range(0,partidas):
    gols.append(int(input(f'Qunatos gols ele marcou na partida {g}? ')))
  jogador['gols'] = gols[:]
  jogador['total'] = sum(gols)
  aproveitamento.append(jogador.copy())
  jogador.clear()
  gols.clear()
  r = str(input('Quer continuar? [S/N] '))
  if r in 'Nn':
    break
print('=-' * 30)
print(f'{'Cod'}{'Nome':>5}{'Gols':>15}{'Total':>25}')
print('-' * 50)
cont = 0
for j in aproveitamento:
  print(f'{cont}{j["nome"]:>10}        {j["gols"]}{j["total"]:>25}')
  cont += 1
while True:
  cont = 0
  ver = int(input('Deseja ver as estatisticas de qual jogador? '))
  if ver < len(aproveitamento):
    print(f' -- Levantamento do Jogador: {aproveitamento[ver]["nome"]}')
    for i in aproveitamento[ver]["gols"]:
      print(f'   No jogo {cont} ele fez {i} gols.')
      cont += 1
  elif ver >= len(aproveitamento) and ver < 999:
    print('Jogador não existe!')
  else:
    break
print('Programa encerrado')