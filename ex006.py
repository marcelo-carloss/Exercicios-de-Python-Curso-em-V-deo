# Solicita ao usuário que insira um número inteiro e armazena na variável n
n = int(input('Digite um número: '))

# Imprime na tela uma frase formatada com os resultados do dobro, triplo e raiz quadrada do número inserido
# Utiliza .format() para inserir os valores de n, n*2 (dobro de n), n*3 (triplo de n) e n**(1/2) (raiz quadrada de n)
print('O dobro de {} é: {}. O triplo de {} é: {}. E a raiz quadrada de {} é: {}' .format(n, (n*2), n, (n*3), n, (n**(1/2))))

