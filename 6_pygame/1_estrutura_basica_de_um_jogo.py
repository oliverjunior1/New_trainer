import pygame

# inicializa o pygame
pygame.init()

# Cria a janela
tela = pygame.display.set_mode((800,600))
pygame.display.set_caption("Meu primeiro programa")

# Loop principal
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    tela.fill((0,0,0))
    pygame.display.update()
pygame.quit()