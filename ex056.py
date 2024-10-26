homem = ''
mulher = 0
senior = 0
s = 0

for i in range(0,4):
  nome = str(input('Digite o seu nome: '))
  idade = int(input('Digite a sua idade: '))
  genero = int(input('Digite a opção que correposnde ao seu genêro: \n [1] Masculino \n [2] Feminino \n:'))
  s += idade
  if genero == 1:
    if idade > senior:
      homem = nome
      senior = idade
  else:
    if idade < 20:
      mulher += 1
print('a média de idade desse grupo de pessoas é de: {}'.format(s/4))
print('A idade do homem mais velho é {} e o seu nome é {}'.format(senior,homem))
print('A quantidade de mulheres com menos de 20 anos é: {}'.format(mulher))