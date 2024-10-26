print('Muito bem-vindo ao Marcelo Bank, hoje iremos fazer o seu empréstimo imobiliário')
valor = float(input('Qual é o valor do imóvel? R$'))
prazo_ano = float(input('Em quantos anos você deseja pagar esse imóvel? '))
salario = float(input('Qual é o valor do seu salário? R$'))

prazo_mes = prazo_ano * 12
parcela = valor / prazo_mes

if parcela <= 0.30 * salario:
  print('Parabéns, seu empréstimo no valor de R${} foi aprovado! Você terá uma parcela de R${:.2f} por mês, seu prazo será de {:.0f} meses'.format(valor, parcela, prazo_mes))
else:
  print('Infelizmente seu empréstimo foi reprovado, as parcelas ficaram no valor de R${:.2f} e excederam 30 por cento do seu salário'.format(parcela))