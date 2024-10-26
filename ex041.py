from datetime import date

ano_nas = int(input('Digite seu ano de nascimento: '))
print('Agora baseado na sua idade, iremos ver qual a sua categoria.')
ano_atual = date.today().year
idade = ano_atual - ano_nas

if idade <= 9:
  print('Sua idade é {} anos, e sua categoria é MIRIM'.format(idade))
elif idade > 9 and idade <= 14: #Eu tinha feito todas as condições dessa forma colocando as duas métricas, mudei após o video de exercicio.
  print('Sua idade é {} anos, e sua categoria é INFANTIL'.format(idade))
elif idade <=19:
  print('Sua idade é {} anos, e sua categoria é JUNIOR'.format(idade))
elif idade <= 25:
  print('Sua idade é {} anos, e sua categoria é SÊNIOR'.format(idade))
else:
  print('Sua idade é {} anos, e sua categoria é MASTER'.format(idade))