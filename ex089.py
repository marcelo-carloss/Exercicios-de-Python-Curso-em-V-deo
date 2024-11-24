sistema = list()

cont = 0
while True:
  nome = str(input('Nome: '))
  nota1 = float(input('Nota 1: '))
  nota2 = float(input('Nota 2: '))
  media = (nota1 + nota2) / 2
  sistema.append([nome, [nota1, nota2], media])
  
  r = str(input('Quer continuar? [S/N]:'))
  if r in 'Nn':
    break
print('-=' * 30)
print(f'{"n°"} {"Nome":<8} {"Média":<13}')
print('-' * 30)
for i, a in enumerate(sistema):
  print(f'{i} {a[0]:<12}  {a[2]:<17}')
  cont += 1
print('-=' * 30)

while True:
  verNotas = int(input('Deseja ver as notas de qual aluno? (999 para sair): ')) 
  if verNotas == 999:
    break
  elif verNotas < len(sistema):
    print(f'As notas de {sistema[verNotas][0]} são {sistema[verNotas][1]}\n')
  elif verNotas > len(sistema):
    print('Aluno não existe\n')
print('-=' * 30)
print('Programa encerrado!')


