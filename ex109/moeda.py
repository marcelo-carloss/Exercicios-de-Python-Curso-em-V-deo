def metade(preco=0,format=False):
  """
  -> Essa função calcula a metade de um preço
  :param preco: valor de preço passado pelo usuário.
  :param format: valor booleano, opcional, caso o usuário queira o valor de preço formatado.
  """
  metade = preco / 2
  return metade if not format else moeda(metade)

#esse acima irei fazer igual a aula, os outros debaixo, foi eu mesmo.

def dobro(preco=0,format=False):
  """
  -> Essa função calcula o dobro de um preço
  :param preco: valor de preço passado pelo usuário.
  :param format: valor booleano, opcional, caso o usuário queira o valor de preço formatado.
  """
  dobro = preco * 2
  if format == True:
    return moeda(dobro)
  return dobro

def aumentar(preco=0, porcentagem=0,format=False):
  """
  -> Essa função calcula o aumento de um preço, a partir de uma porcentagem passada pelo usuário no parametro porcentagem
  :param preco: valor de preço passado pelo usuário.
  :param porcentagem: porcentagem de aumento sobre o valor
  :param format: valor booleano, opcional, caso o usuário queira o valor de preço formatado.
  """
  aumentar = preco + (preco * (porcentagem/100))
  if format == True:
    return moeda(aumentar)
  return aumentar

def diminuir(preco=0,porcetagem=0,format=False):
  """
  -> Essa função calcula uma diminuição de um preço, a partir de uma porcentagem passada pelo usuário no parametro porcentagem
  :param preco: valor de preço passado pelo usuário.
  :param porcentagem: porcentagem de diminuição sobre o valor
  :param format: valor booleano, opcional, caso o usuário queira o valor de preço formatado.
  """
  diminuir = preco - (preco * (porcetagem/100))
  if format == True:
    return moeda(diminuir)
  return diminuir

def moeda(preco=0, moeda='R$'):
  """
  -> Essa função formato os output das funções acima, adicionado o "R$" e colocando 2 números após a virgula, que também foi adicionada no lugar do ponto.
  """
  return f'{moeda}{preco:.2f}'.replace('.',',')