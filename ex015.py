# Solicita ao usuário que digite o número de dias que o carro ficou alugado
dias = int(input('Quantos dias o carro ficou alugado? '))

# Solicita ao usuário que digite a quantidade de quilômetros percorridos com o carro
km = float(input('Quantos KM percorridos? '))

# Calcula o valor total a pagar pelo aluguel do carro
# Cada dia de aluguel custa R$60 e cada quilômetro percorrido custa R$0.15
pago = (dias * 60) + (km * 0.15)

# Exibe na tela o valor total a pagar formatado com duas casas decimais
print('O total a pagar é de R${:.2f}' .format(pago))
