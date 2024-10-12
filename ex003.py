# Imprime uma mensagem inicial
print('Iremos fazer uma soma!')

# Solicita ao usuário que insira dois números inteiros e armazena nas variáveis n1 e n2
n1 = int(input('Digite o primeiro número que você desejar: '))
n2 = int(input('Digite o segundo número que você desejar: '))

# Calcula a soma dos dois números inseridos
s = n1 + n2

# Imprime na tela uma frase formatada com os números inseridos e o resultado da soma
print('Agora que você digitou os dois números, vamos fazer a soma. O primeiro número foi {}, e o segundo número foi {}. A soma entre eles resultará em: {}' .format(n1, n2, s))
