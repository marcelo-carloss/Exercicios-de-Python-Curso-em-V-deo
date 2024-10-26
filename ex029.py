# Solicita ao usuário que informe a sua velocidade e converte a entrada para um número inteiro
vel = int(input('Qual a sua velocidade? '))

# Verifica se a velocidade é maior que 80 km/h
if vel > 80:
    # Calcula a multa, sendo 7 reais por cada km/h acima do limite de 80
    multa = (vel - 80) * 7
    # Exibe o valor da multa
    print('Você ultrapassou o limite de 80km/h e foi multado em: {} reais'.format(multa))

# Exibe uma mensagem final, independentemente de o usuário ter sido multado ou não
print('Bom dia, tome cuidado durante a viagem e não ultrapasse os limites de velocidade!')
