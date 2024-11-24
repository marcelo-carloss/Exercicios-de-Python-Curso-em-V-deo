expressao = str(input('Digite uma expressão: '))
verificar = []
for c in expressao:
  if c == '(':
    verificar.append('(')
  elif c == ')':
    if len(verificar) > 0:
      verificar.pop()
    else:
      verificar.append(')')
      break
if len(verificar) == 0:
  print('Sua expressão está correta.')
else:
  print('Expressão inválida')  