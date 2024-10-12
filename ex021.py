import pygame  # Importa a biblioteca pygame, que é usada para criar jogos e aplicações multimídia em Python.

# Inicializa o mixer do pygame, que é o módulo responsável por carregar e reproduzir sons.
pygame.mixer.init()

# Carrega o arquivo MP3 especificado ('Piração - (ex021).mp3') no mixer. 
# Certifique-se de que o arquivo está no mesmo diretório que o script ou forneça o caminho correto.
pygame.mixer.music.load('Piração - (ex021).mp3')

# Inicia a reprodução do arquivo MP3 carregado.
pygame.mixer.music.play()

# Entra em um loop que continua enquanto a música está tocando.
# A função pygame.mixer.music.get_busy() retorna True enquanto a música está tocando.
while pygame.mixer.music.get_busy():
    # pygame.time.Clock().tick(10) faz o loop esperar 10 milissegundos antes de verificar novamente se a música ainda está tocando.
    # Isso evita que o loop consuma 100% da CPU.
    pygame.time.Clock().tick(10)
