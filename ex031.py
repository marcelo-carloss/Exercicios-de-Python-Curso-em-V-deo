distancia = float(input('Digite a distancia em KM até a cidade de destino, para sabermos o valor da sua passagem: '))
if distancia <= 200:
  valor = distancia * 0.50
else:
  valor = distancia * 0.45
print('Sua passagem custará {} reais'.format(valor))
