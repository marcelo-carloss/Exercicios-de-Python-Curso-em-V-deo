import random
from time import sleep
num = int(input('Vamos brincar de adivinhar? O computador irá gerar um número aleatório entre 0 e 5, e você terá que que adivinha. Qual número você pensou?: '))
sorteio = random.randint(0,5)
print('LOADING...')
sleep(2)
if num == sorteio:
  print('PARABÉNS VOCÊ ACERTOU!!!!')
else:
  print('Que pena, você errou! Eu pensei no número {} e não no {}'.format(sorteio,num))