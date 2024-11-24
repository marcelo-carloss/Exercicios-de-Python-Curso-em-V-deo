def votar(anoNas):
  from datetime import datetime
  idade = datetime.now().year - anoNas
  if idade < 16:
    return f'com {idade} anos: VOTO NEGADO'
  elif 16 <= idade <=18 or idade > 65:
    return f'com {idade} anos: VOTO OPCIONAL'
  else: 
    return f'com {idade} anos: VOTO OBRIGATÓRIO'

anoNascimento = int(input('Digite o ano que você nasceu: '))
print(votar(anoNascimento))