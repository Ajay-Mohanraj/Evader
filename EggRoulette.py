import pygame
import random
import sys


def main():
    pygame.init()
    size = [1500, 1500]
    screen = pygame.display.set_mode(size)
    button1 = pygame.Rect(15, 15, 20, 10)
    button2 = pygame.Rect(15, 15, 30, 10)
    button3 = pygame.Rect(15, 15, 40, 10)
    button4 = pygame.Rect(15, 15, 50, 10)
    button5 = pygame.Rect(15, 15, 60, 10)
    button6 = pygame.Rect(15, 15, 70, 10)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if button1.collidepoint(mouse_pos):
                    return True


button1 = pygame.Rect(15, 15, 20, 10)

main()
pygame.quit()
sys.exit()