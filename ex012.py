# Valor original do produto
valor_original = float(input("Digite o valor original do produto: "))

# Calcula o valor do desconto (5%)
desconto = valor_original * 0.05

# Calcula o valor com desconto
valor_com_desconto = valor_original - desconto

# Exibe o valor original, o desconto aplicado e o valor final com desconto
print(f"Valor original: R${valor_original:.2f}")
print(f"Desconto de 5%: R${desconto:.2f}")
print(f"Valor com desconto: R${valor_com_desconto:.2f}")
