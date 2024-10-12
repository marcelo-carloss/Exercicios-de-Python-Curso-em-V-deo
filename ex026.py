frase = str(input('Digite uma frase: ')).upper().strip()
print('Na frase aparece a letra A {} vezes.' .format(frase.count('A')))
print('Na frase aparece a letra A pela primeira vez na posição {}' .format(frase.find('A')+1))
print('Na frase aparece a letra A pela última vez na posição {}' .format(frase.rfind('A')+1))
 