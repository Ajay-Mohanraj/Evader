import pygame

pygame.init()
win = pygame.display.set_mode((540, 525))
pygame.display.set_caption('First Game')


width = 40
height = 60
vel = 15

# The Player

class Player(object):

    def __init__(self, x, y, width, height, velocity=10, image="ohya.jpg"):
        self.isJump = False
        self.jumpCount = 10
        self.x = x
        self.y = y
        self.vel = velocity
        self.w = width
        self.h = height
        self.player = pygame.image.load(image)

    def work(self):


            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] and self.x > self.vel:

                self.x -= self.vel

            if keys[pygame.K_RIGHT] and self.x < 100 - self.w - self.vel:
                self.x += self.vel

            if keys[pygame.K_UP] and self.y > self.vel:
                self.y -= self.vel

            if keys[pygame.K_DOWN] and self.y < (500 - self.h - self.vel):
                self.y += self.vel
            """if not(isJump):
        
                if keys[pygame.K_UP] and y > vel:
        
                    y -= vel
        
                if keys[pygame.K_DOWN]and y < (500 - height - vel):
        
                    y += vel
        
                if keys[pygame.K_SPACE]:
        
                    isJump = True
        
            else:
        
                if jumpCount >= -10:
        
                    neg = 1
        
                    if jumpCount < 0:
        
                        neg = -1
        
                    y -= (jumpCount ** 2) ** 0.5 * neg
                    jumpCount -= 1
        
            else:
        
                isJump = False
                jumpCount = 10
            """



# The Projectiles

run = True
player1 = Player(210, 400, width, height, vel, "ohya.jpg")
while run:

    pygame.time.delay(50)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
    player1.work()

    win.fill((255, 255, 255))
    win.blit(player1.player, (player1.x, player1.y))
    pygame.display.update()


class Enemy(object):

    enemyList = [pygame.image.load('circle.png'), pygame.image.load('square.png'), pygame.image.load('triangle.png')]

    def __init__(self):
        pass
pygame.quit()
