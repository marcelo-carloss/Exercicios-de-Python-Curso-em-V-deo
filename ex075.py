num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))
num4 = int(input('Digite o último número: '))
numeros = (num1, num2, num3, num4)

if numeros.count(9) != 0:
  print(f'O número 9 apareceu {numeros.count(9)} vezes.')
else:
  print('O número 9 não foi digitado. ')
if numeros.count(3) != 0:
  print(f'A primeira vez que o número 3 aparece é na posição {numeros.index(3)}.')
else:
  print('Número 3 não foi inserido.')
print('Numeros pares: ', end=" ")
for n in numeros:
  if n % 2 == 0:
    print(f'{n}', end=" ")