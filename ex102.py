def fatorial(num, show=False):
  """
  -> Calcula o Fatorial de um número.
  :param num: O número a ser calculado.
  :param show: (opcional) Mostrar ou não a conta.
  :return: O valor do fatorial de um número n.
  """
  f = 1
  for c in range(num, 0, -1):
    if show == True:
      if c == 1:
        print(c, end=' = ')
      else:
        print(c, end=' x ')
    f *= c
  return f

print(fatorial(6))
help(fatorial)
