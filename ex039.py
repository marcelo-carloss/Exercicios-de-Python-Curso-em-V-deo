from datetime import date

ano_nas = int(input('Digite o ano em que você nasceu: '))
ano_atual = date.today().year
idade = ano_atual - ano_nas

if idade == 18:
  print('Você está com a idade certa para se alistar, procure se regularizar!')
elif idade < 18:
  tempo_falta = 18 - idade
  if tempo_falta == 1:
    print('Você ainda não tem idade para se alistar, falta {} ano!'.format(tempo_falta))
  else:
    print('Você ainda não tem idade para se alistar, faltam {} anos!'.format(tempo_falta))
else:
  tempo_passou = idade - 18
  if tempo_passou == 1:
    print('Você ja passou da idade de se alistar, ja se passou {} ano!'.format(tempo_passou))
  else:
    print('Você ja passou da idade de se alistar, ja se passaram {} anos!'.format(tempo_passou))