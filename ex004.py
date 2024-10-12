# Imprime uma mensagem inicial
print('Agora vamos descobrir o tipo dos dados inseridos!')

# Solicita ao usuário que digite algo e armazena na variável dado
dado = input('Digite algo: ')

# Imprime o tipo do dado inserido usando a função type()
print('O tipo do dado inserido é', type(dado))

# Verifica se o dado é alfabético e imprime o resultado
print('É alfabético? ', dado.isalpha())

# Verifica se o dado é numérico e imprime o resultado
print('É numérico? ', dado.isnumeric())

# Verifica se o dado está em maiúsculas e imprime o resultado
print('É maiúsculo? ', dado.isupper())

# Verifica se o dado consiste apenas de espaços em branco e imprime o resultado
print('É um espaço? ', dado.isspace())

# Verifica se o dado é um decimal e imprime o resultado
print('É um decimal? ', dado.isdecimal())
