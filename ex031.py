distancia = float(input('Digite a distancia em KM até a cidade de destino, para sabermos o valor da sua passagem: '))

# A linha acima solicita ao usuário que digite a distância em quilômetros e converte o valor para um número decimal (float).
# O valor digitado é armazenado na variável 'distancia'.

if distancia <= 200:
    # Esta condição verifica se a distância é menor ou igual a 200 km.
    # Se a condição for verdadeira, o preço da passagem é calculado com base em R$ 0,50 por km.
    valor = distancia * 0.50
else:
    # Se a condição for falsa (distância maior que 200 km), o preço da passagem é calculado com base em R$ 0,45 por km.
    valor = distancia * 0.45

print('Sua passagem custará {} reais'.format(valor))
# A linha acima imprime na tela o valor total da passagem, formatando o número como uma moeda.