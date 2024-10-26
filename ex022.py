# Solicita que o usuário digite o nome completo e armazena na variável 'nome'
nome = str(input('Digite seu nome completo: '))

# Exibe o nome com todas as letras maiúsculas
print('seu nome com todas as letras maiúsculas: {}'.format(nome.upper()))

# Exibe o nome com todas as letras minúsculas
print('seu nome com todas as letras minúsculas: {}'.format(nome.lower()))

# Remove os espaços do nome e calcula o número total de letras (sem contar os espaços)
print('seu nome tem {} letras'.format(len(nome.replace(' ', ''))))

# Divide o nome completo em uma lista de palavras e calcula o número de letras do primeiro nome
print('seu primeiro nome tem {} letras'.format(len(nome.split()[0])))
