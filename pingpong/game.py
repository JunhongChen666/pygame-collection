import random

import pygame

pygame.init()
WIDTH = 500
HEIGHT = 500
BACKGROUND_COLOUR = (41, 36, 33)
INTERFACE_COLOUR = (41, 36, 33)
BUTTON_COLOUR = (100, 100, 100)
BUTTON_TEXT_COLOUR =  (255, 235, 205)
WHITE = (255, 255, 255)
#create a game window with a specific width and height
screen = pygame.display.set_mode((WIDTH, HEIGHT))
#create a name for the window
pygame.display.set_caption("plan pingpong")
#define clock
clock = pygame.time.Clock()

RACKET_IMG = pygame.image.load("racket.png")
BALL_IMG = pygame.image.load("ball.png")

class Button:

    def __init__(self, position, text, colour, size = (200, 50)):
        #draw the rectangle as the button
        rect_x, rect_y = position
        rectangle = pygame.Rect(position, size)
        self.rect = rectangle
        pygame.draw.rect(screen, colour, rectangle)
        #draw text on the button
        font = pygame.font.Font(None, 70)
        content = font.render(text, True, BUTTON_TEXT_COLOUR)
        screen.blit(content, position)

    def click(self, position):
        return self.rect.collidepoint(position)


def startInterface():
    clock = pygame.time.Clock()
    while True:
        screen.fill(INTERFACE_COLOUR)
        button_1 = Button((150, 175), '1 Player', BUTTON_COLOUR)
        button_2 = Button((150, 275), '2 Player', BUTTON_COLOUR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_1.click(pygame.mouse.get_pos()):
                    return 1
                elif button_2.click(pygame.mouse.get_pos()):
                    return 2
        clock.tick(10)
        pygame.display.update()

def endInterface(left_score, right_score):
    font1 = pygame.font.Font(None, 50)
    font2 = pygame.font.Font(None, 30)
    text1 = 'Player on left won!' if left_score > right_score else 'Player on right won!'
    text2 = 'Press ESCAPE to quit.'
    text3 = 'Press ENTER to continue or play again.'

    text1 = font1.render(text1, True, WHITE)
    text2 = font2.render(text2, True, WHITE)
    text3 = font2.render(text3, True, WHITE)

    rect1 = text1.get_rect()
    rect2 = text2.get_rect()
    rect3 = text3.get_rect()
    rect1.center = ((WIDTH//2, HEIGHT//2-100))
    rect2.center = ((WIDTH//2, HEIGHT//2+50))
    rect3.center = ((WIDTH//2, HEIGHT//2+100))
    while True:
        screen.fill(BACKGROUND_COLOUR)
        screen.blit(text1, rect1)
        screen.blit(text2, rect2)
        screen.blit(text3, rect3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()


        pygame.display.update()

class Racket(pygame.sprite.Sprite):
    def __init__(self, image, type, speed):
        super().__init__()
        self.image = RACKET_IMG
        self.type = type
        self.rect = self.image.get_rect()
        self.speed = speed

    def move(self, direction):
        if direction == "UP":
            self.rect.top = self.rect.top - self.speed
            self.rect.top = max(self.rect.top, 0)
        if direction== "DOWN":
            self.rect.bottom = self.rect.bottom + self.speed
            self.rect.bottom = min(self.rect.bottom, HEIGHT)

    def automove(self, ball):
        if ball.rect.centery > self.rect.centery:
            self.move("DOWN")
        if ball.rect.centery < self.rect.centery:
            self.move("UP")


    def reset(self):
        if self.type == "RIGHT":
            self.rect.right = WIDTH
        else:
            self.rect.left = 0
        self.rect.centery = HEIGHT//2

    def draw(self):
        screen.blit(self.image, self.rect)

class Ball(pygame.sprite.Sprite):
    def __init__(self, image, speed):
        super().__init__()
        self.image = image
        self.rect = image.get_rect()
        self.speed = speed

    def move(self, right_racket, left_racket, left_score, right_score):
        self.rect.centerx = self.rect.centerx + self.speed * self.directrion_x
        self.rect.centery = self.rect.centery + self.speed * self.directrion_y

        if pygame.sprite.collide_rect(self, right_racket) or pygame.sprite.collide_rect(self, left_racket):
            self.directrion_x = -self.directrion_x
            self.directrion_y = random.choice([1, -1])
            self.speed +=1
        elif self.rect.top < 0:
            self.directrion_y = 1

        elif self.rect.bottom > HEIGHT:
            self.directrion_y = -1

        elif self.rect.left < 0:
            self.reset()
            left_racket.reset()
            right_racket.reset()
            right_score +=1

        elif self.rect.right > WIDTH:
            self.reset()
            left_racket.reset()
            right_racket.reset()
            left_score +=1
        return left_score, right_score
    def reset(self):
        self.rect.centerx = WIDTH//2
        self.rect.centery = random.randrange(self.rect.height//2, HEIGHT - self.rect.height//2)
        self.directrion_x = random.choice([-1, 1])
        self.directrion_y = random.choice([-1, 1])
        self.speed = 1

    def draw(self):
        screen.blit(self.image, self.rect)



font = pygame.font.Font(None, 50)
running = True
game_mode = startInterface()
right_racket = Racket(RACKET_IMG, "RIGHT", 5)
right_racket.reset()
left_racket = Racket(RACKET_IMG, "LEFT", 5)
left_racket.reset()
ball = Ball(BALL_IMG, 1)
ball.reset()
left_score = 0
right_score = 0
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BACKGROUND_COLOUR)

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_UP]:
        right_racket.move('UP')
    elif pressed_keys[pygame.K_DOWN]:
        right_racket.move('DOWN')
    if game_mode == 2:
        if pressed_keys[pygame.K_w]:
            left_racket.move('UP')
        elif pressed_keys[pygame.K_s]:
            left_racket.move('DOWN')
    else:
        left_racket.automove(ball)

    pygame.draw.rect(screen, WHITE, (247, 0, 6, 500))
    right_racket.draw()
    left_racket.draw()
    left_score, right_score = ball.move(right_racket, left_racket, left_score, right_score)
    ball.draw()

    screen.blit(font.render(str(left_score), False, WHITE), (150, 10))
    screen.blit(font.render(str(right_score), False, WHITE), (300, 10))
    if left_score == 11 or right_score == 11:
        break
    pygame.display.update()

endInterface(left_score, right_score)
pygame.quit()

