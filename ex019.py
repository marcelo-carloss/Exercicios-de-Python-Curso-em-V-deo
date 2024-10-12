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

# Sorteio de um aluno
aluno_sorteado = random.choice(alunos)
# Usa a função random.choice() para selecionar aleatoriamente um nome da lista alunos e armazena o nome sorteado na variável aluno_sorteado.

# Exibição do aluno sorteado
print(f"O aluno sorteado foi: {aluno_sorteado}")
# Exibe o nome do aluno sorteado usando uma f-string para formatar a mensagem.
