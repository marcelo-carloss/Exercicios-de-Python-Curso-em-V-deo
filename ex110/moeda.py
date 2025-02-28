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
  """
  -> Essa função faz um resumo mostrando as outras funções (dobro, metade, aumentar e diminuir) através dela.
  :param preco: valor de preço passado pelo usuário.
  :param aumento: valor de porcetagem de aumento, esse valor será usado na função aumentar() e será passado como parametro real de porcentagem.
  :param reducao:  valor de porcetagem de diminuição, esse valor será usado na função diminuir() e será passado como parametro real de porcentagem.
  """
  print('-' * 30)
  print(f'RESUMO DO VALOR'.center(30))
  print('-' * 30)
  print(f'Preço analisado: \t{moeda(preco)}')
  print(f'Dobro do preço: \t{dobro(preco,True)}')
  print(f'Metade do preço: \t{metade(preco)}')
  print(f'{aumento}% de aumento: \t{aumentar(preco, aumento,True)}')
  print(f'{reducao}% de redução: \t{diminuir(preco, reducao,True)}')
  print('-' * 30)
