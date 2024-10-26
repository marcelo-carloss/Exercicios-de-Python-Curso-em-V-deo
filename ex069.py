mulherMenos20 = homens = pessoasMaior18 = 0
while True:
  print('CADASTRAR NOVA PESSOA')
  print('-' * 50)
  idade = int(input('Idade da pessoa: '))
  sexo = ' '
  while sexo not in 'FM':
    sexo = str(input('Sexo da pessoa [F/M]: '))
  if idade > 18:
    pessoasMaior18 += 1
  if sexo == 'M':
    homens += 1
  if idade < 20 and sexo == 'F':
    mulherMenos20 += 1
  continuar = ' '
  while continuar not in 'SN':
    continuar = str(input('Quer continuar? [S/N]')).strip()[0].upper()
  if continuar == 'S':
    print('Quero\n')
  elif continuar == 'N':
    break
print('PROGRAMA ENCERRADO!')
print('-' * 50)
print(f'Foram {pessoasMaior18} pessoas cadastradas com mais de 18 anos.')
print(f'Foram {homens} homens cadastrados.')
print(f'Foram {mulherMenos20} mulheres com menos de 20 anos cadastrados.')