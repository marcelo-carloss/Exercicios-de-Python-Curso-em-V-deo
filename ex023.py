# Solicita ao usuário que digite um número entre 0 e 9999 e converte a entrada para inteiro
num = int(input('Digite um número de 0 a 9999: '))

# Calcula o dígito da unidade (último dígito do número)
u = num // 1 % 10

# Calcula o dígito da dezena (segundo dígito da direita para a esquerda)
d = num // 10 % 10

# Calcula o dígito da centena (terceiro dígito da direita para a esquerda)
c = num // 100 % 10

# Calcula o dígito do milhar (quarto dígito da direita para a esquerda)
m = num // 1000 % 10

# Exibe o dígito da unidade
print('Unidade: {}'.format(u))

# Exibe o dígito da dezena
print('Dezena: {}'.format(d))

# Exibe o dígito da centena
print('Centena: {}'.format(c))

# Exibe o dígito do milhar
print('Milhar: {}'.format(m))
