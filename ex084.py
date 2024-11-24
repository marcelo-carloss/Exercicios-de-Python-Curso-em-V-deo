pessoas = list()
dados = list()
leves = pesada = 0
r = ' '
while r not in 'Nn':
  dados.append(str(input('Nome: ')))
  dados.append(int(input('Peso: ')))
  pessoas.append(dados[:])
  dados.clear()
  
  r = str(input('Quer continuar? [S/N]: '))   
  if len(pessoas) == 1:
    leves = pessoas[0]
    pesada = pessoas[0]
  else:
    for c in pessoas:
      if c[1] > pesada[1]:
        pesada = c
      if c[1] < leves[1]:
        leves = c 
print(f'Pessoa cadastradas: {len(pessoas)}')
print(f'Pessoas mais pesadas com {pesada[1]}kg, foram: ', end=' ')
for n, p in pessoas:
  if p == pesada[1]:
    print(f'{n}', end=',')
print()
print(f'Pessoas mais leves com {leves[1]}kg, foram: ', end=' ')
for n, p in pessoas:
  if p == leves[1]:
    print(f'{n}', end=',')
print()