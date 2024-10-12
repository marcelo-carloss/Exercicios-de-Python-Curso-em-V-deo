# Solicita ao usuário que digite um valor em reais para converter em dólares e armazena na variável r
r = float(input('Quer saber quantos dólares você pode comprar? Digite quanto em reais você possui: '))

# Calcula a quantidade de dólares que podem ser comprados dividindo r pela taxa de câmbio (3.27 reais por dólar)
d = r / 3.27

# Imprime na tela uma frase formatada com os valores inseridos e o resultado da conversão
print('Com {} reais, você consegue comprar {:.2f} dólares.' .format(r, d))
