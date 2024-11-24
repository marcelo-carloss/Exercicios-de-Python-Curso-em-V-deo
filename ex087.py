matriz = list()
line1 = list()
line2 = list()
line3 = list()
somaPares = somaTerCol = maior = 0 
for i in range(0,3):
  line1.append(int(input(f'Digite o valor na posição [0,{i}]: ')))
matriz.append(line1[:])
for i in range(0,3):
  line2.append(int(input(f'Digite um valor na posição [1,{i}]: ')))
matriz.append(line2[:])
for i in range(0,3):
  line3.append(int(input(f'Digite um valor na posição: [2,{i}]: ')))
matriz.append(line3[:])
print('=-' * 40)
for line in matriz:
  for n in line:
    print(n, end=' ')
  print()
print('=-' * 40)

for line in matriz:
  for n in line:
    if n % 2 == 0:
      somaPares += n
      
for line in matriz:
  somaTerCol += line[2]

for n in matriz[1]:
  if n > maior:
    maior = n 
    
print('=-' * 40)
print(f'A soma dos valores pares é {somaPares}')
print(f'A soma dos valores da terceira coluna é {somaTerCol}')
print(f'O maior valor da segunda linha é {maior}')