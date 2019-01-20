import pygame
import random

pygame.init()
win = pygame.display.set_mode((540, 525))
pygame.display.set_caption('First Game')
win_width = 540
win_height = 525

font = pygame.font.Font(None, 25)

x = 210
y = 400
width = 40
height = 60
vel = 15

BALL_SIZE = 25

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

            if keys[pygame.K_RIGHT] and self.x < 500 - self.w - self.vel:
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


ball_list = []


class Ball:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.y_vel = 0
        self.x_vel = 0


def make_ball():
    ball = Ball()

    ball.x = random.randrange(BALL_SIZE, win_width - BALL_SIZE)
    ball.y = random.randrange(BALL_SIZE, win_height - BALL_SIZE)

    ball_speed = random.randrange(1, 20)
    ball.x_vel = ball_speed
    ball.y_vel = ball_speed
    return ball


run = True

player1 = Player(x, y, width, height, vel, "ohya.jpg")
while run:

    pygame.time.delay(50)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
    player1.work()

    if len(ball_list) < 10:
        ball = make_ball()
        ball_list.append(ball)
    win.fill((0, 255, 150))
    for ball in ball_list:
        # Move the ball's center
        ball.x += ball.x_vel
        ball.y += ball.y_vel

        # Bounce the ball if needed
        if ball.y > win_height - BALL_SIZE or ball.y < BALL_SIZE:
            ball.y_vel *= -1
        if ball.x > win_width - BALL_SIZE or ball.x < BALL_SIZE:
            ball.x_vel *= -1
    for ball in ball_list:
        pygame.draw.circle(win, (255, 0, 0), (ball.x, ball.y), BALL_SIZE)
        if (player1.x - 20) < ball.x < (player1.x + 20) and (player1.y - 30) < ball.y < (player1.y +30):
            win.fill((255, 0, 0))
            while True:
                text = font.render("You died!", True, (0, 0, 0))
                win.blit(text, (win_width // 2, win_height // 2))

    win.blit(player1.player, (player1.x, player1.y))
    pygame.display.update()


pygame.quit()
