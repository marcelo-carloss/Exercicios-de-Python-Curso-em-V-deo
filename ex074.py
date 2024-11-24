import random
numeros = random.choices(range(1, 10), k= 5)
lista = (numeros)
print(f'Esses são os números aleatorios: {lista}')
print(f'Esse é o maior número da lista: {max(lista)}')
print(f'Esse é o menor número da lista: {min(lista)}')