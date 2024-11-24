def calcular_area(l,c):
  area = l * c
  print(f'A área de um terreno {largura} x {comprimento} é de {area}m²')
def titulo(txt):
  print(f' {txt} ')
  print('-' * 20)

titulo('Controle de Terrenos')
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
calcular_area(largura,comprimento)