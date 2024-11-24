import moeda

preço = float(input('Digite o preço: R$'))
print(f'A metade de {preço} é {moeda.metade(preço)}')
print(f'O dobro de {preço} é {moeda.dobro(preço)}')
print(f'Aumentando 20%, temos {moeda.aumentar(preço, 20)}')
print(f'Reduzindo 10%, temos {moeda.diminuir(preço, 10)}')