# Solicita a largura e altura da parede ao usuário
largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))

# Calcula a área da parede
area = largura * altura

# Cada lata de tinta pinta 2 metros quadrados
area_por_lata = 2

# Calcula quantas latas de tinta são necessárias
latas_necessarias = area / area_por_lata

# Exibe a área da parede e o número de latas necessárias
print(f"\nÁrea da parede: {area:.2f} metros quadrados")
print(f"Latas de tinta necessárias: {latas_necessarias}")
