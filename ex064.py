n = int(input('Digite um número: '))
s = 0
cont = 0
while n != 999:
  s += n
  cont += 1
  print('Deseja continuar?')
  n = int(input('Se sim, digite outro número, se não, digite 999: '))
print('A soma de todos os números é: {} e foram {} números digitados'.format(s, cont))