import random

import config as cfg
import pygame


class Ship(pygame.sprite.Sprite):
    def __init__(self, image, explode_image, id, bullet_image):
        super().__init__()
        # image
        self.image = image
        self.explode_image = explode_image
        self.bullet_image = bullet_image
        # position
        self.rect = self.image.get_rect()
        self.rect.center = [random.randrange(18, 938), random.randrange(18, 520)]
        #speed
        self.speed = [10, 5]
        #player id
        self.player_id = id
        # shot cooldown time
        self.cooling_time = 0

        self.explode_step = 0

    def shot(self):
        bullet = Bullet(self.bullet_image, (self.rect.centerx, self.rect.centery - 8), self.player_id)
        return bullet

    def move(self, direction):
        if direction == 'LEFT':
            self.rect.centerx = max(self.rect.centerx - self.speed[0], 18)
        elif direction == 'RIGHT':
            self.rect.centerx = min(self.rect.centerx + self.speed[0], 938)
        elif direction == 'UP':
            self.rect.centery = max(self.rect.centery - self.speed[0], 18)
        elif direction == 'DOWN':
            self.rect.centery = min(self.rect.centery + self.speed[0], 520)


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
