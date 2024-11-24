numeros = []
while True:
  num = int(input('Digite um valor: '))
  numeros.append(num)
  continuar = ' '
  while continuar not in 'SN':
    continuar = str(input('Deseja continuar? [S/N]: ')).upper().split()[0]
  if continuar == 'N':
    break
numPar = []
numImpar = []
for i in numeros:
  if i % 2 == 0:
    numPar.append(i)
  else:
    numImpar.append(i)
print(f'A lista completa com todos os valores: {sorted(numeros)}')
print(f'Lista com os números pares: {sorted(numPar)}')
print(f'Lista com os números impares: {numImpar}')