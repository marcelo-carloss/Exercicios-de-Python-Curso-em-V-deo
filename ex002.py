# Pede a o usuario que digite se nome, guarda na variavel 'nome' e após isso imorime na tela o a frase e o nome dele
cores = {'amarelo':'\033[33m',
         'azul':'\033[34m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'limpa':'\033[m'}

nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer, {}{}{}'.format(cores['amarelo'], nome, cores['limpa']))