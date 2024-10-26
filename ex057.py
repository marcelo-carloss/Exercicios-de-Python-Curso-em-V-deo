genero = str(input('Qual o seu sexo? [M/F]: ')).strip().upper()[0]
while genero not in 'MF':
  genero = str(input('Opção inválida, digite novamente. Qual seu sexo? [M/F]: ')).upper()
if genero == 'F':
  print('Mulher')
else:
  print('Homem')