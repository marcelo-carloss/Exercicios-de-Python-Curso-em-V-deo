def metade(preco=0,format=True):
  metade = preco / 2
  if format == True:
    return moeda(metade)
  return metade

def dobro(preco=0,format=True):
  dobro = preco * 2
  if format == True:
    return moeda(dobro)
  return dobro

def aumentar(preco=0, porcentagem=0,format=True):
  aumentar = preco + (preco * (porcentagem/100))
  if format == True:
    return moeda(aumentar)
  return aumentar

def diminuir(preco=0,porcetagem=0,format=True):
  diminuir = preco - (preco * (porcetagem/100))
  if format == True:
    return moeda(diminuir)
  return diminuir

def moeda(preco=0, moeda='R$'):
  return f'{moeda}{preco:.2f}'.replace('.',',')

def resumo(preco=0, aumento=0, reducao=0):
  print('-' * 30)
  print(f'{'RESUMO DO VALOR':>10}')
  print('-' * 30)
  print(f'Preço analisado: {moeda(preco):>10}')
  print(f'Dobro do preço: {dobro(preco):>10}')
  print(f'Metade do preço: {metade(preco):>10}')
  print(f'{aumento}% de aumento: {aumentar(preco, aumento):>10}')
  print(f'{reducao}% de redução: {diminuir(preco, reducao):>10}')
  print('-' * 30)
