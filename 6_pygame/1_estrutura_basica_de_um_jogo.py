import pygame

pygame.init()

tela = pygame.display.set_mode((700,700))
pygame.display.set_caption("Meu primeiro jogo")

running = True
while running:
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            running = False

    tela.fill((0,0,0))
    pygame.display.update()

pygame.quit()