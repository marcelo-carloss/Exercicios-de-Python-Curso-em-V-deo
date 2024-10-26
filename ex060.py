fatorial = int(input('Digite um número para descobrir o seu fatorial: '))
resultado = 1
mult = 1
while fatorial >= mult:
  resultado *= mult
  mult += 1
print('O {}! é: {}'.format(fatorial, resultado))
