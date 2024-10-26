print('MARCELO BANK')
print('-' * 50)
ced50 = ced20 = ced10 = ced1 = valor = 0
valor = int(input('Qual valor você deseja sacar? R$'))

if valor > 50:
  ced50 = int(valor / 50)
  valor = valor % 50
if valor < 50 and valor >= 20:
  ced20 = int(valor / 20)
  valor = valor % 20
if valor < 20 and valor >= 10:
  ced10 = int(valor / 10)
  valor = valor % 10
if valor < 10 and valor >= 1 :
  ced1 = int(valor / 1)
  valor = valor % 1

print(f'Total de {ced50} cédulas de R$50.')
print(f'Total de {ced20} cédulas de R$20.')
print(f'Total de {ced10} cédulas de R$10.')
print(f'Total de {ced1} cédulas de R$1.')
print('-' * 50)

