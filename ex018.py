import math  # Importa o módulo math, que fornece funções matemáticas, como seno, cosseno e tangente.

# Leitura do ângulo em graus e conversão para radianos em uma única linha
angulo_radianos = math.radians(float(input("Digite um ângulo em graus: ")))
# input("Digite um ângulo em graus: ") - Solicita ao usuário que insira um ângulo em graus.
# float(...) - Converte a entrada do usuário (uma string) para um número de ponto flutuante (float).
# math.radians(...) - Converte o ângulo de graus para radianos.
# O valor em radianos é então armazenado na variável angulo_radianos.

# Cálculo do seno, cosseno e tangente
seno = math.sin(angulo_radianos)
# math.sin(angulo_radianos) - Calcula o seno do ângulo em radianos e armazena o resultado na variável seno.

cosseno = math.cos(angulo_radianos)
# math.cos(angulo_radianos) - Calcula o cosseno do ângulo em radianos e armazena o resultado na variável cosseno.

tangente = math.tan(angulo_radianos)
# math.tan(angulo_radianos) - Calcula a tangente do ângulo em radianos e armazena o resultado na variável tangente.

# Exibição dos resultados
print(f"Seno: {seno}")
# print(f"Seno: {seno}") - Exibe o valor do seno no console.

print(f"Cosseno: {cosseno}")
# print(f"Cosseno: {cosseno}") - Exibe o valor do cosseno no console.

print(f"Tangente: {tangente}")
# print(f"Tangente: {tangente}") - Exibe o valor da tangente no console.
