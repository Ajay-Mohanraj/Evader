import pygame
import random

class App(object):
    def __init__(self):
        pygame.init()
        self.eggs = ["boiled", "boiled", "boiled", "boiled", "boiled", "raw"]
        self.make_bttn()
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640, 400

    def roulette(self):
        thing = random.choice(self.eggs)
        if thing == "raw":
            self.endGame()
        else:
            self.eggs.remove("boiled")
            return True

    def make_bttn(self):
        mouse = pygame.mouse.get_pos()

        if 150 + 100 > mouse[0] > 150 and 450 + 50 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, bright_green, (150, 450, 100, 50))
        else:
            pygame.draw.rect(gameDisplay, "green", (150, 450, 100, 50))
        pygame.display.update()


    def endGame(self):
        pic = pygame.image.load("ohya.jpg")
        pygame.display.set_icon(pic)
        pygame.display.set_caption("YOU GOT EGGED!")

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        pass

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()