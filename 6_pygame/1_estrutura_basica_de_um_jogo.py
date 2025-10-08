import pygame

pygame.init()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Meu primeiro jogo")

running = True
while running:
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            running = False
    screen.fill((0,0,0))

pygame.quit()