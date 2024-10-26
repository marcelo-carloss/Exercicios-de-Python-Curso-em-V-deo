print('MARCELO BANK')
print('-' * 50)
valor = int(input('Qual valor você deseja sacar? R$'))
total = valor
cédula = 50
totalCédula = 0

while True:
  if total >= cédula:
    total -= cédula
    totalCédula += 1
  else:
    if totalCédula > 0:
      print(f'Foram {totalCédula} de {cédula}')
    if cédula == 50:
      cédula = 20
    elif cédula == 20:
      cédula = 10
    elif cédula == 10:
      cédula = 1
    totalCédula = 0
    if total == 0:
      break
  
