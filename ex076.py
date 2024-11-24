lista = ('Maçã', 1, 'Banana', 3, 'Bolacha', 4.50, 'Arroz', 30, 'Feijão', 20, 'Pastel', 6, 'Suco', 2.50, 'Pizza', 45) 
print('-' * 50)
print('LISTAGEM DE PREÇOS')
print('-' * 50)
for i in range(0 , len(lista), 2):
  print(f'{lista[i]:.<30}R$ {lista[i +1]:.2f}')