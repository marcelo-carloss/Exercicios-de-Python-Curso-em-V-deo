print('Seja bem vindo ao mercadinho MarShop')
valor = float(input('Digite o valor do produto: R$'))
escolha = int(input('Digite a opção de pagamento desejada: \n 1- À vista no dinheiro/cheque (desconto de 10%) \n 2- À vista no cartão (desconto de 5%) \n 3- Em até 2x no cartão (preço sem juros) \n 4- 3x ou mais no cartão (juros de 20%) \n\n Qual será a forma de pagamento? : '))

if escolha == 1:
  total = valor - (0.10 * valor)
  print('Muito bem, você ganhou um desconto de 10%, seu produto de R${}, ficará no valor de R${}!'.format(valor, total))
elif escolha == 2:
  total = valor - (0.05 * valor)
  print('Muito bem, você ganhou um desconto de 5%, seu produto de R${}, ficará no valor de R${}!'.format(valor, total))
elif escolha == 3:
  total = valor / 2
  print('Muito bem, seu produto de R${}, ficará 2x de R${}!'.format(valor, total))
elif escolha == 4:
  total = valor + (0.20 * valor)
  totparc = int(input('Quantas parcelas? '))
  parcela = total / totparc
  print('Divido em {}x o seu produto tem um juros de 20%, seu produto de {} ficará no valor de {}'.format(totparc, valor, total))
else:
  print('Opção inválida, tente novamente.')
