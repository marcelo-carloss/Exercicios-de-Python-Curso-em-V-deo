soma = 0
for num in range(1, 7):
 s = int(input('Digite um numero: '))
 if s % 2 == 0:
  soma += s
print('A soma dos números pares que você digitou é: {}'.format(soma))