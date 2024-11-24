numeros = []
while True:
  continuar = ' '
  n =  int(input('Digite um valor: '))
  if n not in numeros:
    numeros.append(n)
    print('Valor adicionado com sucesso!')
  else:
    print('Valor duplicado, não vou adicionar!')
  while continuar not in 'SN':
    continuar = str(input('Quer continuar? [S/N]: ')).split()[0].upper()
  if continuar == 'N':
    break
print('-=' * 30)
print(f'Você digitou os valores {sorted(numeros)}')