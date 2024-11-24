lista = []
for num in range(0, 5):
  lista.append(int(input(f'Digite um número na posição {num}: ')))
print(f'Os números digitados foram: {lista}')
print(f'O maior valor na lista é {max(lista)} nas posições: ', end=' ')
for i, v in enumerate(lista):
  if v == max(lista):
    print(f'{i}...', end=' ')
print()
print(f'O menor valor na lista é {min(lista)} nas posições: ', end=' ')
for i, v in enumerate(lista):
  if v == min(lista):
    print(f'{i}...', end=' ')
print()