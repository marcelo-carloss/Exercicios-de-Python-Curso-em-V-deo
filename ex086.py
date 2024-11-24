matriz = list()
line1 = list()
line2 = list()
line3 = list()
 
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
