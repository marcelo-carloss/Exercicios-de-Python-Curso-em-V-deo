numeros = list()
numPares = list()
numImpares = list()
for n in range(1,8):
  numeros.append(int(input(f'Digite o {n}° valor: ')))
for n in numeros:
  if n % 2 == 0:
    numPares.append(n)
  else:
    numImpares.append(n)
print(f'Todos os valores digitados: {sorted(numeros)}')
print(f'Valores pares digitados: {sorted(numPares)}')
print(f'Valores ímpares digitados: {sorted(numImpares)}') 