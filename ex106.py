from time import sleep

c = ('\033[m',          # 0 - sem cor
     '\033[0;30;41m',   # 1 - vermelho
     '\033[0;30;42m',   # 2 - verde
     '\033[0;30;43m',   # 3 - amarelo
     '\033[0;30;44m',   # 4 - azul
     '\033[0;30;45m',   # 5 - roxo
     '\033[7;30m'       # 6 - branco
     )      

def ajuda(com):
  titulo(f'Acessando o manual do comando \'{com}\'',4)
  print(c[3], end='')
  help(com)
  print(c[0], end='')
  sleep(1)

def titulo(msg, cor=0):
  tam = len(msg) + 4
  print(c[cor], end='')
  print('~' * tam)
  print(f'  {msg}')
  print('~' * tam)
  print(c[0], end='')
  sleep(1)

comando = ' '
while True:
  titulo('SISTEMA DE AJUDA', 5)
  comando = str(input('Função ou Biblioteca >> ')).upper() 
  if comando == 'FIM':
    break
  else:
    ajuda(comando)
titulo('ATÉ BREVE!', 3)