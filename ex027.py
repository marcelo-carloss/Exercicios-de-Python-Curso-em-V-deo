# Solicita ao usuário que digite o nome completo e remove os espaços extras nas extremidades
n = str(input('Digite o seu nome completo: ')).strip()

# Divide o nome completo em uma lista de palavras, onde cada palavra é separada por espaços
nome = n.split()

# Exibe uma saudação utilizando o primeiro nome (a primeira palavra da lista)
print('Eai, {}. satisfação!'.format(nome[0]))

# Exibe o primeiro nome da lista (a primeira palavra)
print('Seu primeiro nome é: {}'.format(nome[0]))

# Exibe o último nome da lista (a última palavra), acessando o último índice com len(nome)-1
print('Seu último nome é: {}'.format(nome[len(nome) - 1]))
