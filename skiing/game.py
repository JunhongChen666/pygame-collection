import pygame
import os

pygame.init()
WIDTH = 640
HEIGHT = 640
#create a game window with a specific width and height
screen = pygame.display.set_mode((WIDTH, HEIGHT))
#create a name for the window
pygame.display.set_caption("skiing")
#define clock
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (68, 93, 72)
BLUE = (100, 153, 233)

PLAYER_IMG_1 = pygame.image.load(os.path.join(os.getcwd(), 'images/skier_forward.png'))
PLAYER_IMG_2 = pygame.image.load(os.path.join(os.getcwd(), 'images/skier_right1.png'))
PLAYER_IMG_3 = pygame.image.load(os.path.join(os.getcwd(), 'images/skier_right2.png'))
PLAYER_IMG_4 = pygame.image.load(os.path.join(os.getcwd(), 'images/skier_fall.png'))
PLAYER_IMG_5 = pygame.image.load(os.path.join(os.getcwd(), 'images/skier_left2.png'))
PLAYER_IMG_6 = pygame.image.load(os.path.join(os.getcwd(), 'images/skier_left1.png'))
PLAYER_IMGS = [PLAYER_IMG_1,PLAYER_IMG_2,PLAYER_IMG_3,PLAYER_IMG_4,PLAYER_IMG_5,PLAYER_IMG_6]

TREE_IMG = pygame.image.load(os.path.join(os.getcwd(), 'images/tree.png'))
FLAG_IMG = pygame.image.load(os.path.join(os.getcwd(), 'images/flag.png'))

#print score
score = 0
scoreFont = pygame.font.Font(None, 50)
def drawScore(score):
    score = str(score)
    score_text = scoreFont.render(score, True, BLACK, WHITE)
    screen.blit(score_text, (0, 15))

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

    
    def set_forward(self):
        self.image = self.images[0]
        self.direction = 0
        self.speed = [self.direction, 6-abs(self.direction)*2]

    def draw(self):
        screen.blit(self.image, self.rect)

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, image, type):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center = (x, y))
        self.type = type
    

    def move(self, speed):
        self.rect.centery = self.rect.centery-speed

    def draw(self):
        screen.blit(self.image, self.rect)

def create_obstacles():
    obstacles = pygame.sprite.Group()
    obstacle = Obstacle(WIDTH/2, HEIGHT, TREE_IMG, "tree")
    obstacles.add(obstacle)
    return obstacles



    
        


'''
start interface
'''
def show_start_interface():
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


show_start_interface()
obstacles = create_obstacles()
skier = Skier(WIDTH/2, 100, PLAYER_IMGS)
distance = 0
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
    screen.fill(WHITE)
    skier.move()
    skier.draw()
    speed = skier.speed[1]
    print(speed)
    for obstacle in obstacles:
        obstacle.move(speed)
        obstacle.draw()




    
    drawScore(score)
    pygame.display.update()

pygame.quit()