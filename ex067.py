print('-' * 50)
print('PROGRAMA DE TABUADA!')
print('-' * 50)
while True:
  n = int(input('Qual tabuada você deseja ver? '))
  print('-' * 50)
  cont = 0
  if n > 0:
    while cont <= 10:
      print(f'{n} * {cont} = {n * cont}')
      cont += 1
  else:
    break
print('PROGRAMA DE TABUADA ENCERRADO!')
print('-' * 50)