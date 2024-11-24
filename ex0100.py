from random import randint
numeros = list()

def sorteia():
  print('Sorteando 5 valores da lista: ', end='')
  for i in range(0, 5):
    numeros.append(randint(1,10))
    print(numeros[i],end=' ')
  print('PRONTO!')

def somarPar(lst):
  s = 0
  for i in lst:
    if i % 2 == 0:
      s += i
  print(f'Somando os valores pares de {lst}, temos {s}')
    
sorteia()
somarPar(numeros)