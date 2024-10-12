import math

# Ler os valores dos catetos
CO = float(input("Digite o comprimento do cateto oposto: "))
CA = float(input("Digite o comprimento do cateto adjacente: "))

# Calcular o comprimento da hipotenusa usando o Teorema de Pitágoras
H = math.sqrt(CO**2 + CA**2)

# Mostrar o resultado
print(f"O comprimento da hipotenusa é: {H}")
