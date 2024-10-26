from time import sleep

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
opção = 0
while opção != 5:
  print('\nEscolha o que deseja fazer com os dois números. \n [1] Somar \n [2] Multiplicar \n [3] Maior \n [4] Novos números \n [5] Sair do programa \n')
  opção = int(input('Digite uma opção '))
  print('Processando...')
  sleep(1)
  if opção >= 6:
    print('Opção inválida! \n')
    sleep(1)
  else:
    if opção == 1:
      soma = n1 + n2
      print('{} + {} = {} \n'.format(n1, n2, soma))
      sleep(1)
    elif opção == 2:
      produto = n1 * n2
      print('{} * {} = {} \n'.format(n1, n2, produto))
      sleep(1)
    elif opção == 3:
      if n1 > n2:
        print('{} é maior que {} \n'.format(n1, n2))
        sleep(1)
      else:
        print('{} é maior que {} \n'.format(n2, n1))
        sleep(1)
    elif opção == 4:
      n1 = float(input('Digite o primeiro número: '))
      n2 = float(input('Digite o segundo número: '))
      sleep(1)
print('Programa finalizado.')