# Importa a biblioteca random para gerar números aleatórios
import random

# Importa a função sleep da biblioteca time para adicionar um atraso na execução
from time import sleep

# Solicita ao usuário que insira um número inteiro entre 0 e 5
num = int(input('Vamos brincar de adivinhar? O computador irá gerar um número aleatório entre 0 e 5, e você terá que adivinhar. Qual número você pensou?: '))

# Gera um número aleatório entre 0 e 5 usando a função randint
sorteio = random.randint(0, 5)

# Exibe uma mensagem de "carregando" para simular processamento
print('LOADING...')
sleep(2)  # Aguarda 2 segundos antes de continuar

# Verifica se o número escolhido pelo usuário é igual ao número sorteado pelo computador
if num == sorteio:
    # Se o usuário acertar, exibe uma mensagem de parabéns
    print('PARABÉNS VOCÊ ACERTOU!!!!')
else:
    # Caso contrário, exibe uma mensagem dizendo que o usuário errou e mostra o número sorteado
    print('Que pena, você errou! Eu pensei no número {} e não no {}'.format(sorteio, num))
