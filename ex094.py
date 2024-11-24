sistema = list()
pessoas = {}
while True:
  pessoas['nome'] = str(input('Nome: '))
  pessoas['sexo'] = str(input('Sexo: [M/F] ')).upper().split()[0]
  pessoas['idade'] = int(input('Idade: '))
  sistema.append(pessoas.copy())
  pessoas.clear()
  r = str(input('Quer continuar? [S/N] '))
  if r in 'Nn':
    break
media = 0
for i in sistema:
  media += i["idade"] / len(sistema)
print('=-' * 30)
print(f' - O grupo tem {len(sistema)} pessoas')
print(f' - A média de idade do grupo é {media}')
print(f' - As mulheres cadastradas foram: ', end='')
for pessoas in sistema:
  if pessoas["sexo"] == 'F':
   print(f'{pessoas["nome"]}',end=' ')
print('\n - Lista das pessoas que estão acima da média:\n')
for pessoas in sistema:
  if pessoas['idade'] > media:
    print(f'nome = {pessoas["nome"]}; sexo = {pessoas["sexo"]}; idade = {pessoas["idade"]};\n')