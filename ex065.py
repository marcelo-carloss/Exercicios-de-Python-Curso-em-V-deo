resposta = ''
soma = cont = 0
maior = menor = 0
while resposta != 'N':
  n = int(input('Digite um número: '))
  soma += n
  cont += 1
  if cont == 1:
    maior = menor = n  
  else:
    if n > maior:
      maior = n
    if menor > n:
      menor = n
  resposta = str(input('Deseja continuar? [S/N] ')).upper()

print('A quantidade de números digitados foram: {}'.format(cont))
print('A soma de todos os números deu: {}'.format(soma))  
print('A média de todos os números foi: {:.2f}'.format(soma/cont))
print('O menor número digitado foi: {}'.format(menor))
print('O maior número digitado foi: {}'.format(maior))
