import random
print('JOGO DO PAR OU ÍMPAR')
print('-' * 50)
ganhou = True
vitoria = 0
while ganhou:
  jogador = int(input('Digite um número: '))
  computador = random.randint(1,10)
  total = jogador + computador
  resultado = ' '
  while resultado not in 'PI':
    resultado = str(input('Você quer Ímpar ou Par? [I/P] ')).strip()[0].upper()
  print('-' * 50)
  print(f'Você jogou {jogador} e o computador {computador}. Total de {total} DEU PAR')
  if total % 2 == 0:
    if resultado == 'P':
      print('DEU PAR')
      print('-' * 50)
      print('Você GANHOU! \n Bora jogar novamente...')
      vitoria += 1
    else:
      print('DEU PAR')
      print('-' * 50)
      print('Você PERDEU!')
      ganhou = False
  else:
    if resultado == 'I':
      print('DEU ÍMPAR')
      print('-' * 50)
      print('Você GANHOU! \n Bora jogar novamente...')
      vitoria += 1
    else:
      print('DEU ÍMPAR')
      print('-' * 50)
      print('Você PERDEU!')
      ganhou = False
print('-' * 50)
print(f'Você ganhou {vitoria} vezes.')