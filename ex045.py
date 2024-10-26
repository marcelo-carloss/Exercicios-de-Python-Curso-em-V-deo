import random
jokenpô = ['pedra','papel','tesoura']
computador = random.choice(jokenpô)
print('Vamos jogar Jokenpô! Esse jogo consiste em escolher entre Pedra, Papel ou Tesoura. Você jogará contra o computador. Lembrando que Pedra ganha de Tesoura, a Tesoura do Papel e o Papel da Pedra! \n\n')
jogador = str(input('Vamos lá, escolha uma das opções: \n '))

if computador == jogador:
  print('Deu empate, você escolheu {} e o computador também escolheu {}'.format(jogador, computador))
else:
  if computador == 'pedra' and jogador == 'tesoura':
    print('Você PERDEU, o computador escolheu {} e você escolheu {}'.format(computador, jogador))
  elif computador == 'papel' and jogador == 'pedra':
    print('Você PERDEU, o computador escolheu {} e você escolheu {}'.format(computador, jogador))
  elif computador == 'tesoura' and jogador == 'papel':
    print('Você PERDEU, o computador escolheu {} e você escolheu {}'.format(computador, jogador))
  elif computador == 'pedra' and jogador == 'papel':
    print('Você GANHOU, o computador escolheu {} e você escolheu {}'.format(computador, jogador))
  elif computador == 'papel' and jogador == 'tesoura':
    print('Você GANHOU, o computador escolheu {} e você escolheu {}'.format(computador, jogador))
  elif computador == 'tesoura' and jogador == 'pedra':
    print('Você GANHOU, o computador escolheu {} e você escolheu {}'.format(computador, jogador))
print('\n\n Obrigado por jogar! Volte mais vezes.')