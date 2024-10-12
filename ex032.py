from datetime import date
ano = int(input('Digite um ano para sabermos se ele é um ano bissexto: '))
if ano == 0:
  ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
  print('Sim, o ano de {}, é um ano bissexto'.format(ano))
else:
  print('Não, o ano de {}, não é um ano bissexto'.format(ano))