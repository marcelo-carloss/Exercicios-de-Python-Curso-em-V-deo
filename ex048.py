s = 0
cont = 0
for num in range(1, 501, 2):
  if num % 3 == 0:
   cont += 1
   s += num
print('A soma de todos números ímpares entre 1 e 500, e que são multiplos de 3, é: {}, a quantidade de números somados foram: {}'.format(s,cont))