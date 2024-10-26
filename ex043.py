altura = float(input('Digite sua altura(número decimal): '))
peso = float(input('Digite seu peso(número decimal): '))
IMC = peso / (altura ** 2)
if IMC < 18.5:
 print('Seu IMC é de: {:.2f}, seu status é ABAIXO DO PESO!'.format(IMC))
elif IMC >= 18.5 and IMC <= 25: 
 print('Seu IMC é de: {:.2f}, seu status é PESO IDEAL!'.format(IMC))
elif IMC > 25 and IMC <= 30:
 print('Seu IMC é de: {:.2f}, seu status é SOBREPESO!'.format(IMC))
elif IMC > 30 and IMC <= 40:
 print('Seu IMC é de: {:.2f}, seu status é OBESIDADE!'.format(IMC))
else:
 print('Seu IMC é de: {:.2f}, seu status é OBESIDADE MÓRBIDA!'.format(IMC))