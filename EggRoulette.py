import pygame
import random


boiled_egg = pygame.image.load("egg.jpg")
raw_egg = pygame.image.load("raw_egg.jpg")
eggs = ["boiled", "boiled", "boiled", "boiled", "boiled", "raw"]

def press_button(screen, button):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if button.collidepoint(mouse_pos):
                    egg = random.choice(eggs)
                    while True:
                        if egg == "raw":
                            screen.blit(raw_egg, (15, 15))
                            pygame.display.flip()
                        else:
                            screen.blit(boiled_egg, (15, 15))
                            pygame.display.flip()

def main():
    pygame.init()
    size = [1500, 1500]
    bg = [255, 255, 255]
    clock = pygame.time.Clock()
    fps = 60
    screen = pygame.display.set_mode(size)

    button1 = pygame.Rect(15, 15, 20, 10)
    button2 = pygame.Rect(15, 15, 30, 10)
    button3 = pygame.Rect(15, 15, 40, 10)
    button4 = pygame.Rect(15, 15, 50, 10)
    button5 = pygame.Rect(15, 15, 60, 10)
    button6 = pygame.Rect(15, 15, 70, 10)

    press_button(screen, button1)
    press_button(screen, button2)
    press_button(screen, button3)
    press_button(screen, button4)
    press_button(screen, button5)
    press_button(screen, button6)

    screen.fill(bg)

    pygame.draw.rect(screen, [255, 0, 0], button1)
    pygame.draw.rect(screen, [255, 0, 0], button2)
    pygame.draw.rect(screen, [255, 0, 0], button3)
    pygame.draw.rect(screen, [255, 0, 0], button4)
    pygame.draw.rect(screen, [255, 0, 0], button5)
    pygame.draw.rect(screen, [255, 0, 0], button6)

    pygame.display.update()
    clock.tick(fps)


if __name__ == '__main__':
    while True:
        main()
        pygame.quit()

