import random  # Importa o módulo random, que contém funções para gerar números aleatórios e realizar sorteios.

# Leitura dos nomes dos alunos
aluno1 = input("Digite o nome do primeiro aluno: ")
# Solicita ao usuário que digite o nome do primeiro aluno e armazena o nome na variável aluno1.

aluno2 = input("Digite o nome do segundo aluno: ")
# Solicita ao usuário que digite o nome do segundo aluno e armazena o nome na variável aluno2.

aluno3 = input("Digite o nome do terceiro aluno: ")
# Solicita ao usuário que digite o nome do terceiro aluno e armazena o nome na variável aluno3.

aluno4 = input("Digite o nome do quarto aluno: ")
# Solicita ao usuário que digite o nome do quarto aluno e armazena o nome na variável aluno4.

# Criação de uma lista com os nomes dos alunos
alunos = [aluno1, aluno2, aluno3, aluno4]
# Cria uma lista chamada alunos que contém os nomes dos quatro alunos digitados pelo usuário.

# Embaralhamento da lista de alunos
random.shuffle(alunos)
# Usa a função random.shuffle() para embaralhar a lista de alunos de forma aleatória.

# Exibição da sequência dos alunos
print("A sequência sorteada dos alunos é:")
for i, aluno in enumerate(alunos, start=1):
    print(f"{i}. {aluno}")
# Exibe a sequência sorteada dos alunos, numerando cada aluno na lista embaralhada.
