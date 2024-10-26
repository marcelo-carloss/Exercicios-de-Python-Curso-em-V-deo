# Solicita ao usuário que digite uma frase, converte para maiúsculas e remove espaços extras das extremidades
frase = str(input('Digite uma frase: ')).upper().strip()

# Conta quantas vezes a letra 'A' aparece na frase e exibe o resultado
print('Na frase aparece a letra A {} vezes.'.format(frase.count('A')))

# Encontra a posição da primeira ocorrência da letra 'A' e exibe, somando 1 para ajustar a contagem (posição humana, começa em 1)
print('Na frase aparece a letra A pela primeira vez na posição {}'.format(frase.find('A') + 1))

# Encontra a posição da última ocorrência da letra 'A' e exibe, também ajustando a contagem para começar em 1
print('Na frase aparece a letra A pela última vez na posição {}'.format(frase.rfind('A') + 1))
