totalGasto = maisDeMil = menorValor = maiorValor = cont = 0
maisBarato = maisCaro = ''
while True:
  nomeProduto = str(input('Qual nome do produto? '))
  preçoProduto = float(input('Qual o preço do produto? R$'))
  cont += 1
  totalGasto += preçoProduto
  if preçoProduto > 1000:
    maisDeMil += 1
  if cont == 1:
    menorValor = maiorValor = preçoProduto
    maisBarato = maisCaro = nomeProduto
  else:
    if preçoProduto < menorValor:
      menorValor = preçoProduto
      maisBarato = nomeProduto
    if preçoProduto > maiorValor:
      maiorValor = preçoProduto
      maisCaro = nomeProduto
  continuar = ' '
  while continuar not in 'SN':
    continuar = str(input('Quer continuar? [S/N]: ')).strip()[0].upper()
  if continuar == 'S':
    print('Ok, insira o próximo produto.')
  elif continuar == 'N':
    break
print('PROGRAMA ENCERRADO!')
print(f'O valor total da sua compra foi de {totalGasto:.2f}')
print(f'Foram {maisDeMil} produtos que custaram mais de R$1000.')
print(f'O produtos mais barato foi o {maisBarato} e custou R${menorValor:.2f}')
print(f'O produto mais caro foi {maisCaro} e ele custou R${maiorValor:.2f}')