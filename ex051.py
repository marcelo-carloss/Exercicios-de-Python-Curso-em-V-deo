pt = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite o valor da razão desse PA: '))
termos = [pt]
for n in range(0, 9):
 pt += r
 termos.append(pt)
print(termos)

# A forma acima foi como eu fiz

# a forma abaixo foi feito na aula:

'''
primeiro = int(input('Digite o primeiro termo de uma PA: '))
razao = int(input('Digite o valor da razão dessa PA: '))
décimo = primeiro + (10 - 1) * razao
for c in range(primeiro, décimo + razao, razao):
  print('{}'.format(c), end=' → ')
print('ACABOU!')
'''
