'''
num = int(input('Digite um número: '))
is_primo = True

if num < 2:
  is_primo = False
elif num == 2:
  is_primo = True
elif num % 2 == 0:
  is_primo = False
else:
  for i in range(3, int(num ** 0.5) +1 , 2):
    if num % i == 0:
      is_primo = False
      break
if is_primo:
  print('O número {} é um número primo'.format(num))
else:
  print('O número {} NÃO é um número primo'.format(num))
  '''

# a forma acima foi como eu fiz, com ajuda de pesquisa. 

# a foma abaixo é como foi feito na aula, e é uma forma mais simples.

num = int(input('Digite um número: '))
cont = 0
for i in range(1, num + 1):
  if num % i == 0:
    cont += 1
if cont == 2:
  print('{} é um número PRIMO, pois ele é divisivel apenas por 1 e por ele mesmo.'.format(num))
else:
  print('{} NÃO é PRIMO, pois tem {} divisores'.format(num, cont))