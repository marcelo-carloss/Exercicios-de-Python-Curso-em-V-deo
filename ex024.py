# Solicita ao usuário que digite o nome da cidade e armazena o valor em 'cidade'
cidade = input('Digite o nome da sua cidade: ')

# Verifica se os primeiros 5 caracteres da string (convertidos para maiúsculas) são iguais a 'SANTO'
if cidade[:5].upper() == 'SANTO':
    # Se a condição for verdadeira, exibe que a cidade começa com "Santo"
    print('Sua cidade começa com a palavra "Santo"')
else:
    # Caso contrário, exibe que a cidade não começa com "Santo"
    print('Sua cidade não começa com a palavra "Santo"')
