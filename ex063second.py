a = 0
b = 1
count = 1
n = int(input('Digite um numero: '))

while count <= n:
  print('{} →'.format(a), end=" ")
  prox = a + b
  a = b
  b = prox
  count += 1
print('FIM')