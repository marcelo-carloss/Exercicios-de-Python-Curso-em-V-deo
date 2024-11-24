numeros = []
while len(numeros) < 5:
  num = int(input('Digite um valor: '))
  if len(numeros) == 0:
    numeros.append(num)
    print('Numero adicionado no final...')
  else:
    inserido = False
    for i in range(len(numeros)):
      if num < numeros[i]:
        numeros.insert(i, num)
        print(f"Numero {num} adicionado na posição {i}")
        inserido = True
        break
    if not inserido:
      numeros.append(num)
      print('Numero adicionado no final....')
print(f'Os valores adicionados em ordem foram {numeros}')