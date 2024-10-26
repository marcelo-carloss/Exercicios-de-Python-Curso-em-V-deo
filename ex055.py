peso = []
for i in range(0, 5):
  peso.append(float(input('Digite seu peso: ')))
menor = min(peso)
maior = max(peso)
print('O maior peso lido foi {}, e o menor peso lido foi {}'.format(maior, menor))