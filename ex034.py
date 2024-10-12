salario = float(input('Digite o seu salário: '))
if salario <= 1250:
 novo_salario = salario + (salario * 0.15)
else:
 novo_salario = salario + (salario * 0.10)
print('Você ganhava R${:.2f} e agora irá ganhar R${:.2f}'.format(salario, novo_salario))