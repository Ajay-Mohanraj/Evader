import pygame
import random

pygame.init()
win = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption('First Game')
win_width = 900
win_height = 900

font = pygame.font.Font(None, 25)

x = 210
y = 400
width = 88
height = 96
vel = 3

BALL_SIZE = 25

clock = pygame.time.Clock()
frame_count = 0
frame_rate = 60


# The Player


class Player(object):

    def __init__(self, x, y, width, height, velocity=2, image="ohyabest.png"):

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

            if keys[pygame.K_LEFT] and self.x > 900 - self.vel:

                self.x -= self.vel

            if keys[pygame.K_RIGHT] and self.x < 900 - self.w - self.vel:
                self.x += self.vel

            if keys[pygame.K_UP] and self.y > 900 - self.vel:
                self.y -= self.vel

            if keys[pygame.K_DOWN] and self.y < (900 - self.h - self.vel):
                self.y += self.vel


ball_list = []


class Ball:

    def __init__(self):

        self.x = 0
        self.y = 0
        self.y_vel = 0
        self.x_vel = 0


class Timer:

    def __init__(self, frame_count, frame_rate):

        self.frame_count = frame_count
        self.frame_rate = frame_rate

    def time_elapsed(self):

        self.total_seconds = self.frame_count//self.frame_rate
        self.minutes = self.total_seconds // 60
        self.seconds = self.total_seconds % 60
        self.minutes = str(self.minutes)
        self.seconds = str(self.seconds)

        return self.minutes + ":" + self.seconds


def make_ball():

    ball = Ball()

    ball.x = random.randrange(BALL_SIZE, win_width - BALL_SIZE)
    ball.y = random.randrange(BALL_SIZE, win_height - BALL_SIZE)

    ball_speed = random.randrange(1, 3)
    ball.x_vel = ball_speed
    ball.y_vel = ball_speed
    return ball


run = True

timer = Timer(frame_count, frame_rate)
player1 = Player(x, y, width, height, vel, "ohya.jpg")

while run:
    clock.tick(frame_rate)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

    player1.work()

    time = font.render(timer.time_elapsed(), True, (0, 0, 0))
    win.blit(time, (10, 10))

    if timer.total_seconds % 10 == 0:
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

        if ((player1.x - 44) <= ball.x - 12.5 <= (player1.x + 44) or (player1.x - 44) <= ball.x + 12.5 <= (player1.x + 44)) and ((player1.y - 48) <= ball.y - 12.5 <= (player1.y + 48) or (player1.y - 48) <= ball.y + 12.5 <= (player1.y + 48)):
            win.fill((255, 0, 0))
            run = False

        else:

            pygame.draw.circle(win, (255, 0, 0), (ball.x, ball.y), BALL_SIZE)

    win.blit(player1.player, (player1.x, player1.y))
    pygame.display.update()
    timer.frame_count += 1
    clock.tick(frame_rate)

run = True
while run:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

    pygame.display.set_caption("YOU LOST!")
    text = font.render("YOU GOT HIT!", True, (0, 0, 0))

    if timer.minutes == "1" and timer.seconds == "1":
        other_text = font.render("YOU SURVIVED: " + timer.minutes + " minute and " + timer.seconds + " second", True, (0, 0, 0))

    elif timer.minutes == "1":
        other_text = font.render("YOU SURVIVED: " + timer.minutes + " minute and " + timer.seconds + " seconds", True, (0, 0, 0))

    elif timer.seconds == "1":
        other_text = font.render("YOU SURVIVED: " + timer.minutes + " minutes and " + timer.seconds + " second", True, (0, 0, 0))

    else:
        other_text = font.render("YOU SURVIVED: " + timer.minutes + " minutes and " + timer.seconds + " seconds", True, (0, 0, 0))

    win.blit(other_text, ((win_width // 2) - 75, (win_height // 2) + 20))
    win.blit(text, ((win_width // 2) - 30, win_height // 2))
    pygame.display.update()


pygame.quit()
