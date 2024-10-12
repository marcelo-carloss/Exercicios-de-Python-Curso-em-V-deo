# Imprime uma mensagem inicial
print('Olá, para descobrir a média das suas notas.')

# Solicita ao usuário que digite a primeira nota e armazena na variável nota1
nota1 = int(input('Digite sua primeira nota: '))

# Solicita ao usuário que digite a segunda nota e armazena na variável nota2
nota2 = int(input('Digite sua segunda nota: '))

# Calcula a média das duas notas inseridas
m = (nota1 + nota2) / 2

# Imprime na tela uma frase formatada com as notas digitadas e a média calculada
print('Sua nota 1 foi: {}, sua nota 2 foi: {}, e sua média foi: {}' .format(nota1, nota2, m))
