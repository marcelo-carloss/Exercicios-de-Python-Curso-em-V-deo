def leiaInt(msg):
  while True:
    try:
      n = int(input(msg))
    except (ValueError, TypeError):
      print('\033[0;31mERRO: por favor, digite um número inteiro válido.\033[m')
      continue
    except KeyboardInterrupt:
      print('\n\033[0;31mUsuário preferiu não digitar esse número.\033[m')
      return 0
    else:
      return n

def linha(tam=40):
  print('-' * tam)

def cabecalho(msg):
  linha()
  print(msg.center(40))
  linha()

def menu(lst):
  cabecalho('MENU PRINCIPAL')
  c = 1
  for item in lst:
    print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
    c += 1
  linha()
  opç = leiaInt('\033[34mSua opção: \033[m')
  return opç

