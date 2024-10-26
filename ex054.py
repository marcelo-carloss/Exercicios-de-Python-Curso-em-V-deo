from datetime import date
atual = date.today().year
maioridade = []
menoridade = []
for i in range(0, 7):
  idade = int(input('Digite seu ano de nascimento: '))
  if atual - idade >= 21:
    maioridade.append(idade)
  else:
    menoridade.append(idade)
print('São {} que são maior de idade e {} que são menor de idade!'.format(len(maioridade), len(menoridade)))
