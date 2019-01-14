import pygame
import random

class EggRoulette(object):
    def __init__(self):
        pygame.init()
        self.eggs = ["boiled", "boiled", "boiled", "boiled", "boiled", "raw"]
        self.makeBttn()

    def makeBttn(self):
        mouse = pygame.mouse.get_pos()
        if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, bright_green, (150, 450, 100, 50))
        else:
            pygame.draw.rect(gameDisplay, green, (150, 450, 100, 50))


    def roulette(self):
        thing = random.choice(self.eggs)
        if thing == "raw":
            return False
        else:
            self.eggs.remove("boiled")
            return True

    def endGame(self):
        pic = pygame.image.load("ohya.jpg")
        pygame.display.set_icon(pic)
        pygame.display.set_caption("YOU GOT EGGED!")


def main():
    game = EggRoulette()
    boolean = game.roulette()

    while boolean is True:
        boolean = game.roulette





