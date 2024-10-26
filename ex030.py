num = int(input('Digite um número e te direi se ele é PAR ou IMPAR: '))

# A linha acima solicita ao usuário que digite um número e o converte para um número inteiro.
# O valor digitado é armazenado na variável 'num'.

if num % 2 == 0:
    # Esta linha verifica se o resto da divisão de 'num' por 2 é igual a 0.
    # Se o resto for 0, significa que o número é par.
    print('O número {}, é PAR'.format(num))
else:
    # Se o resto da divisão não for 0, significa que o número é ímpar.
    print('O número {}, é ÍMPAR'.format(num))