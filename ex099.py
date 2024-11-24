from time import sleep

def maior(*num):
  print('Analisando os valores passados....')
  maior = 0
  tam = len(num)
  for i in num:
    if i > maior:
      maior = i
    print(f'{i}',end=' ', flush=True)
    sleep(0.5)
    
  print(f'Foram informados {tam} valores ao todo')
  print(f' O maior valor informado foi {maior}')
  print('=-' * 30)

maior(3, 5, 9, 4, 2, 7)
maior(0, 4, 7, 8, 2)
maior(2, 0, 10, 3)
maior(3, 1, 5,)
maior(7, 4) 
maior(2)
maior(0)
maior()