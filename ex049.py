print('Vamos fazer a tabuada?')
t = int(input('Você quer a tabuada do: '))

for n in range(0, 11):
  print('{} x {} = {}'.format(t, n, t * n))