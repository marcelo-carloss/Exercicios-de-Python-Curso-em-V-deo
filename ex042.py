r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1+ r2:
  print('SIM, esses segmentos formam um triângulo')
  if r1 == r2 == r3:
    print('Esse triângulo tem todos os lados iguais, portanto será EQUILÁTERO!')
  elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
    print('Esse triângulo tem dois lados iguais, portanto será ISÓSCELES!')
  else:
    print('Esse triângulo tem todos os lados diferentes, portanto será ESCALENO!')
else:
  print('NÃO, esses segmentos não formam um triângulo!') 