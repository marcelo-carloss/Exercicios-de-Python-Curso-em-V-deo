# Solicita ao usuário que digite o nome completo e armazena o valor em 'nome'
nome = input('Digite o seu nome completo, por favor: ')

# Verifica se a palavra 'SILVA' está presente no nome, independentemente de maiúsculas ou minúsculas
if 'SILVA' in nome.upper():
    # Se a palavra 'SILVA' for encontrada, exibe que o nome contém "Silva"
    print('Seu nome contém "Silva"')
else:
    # Se a palavra 'SILVA' não for encontrada, exibe que o nome não contém "Silva"
    print('Seu nome não contém "Silva"')
