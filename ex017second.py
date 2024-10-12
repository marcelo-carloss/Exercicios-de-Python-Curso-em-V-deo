from math import hypot

# Ler os valores dos catetos
CO = float(input("Digite o comprimento do cateto oposto: "))
CA = float(input("Digite o comprimento do cateto adjacente: "))

# Calcular o comprimento da hipotenusa usando o Teorema de Pitágoras
H = hypot(CO, CA)

# Mostrar o resultado
print(f"O comprimento da hipotenusa é: {H}")