import math  # Importa a biblioteca math, que fornece funções matemáticas, como truncar números.

# Solicita ao usuário que insira um número real (float) e converte a entrada para um tipo float.
num = float(input('Digite um número real, para que possamos obter o numero inteiro: '))

# Utiliza a função math.trunc() para truncar a parte decimal do número e obter a parte inteira.
# A função math.trunc() remove a parte decimal de um número, efetivamente arredondando-o para zero.
# O resultado é então formatado e impresso.
print('A parte inteira do número digitado é: {}'.format(math.trunc(num)))
