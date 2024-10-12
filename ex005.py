# Imprime uma mensagem inicial
print('Insira um número, e te mostrarei o anterior e o próximo número!')

# Solicita ao usuário que digite um número inteiro e armazena na variável n
n = int(input('Digite qualquer número: '))

# Calcula o número anterior (na) e o próximo número (np) em relação a n
na = n - 1
np = n + 1

# Imprime na tela uma frase formatada com o número digitado, o número anterior e o próximo número
print('O número que você digitou foi {}, o número anterior a ele é {}, e o próximo número é {}' .format(n, na, np))
