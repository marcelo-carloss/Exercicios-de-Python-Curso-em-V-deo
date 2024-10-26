num = int(input('Digite um número inteiro: '))
escolha = int(input('Agora escolha qual será a base de conversão: \n Digite o número da sua escolha \n 1- Binário \n 2- Octal \n 3- Hexadecimal \n '))
if escolha == 1:
  print('O número {} em base Binária é: {}'.format(num, bin(num)[2:]))
elif escolha == 2:
  print('O número {} em base Octal é: {}'.format(num, oct(num)[2:]))
elif escolha == 3:
  print('O número {} em base Hexadecimal é: {}'.format(num, hex(num)[2:]))
else:
  print('Essa opção não existe!')