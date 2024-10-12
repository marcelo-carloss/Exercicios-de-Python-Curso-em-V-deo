# Solicita ao usuário que digite um valor em metros e armazena na variável m
m = int(input('Conversor de metros para cm e mm. Digite um valor em metros: '))

# Calcula o valor em centímetros (cm) multiplicando m por 100
cm = m * 100

# Calcula o valor em milímetros (mm) multiplicando m por 1000
mm = m * 1000

# Imprime na tela uma frase formatada com os valores convertidos
print('{}m são {}cm e {}mm' .format(m, cm, mm))
