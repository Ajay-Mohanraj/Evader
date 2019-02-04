import pygame

pygame.init()
win = pygame.display.set_mode((400, 400))
win.fill((255, 255, 255))
run = True
player = pygame.image.load("OHYATHEGOD.png")
while run:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

    win.blit(player, (0, 0))