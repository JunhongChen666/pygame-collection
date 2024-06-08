import pygame
import random
import cfg
class Game():
    def __init__(self):
        pass
    def setupWalls(self):
        self.wallGroup = pygame.sprite.Group()
        wallPositions = [
            [0, 0, 6, 600], [0, 0, 600, 6], [0, 600, 606, 6], [600, 0, 6, 606], [300, 0, 6, 66], [60, 60, 186, 6],
            [360, 60, 186, 6], [60, 120, 66, 6], [60, 120, 6, 126], [180, 120, 246, 6], [300, 120, 6, 66],
            [480, 120, 66, 6], [540, 120, 6, 126], [120, 180, 126, 6], [120, 180, 6, 126], [360, 180, 126, 6],
            [480, 180, 6, 126], [180, 240, 6, 126], [180, 360, 246, 6], [420, 240, 6, 126], [240, 240, 42, 6],
            [324, 240, 42, 6], [240, 240, 6, 66], [240, 300, 126, 6], [360, 240, 6, 66], [0, 300, 66, 6],
            [540, 300, 66, 6], [60, 360, 66, 6], [60, 360, 6, 186], [480, 360, 66, 6], [540, 360, 6, 186],
            [120, 420, 366, 6], [120, 420, 6, 66], [480, 420, 6, 66], [180, 480, 246, 6], [300, 480, 6, 66],
            [120, 540, 126, 6], [360, 540, 126, 6]
        ]
        for wallPosition in wallPositions:
            wall = Wall(*wallPosition, cfg.SKYBLUE)
            self.wallGroup.add(wall)
        return self.wallGroup
    
    def setupGate(self):
        self.gateGroup = pygame.sprite.Group()
        gate_position = [282, 242, 42, 2]
        gate = Wall(*gate_position, cfg.WHITE)
        self.gateGroup.add(gate)
        return self.gateGroup
    
    def setupFood(self):
        self.foodGroup = pygame.sprite.Group()
        for row in range(19):
            for col in range(19):
                if (row == 7 or row == 8) and (col == 8 or col == 9 or col == 10):
                    continue
                else:
                    food = Food(30 * col + 32, 30 * row + 32, 4, cfg.YELLOW)
                    if pygame.sprite.spritecollide(food, self.wallGroup, False):
                        continue
                self.foodGroup.add(food)
        return self.foodGroup
    
    def setupPlayer(self):
        self.playerGroup = pygame.sprite.Group()
        PLAYERIMG = pygame.image.load(cfg.HEROPATH)
        player = Player(287, 439, PLAYERIMG)
        return player
    
    def setupGhosts(self):
        self.ghostGroup = pygame.sprite.Group()
        BlinkyIMG = pygame.image.load(cfg.BlinkyPATH)
        ClydeIMG = pygame.image.load(cfg.ClydePATH)
        InkyIMG = pygame.image.load(cfg.InkyPATH)
        PinkyIMG = pygame.image.load(cfg.PinkyPATH)
        blinky = Ghost(287, 199, BlinkyIMG, "Blinky")
        blinky.tracks = [
                    [0, -0.5, 4], [0.5, 0, 9], [0, 0.5, 11], [0.5, 0, 3], [0, 0.5, 7], [-0.5, 0, 11], [0, 0.5, 3],
                    [0.5, 0, 15], [0, -0.5, 15], [0.5, 0, 3], [0, -0.5, 11], [-0.5, 0, 3], [0, -0.5, 11], [-0.5, 0, 3],
                    [0, -0.5, 3], [-0.5, 0, 7], [0, -0.5, 3], [0.5, 0, 15], [0, 0.5, 15], [-0.5, 0, 3], [0, 0.5, 3],
                    [-0.5, 0, 3], [0, -0.5, 7], [-0.5, 0, 3], [0, 0.5, 7], [-0.5, 0, 11], [0, -0.5, 7], [0.5, 0, 5]
                ]
        self.ghostGroup.add(blinky)
        clyde = Ghost(319, 259, ClydeIMG, "Clyde")
        clyde.tracks = [
                    [-1, 0, 2], [0, -0.5, 4], [0.5, 0, 5], [0, 0.5, 7], [-0.5, 0, 11], [0, -0.5, 7],
                    [-0.5, 0, 3], [0, 0.5, 7], [-0.5, 0, 7], [0, 0.5, 15], [0.5, 0, 15], [0, -0.5, 3],
                    [-0.5, 0, 11], [0, -0.5, 7], [0.5, 0, 3], [0, -0.5, 11], [0.5, 0, 9]
                ]
        self.ghostGroup.add(clyde)
        inky = Ghost(255, 259, InkyIMG, "Inky")
        inky.tracks = [
                    [1, 0, 2], [0, -0.5, 4], [0.5, 0, 10], [0, 0.5, 7], [0.5, 0, 3], [0, -0.5, 3],
                    [0.5, 0, 3], [0, -0.5, 15], [-0.5, 0, 15], [0, 0.5, 3], [0.5, 0, 15], [0, 0.5, 11],
                    [-0.5, 0, 3], [0, -0.5, 7], [-0.5, 0, 11], [0, 0.5, 3], [-0.5, 0, 11], [0, 0.5, 7],
                    [-0.5, 0, 3], [0, -0.5, 3], [-0.5, 0, 3], [0, -0.5, 15], [0.5, 0, 15], [0, 0.5, 3],
                    [-0.5, 0, 15], [0, 0.5, 11], [0.5, 0, 3], [0, -0.5, 11], [0.5, 0, 11], [0, 0.5, 3], [0.5, 0, 1]
                ]
        self.ghostGroup.add(inky)
        pinky = Ghost(287, 259, PinkyIMG, "Pinky")
        pinky.tracks = [
                    [0, -1, 4], [0.5, 0, 9], [0, 0.5, 11], [-0.5, 0, 23], [0, 0.5, 7], [0.5, 0, 3],
                    [0, -0.5, 3], [0.5, 0, 19], [0, 0.5, 3], [0.5, 0, 3], [0, 0.5, 3], [0.5, 0, 3],
                    [0, -0.5, 15], [-0.5, 0, 7], [0, 0.5, 3], [-0.5, 0, 19], [0, -0.5, 11], [0.5, 0, 9]
                ]
        self.ghostGroup.add(pinky)
        return self.ghostGroup



