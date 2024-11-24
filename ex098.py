from time import sleep
def contador(inicio, fim, passo):
  
  if passo == 0:
    passo == 1
    
  if passo < 0:
    passo *= -1

  print(f'De {inicio} até {fim} de {passo} em {passo}')

  if inicio < fim:
    cont = inicio
    while inicio <= fim:
      print(inicio, end=' ', flush=True)
      sleep(0.5)
      cont += passo
    print('FIM!')
    
  else:
    cont = inicio
    while inicio >= fim:
      print(inicio, end=' ', flush=True)
      sleep(0.5)
      cont -= passo
    print('FIM!')
      
contador(1,10,1)
print()
contador(10,0,-2)
print('Contagem personalizada')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)