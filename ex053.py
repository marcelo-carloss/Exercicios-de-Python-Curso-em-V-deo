frase = str(input('Escreva uma frase: ')).replace(" ", "").upper()
print(frase)
frase_reversa = frase[::-1]
print('O inverso de {} é {}'.format(frase, frase_reversa))

if frase == frase_reversa:
  print('Essa frase é um palíndromo')
else:
  print('Essa frase NÃO é um palíndromo')