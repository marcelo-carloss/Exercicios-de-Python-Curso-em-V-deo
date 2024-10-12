cores = {'amarelo':'\033[33m',
         'azul':'\033[34m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'limpa':'\033[m'}

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
  print('{}SIM, esses segmentos formam um triângulo{}'.format(cores['verde'], cores['limpa']))
else:
  print('{}NÃO, esses segmentos não formam um triângulo.{}'.format(cores['vermelho'],cores['limpa']))