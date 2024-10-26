from time import sleep
#Eu tinha feito dessa forma

'''for num in range(1, 50):
  if num % 2 == 0:
   print(num)
   sleep(0.5)'''

#Forma mais adequada de fazer, pois assim terá menos iterações
for num in range(2,51,2):
  print(num)
  sleep(0.5)

  