'''Walls are rectangles'''
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y

class Food(pygame.sprite.Sprite):
    def __init__(self, x, y, length, color):
        super().__init__()
        self.image = pygame.Surface([length, length])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        #set the image and initial position of the player
        self.image = image
        #for flipping
        self.base_image = self.image
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y

        self.base_speed = 30
        #speed x, speed y
        self.speed = [0, 0]

    def changeDirection(self, direction):
        
        self.speed = [direction[0] * self.base_speed, direction[1] * self.base_speed]
        if direction[0]==1:
            self.image = self.base_image.copy()
        elif direction[0]==-1:
            #horizontally
            self.image = pygame.transform.flip(self.base_image, True, False)
            # #vertivally
            # self.image = pygame.transform.flip(self.base_image, False, True)
        elif direction[1]==1:
            self.image = pygame.transform.rotate(self.base_image, -90)
        elif direction[1]==-1:
            self.image = pygame.transform.rotate(self.base_image, 90)
    
    def move(self, wallGroup, gateGroup):
        old_x = self.rect.left
        old_y = self.rect.top
        self.rect.left = self.rect.left + self.speed[0]
        self.rect.top = self.rect.top + self.speed[1]

        isCollideWithWall = pygame.sprite.spritecollide(self, wallGroup, False)
        isCollideWithGate = pygame.sprite.spritecollide(self, gateGroup, False)
        if isCollideWithWall or isCollideWithGate:
            self.rect.left = old_x
            self.rect.top = old_y

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Ghost(pygame.sprite.Sprite):
    def __init__(self, x, y, image, name):
        super().__init__()
        #set the image and initial position of the player
        self.image = image
        #for flipping
        self.base_image = self.image
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y

        self.base_speed = 30
        #speed x, speed y
        self.speed = [0, 0]

        self.tracks = []
        self.tracks_loc = [0, 0]
        self.name = name

    def changeDirection(self, direction):
        
        self.speed = [direction[0] * self.base_speed, direction[1] * self.base_speed]
        if direction[0]==1:
            self.image = self.base_image.copy()
        elif direction[0]==-1:
            #horizontally
            self.image = pygame.transform.flip(self.base_image, True, False)
            # #vertivally
            # self.image = pygame.transform.flip(self.base_image, False, True)
        elif direction[1]==1:
            self.image = pygame.transform.rotate(self.base_image, -90)
        elif direction[1]==-1:
            self.image = pygame.transform.rotate(self.base_image, 90)
    
    def move(self, wallGroup, gateGroup):
        old_x = self.rect.left
        old_y = self.rect.top
        self.rect.left = self.rect.left + self.speed[0]
        self.rect.top = self.rect.top + self.speed[1]

        isCollideWithWall = pygame.sprite.spritecollide(self, wallGroup, False)
        if isCollideWithWall:
            self.rect.left = old_x
            self.rect.top = old_y

    def draw(self, screen):
        screen.blit(self.image, self.rect)    


