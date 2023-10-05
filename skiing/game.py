import pygame
import os
from cfg import *
import random
import time


def drawScore(screen, scoreFont, score):
    score = "score: "+str(score)
    score_text = scoreFont.render(score, True, BLACK)
    screen.blit(score_text, (0, 0))

class Skier(pygame.sprite.Sprite):
    def __init__(self, x, y, images):
        super().__init__()
        self.direction = 0 #(from -2 to 2)
        self.images = images
        self.image = self.images[0]
        self.rect =  self.image.get_rect(center=(x, y))
        self.speed = [self.direction, 6-abs(self.direction)*2]

    #change player's direction
    def turn(self, num):
        #update direction
        self.direction += num
        self.direction = min(2, self.direction)
        self.direction = max(-2, self.direction)
        #update image
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect(center=self.rect.center)
        #update speed
        self.speed = [self.direction, 6-abs(self.direction)*2]

    def move(self): #horizontally
        self.rect.centerx += self.speed[0]
        self.rect.centerx = max(20, self.rect.centerx)
        self.rect.centerx = min(620, self.rect.centerx)

    def set_fall(self):
        self.image = self.images[3]
        self.rect = self.image.get_rect(center=self.rect.center)

    
    def set_forward(self):
        self.image = self.images[0]
        self.direction = 0
        self.speed = [self.direction, 6-abs(self.direction)*2]
        self.rect = self.image.get_rect(center=self.rect.center)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, image, type):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center = (x, y))
        self.type = type
        self.passed = False
        
    def move(self, speed):
        self.rect.centery = self.rect.centery-speed

    def draw(self,screen):
        screen.blit(self.image, self.rect)

def create_obstacles(round, num = 10):
    obstacles = pygame.sprite.Group()
    locations = []
    if round ==1:
        s = 0
        e = 9
    else:
        s = 10
        e = 19
    for i in range(num):
        row = random.randint(s, e)
        col = random.randint(0, 9)
        x, y = (col * 64 + 20, row * 64 + 20)
        if (x, y) not in locations:
            locations.append((x, y))
            type = None
            IMG = None
            if random.randint(0, 1) == 1:
                type = 1
                IMG = TREE_IMG
            else:
                type = 0
                IMG = FLAG_IMG
            obstacle = Obstacle(x, y, IMG, type)
            obstacles.add(obstacle)
    return obstacles

def combine_obstacles(obstacles1, obstacles2):
    obstacles = pygame.sprite.Group()
    for obstacle in obstacles1:
        obstacles.add(obstacle)
    for obstacle in obstacles2:
        obstacles.add(obstacle)
    return obstacles


'''
start interface
'''
def show_start_interface(screen, WIDTH):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                return
        screen.fill(WHITE)
        font =  pygame.font.Font(None, WIDTH//10)

        title = font.render(u'SKIING', True, GREEN, WHITE)
        title_rect = title.get_rect()
        title_rect.center = (WIDTH/2, WIDTH/3)
        screen.blit(title, title_rect)

        content = font.render(u'press any key to start', True, BLUE, WHITE)
        content_rect = content.get_rect()
        content_rect.center = (WIDTH/2, WIDTH/2)
        screen.blit(content, content_rect)
        pygame.display.update()

def redraw_screen(screen, skier, obstacles, scoreFont, score):
        screen.fill(WHITE)
        skier.draw(screen)
        for obstacle in obstacles:
            if not (obstacle.type == 0 and obstacle.passed):
                obstacle.draw(screen)
        drawScore(screen, scoreFont, score)
        pygame.display.update()


def main():
    pygame.init()
    WIDTH = 640
    HEIGHT = 640
    #create a game window with a specific width and height
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    #create a name for the window
    pygame.display.set_caption("skiing")
    #define clock
    clock = pygame.time.Clock()
    #print score
    score = 0
    scoreFont = pygame.font.Font(None, 35)
    show_start_interface(screen, WIDTH)
    obstacles1 = pygame.sprite.Group()
    obstacles2 = create_obstacles(2)
    obstacles = combine_obstacles(obstacles1, obstacles2)
    skier = Skier(WIDTH/2, 100, PLAYER_IMGS)
    distance = 0
    flag = True
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    skier.turn(-1)
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    skier.turn(1)
        skier.move()
        speed = skier.speed[1]
        distance = distance + speed
        if distance>=640 and flag:
            flag = not flag
            obstacles1 = create_obstacles(2)
            obstacles = combine_obstacles(obstacles1, obstacles2)
        if distance>=1280 and not flag:
            flag = not flag
            obstacles2 = create_obstacles(2)
            obstacles = combine_obstacles(obstacles1, obstacles2)
            distance = distance-1280
        for obstacle in obstacles:
            obstacle.move(speed)

        #collision detection
        hit_obstacles = pygame.sprite.spritecollide(skier, obstacles, False)

        # when collisions happen, it will do the following things
        for obstacle in hit_obstacles:

            if obstacle.type == 0 and not obstacle.passed:
                obstacle.passed = True
                score +=10
                obstacles.remove(obstacle)
                redraw_screen(screen, skier, obstacles, scoreFont, score)

            if obstacle.type == 1 and not obstacle.passed:
                obstacle.passed = True
                skier.set_fall() 
                score -=50
                redraw_screen(screen, skier, obstacles, scoreFont, score)
                pygame.time.delay(1000)
                skier.set_forward()
            break

        redraw_screen(screen, skier, obstacles, scoreFont, score)

    pygame.quit()


if __name__=="__main__":
    main()