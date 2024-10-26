primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('digite a razão: '))
termoAtual = primeiro
cont = 1
maisTermos = 10
total = 0 
while maisTermos != 0:
  total = total + maisTermos
  while cont <= total:
    print('{} → '.format(termoAtual), end='')
    termoAtual += razão
    cont += 1
  print('PAUSA')
  maisTermos = int(input('Quantos termos a mais você deseja ver? '))
print('FIM DO PROGRAMA! Foram mostrados {} termos.'.format(total))