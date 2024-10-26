cont = soma = 0
while True:
  n = int(input('Digite um número [999 PARA ENCERRAR]: '))
  if n == 999:
    break
  cont += 1
  soma += n
print('-' * 30)
print('PROGRAMA ENCERRADO!')
print('-' * 30)
print(f'Você digitou {cont} números, e a soma deles deu {soma}')