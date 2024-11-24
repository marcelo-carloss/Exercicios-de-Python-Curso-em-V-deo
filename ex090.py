alunos = {}
alunos['nome'] = str(input('Nome do aluno? '))
alunos['media'] = float(input(f'Média de {alunos['nome']}: '))
if alunos['media'] >= 7:
  alunos['situação'] = 'Aprovado'
elif 5 <= alunos["media"] < 7:
  alunos['situação'] = 'Recuperação'
else:
  alunos['situação'] = 'Reprovado'
for k, v in alunos.items():
  print(f'{k} é {v}')
