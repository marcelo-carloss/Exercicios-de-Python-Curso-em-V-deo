num = int(input('Digite um número de 0 a 9999:   '))

if num >= 0 and num < 10000:
  num_str = str(num)
  print('unidade: {}\n  dezena: {} \n  centena: {} \n  milhar: {}' .format(num_str[0], num_str[1], num_str[2], num_str[3] ))