import random

import config as cfg
import pygame

class Game:
    def setupPlayerGroup(self, num_player):
        BULLET_IMG = pygame.image.load(cfg.IMAGEPATHS['bullet']).convert_alpha()
        BULLET_IMG = pygame.transform.scale(BULLET_IMG, (10, 10))
        RED_SHIP_IMG = pygame.image.load(cfg.IMAGEPATHS['red_ship']).convert_alpha()
        RED_SHIP_IMG = pygame.transform.scale(RED_SHIP_IMG, (36, 36))
        BLUE_SHIP_IMG = pygame.image.load(cfg.IMAGEPATHS['blue_ship']).convert_alpha()
        BLUE_SHIP_IMG = pygame.transform.scale(BLUE_SHIP_IMG, (36, 36))
        EXPLODE_IMG = pygame.image.load(cfg.IMAGEPATHS['ship_exploded']).convert_alpha()
        
        # initialize spaceship
        player_group = pygame.sprite.Group()
        player_group.add(Ship(RED_SHIP_IMG, EXPLODE_IMG, 1, BULLET_IMG))
        if num_player == 2:
            player_group.add(Ship(BLUE_SHIP_IMG, EXPLODE_IMG, 2, BULLET_IMG))
        return player_group 


class Ship(pygame.sprite.Sprite):
    def __init__(self, image, explode_image, id, bullet_image):
        super().__init__()
        # image
        self.image = image
        self.explode_image = explode_image
        self.bullet_image = bullet_image
        # position
        self.rect = self.image.get_rect()
        self.rect.center = [random.randrange(18, 938), 500]
        #speed
        self.base_speed = (10, 5)
        self.speed = (0, 0)
        #player id
        self.player_id = id
        # shot cooldown time
        self.cooling_time = 0

        self.explode_step = 0

    def shot(self):
        bullet = Bullet(self.bullet_image, (self.rect.centerx, self.rect.centery - 8), self.player_id)
        return bullet

    def changeDirection(self, direction):
        self.speed = (direction[0] * self.base_speed[0], direction[1] * self.base_speed[1])

    def move(self):

        old_centerx = self.rect.centerx
        old_centery = self.rect.centery

        self.rect.centerx = self.rect.centerx + self.speed[0]
        self.rect.centery = self.rect.centery + self.speed[1]

        if self.rect.centerx < 18 or 938 < self.rect.centerx:
            self.rect.centerx = old_centerx
        if self.rect.centery < 18 or 520 < self.rect.centery:
            self.rect.centery = old_centery

    def explode(self, screen):
        #get the portion of the image
        img = self.explode_image.subsurface((48 * (self.explode_step - 1), 0), (48, 48))
        rect = img.get_rect()
        rect.center = self.rect.center
        screen.blit(img, rect)
        self.explode_step+=1

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, position, player_id):
        super().__init__()
        # image, rect, position, speed
        self.image = image

        self.rect = self.image.get_rect()
        self.rect.center = [position[0], position[1]]
        self.speed = 8
        self.player_id = player_id

    def move(self):
        self.rect.centery = self.rect.centery - self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = [random.randrange(20, cfg.SCREENSIZE[0] - 20), -64]
        self.speed = random.randrange(3, 9)

    def move(self):
        self.rect.centery = self.rect.centery + self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)
