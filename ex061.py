primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('digite a razão: '))
termo_atual = primeiro
cont = 1
while cont <= 10:
  print('{} → '.format(termo_atual), end='')
  termo_atual += razão
  cont += 1
print('FIM')