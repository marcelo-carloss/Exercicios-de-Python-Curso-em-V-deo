numeros = []
cont = 0
while True:
  num = int(input('Digite um número: '))
  numeros.append(num)
  cont += 1
  continuar = ' '
  while continuar not in 'SN':
    continuar = str(input('Deseja continuar? [S/N]: ')).upper().split()[0]
  if continuar == 'N':
    break
print(f'A quantidade de números digitados foi: {cont}')
print(f'A lista de valores, ordenados de forma decrescente: {sorted(numeros)[::-1]}')
print(f'Sim, o valor 5 foi digitado' if numeros.count(5) else 'Numero 5 não encontrado!')