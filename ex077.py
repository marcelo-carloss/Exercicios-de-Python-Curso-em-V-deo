lista = ('Cerveja', 'Agua', 'Suco', 'Comida', 'Salada', 'Brisa', 'Marcelo', 'Carro', 'Moto', 'Programaçao', 'Oliveira', 'Saxofone', 'Jesus', 'Nossa', 'Senhora')
for palavras in lista:
  print(f'\nNa palavra {palavras.upper()} tem as vogais: ', end='')
  for vogais in palavras:
    if vogais in 'aeiou':
      print(vogais, end=' ')
