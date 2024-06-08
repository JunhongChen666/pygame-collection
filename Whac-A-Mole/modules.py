import pygame
import config

class Game:
    def __init__(self):
          pass
    def setupHammer(self):
        pos = pygame.mouse.get_pos()
        hammer = Hammer(pos)
        return hammer
    def setupMole(self):
        mole = Mole()
        return mole

class Hammer(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.images = [pygame.image.load(config.HAMMER_IMAGEPATHS[0]), pygame.image.load(config.HAMMER_IMAGEPATHS[1])]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.isHitting = False

        self.coolDownTime = 4
        self.count = 0
    def setPosition(self, position):
        self.rect.center = position

    def hit(self):
        self.isHitting = True
    
    def draw(self, screen):
        if not self.isHitting:
            self.image = self.images[0]
        else:
            self.image = self.images[1]
            self.count+=1
            if self.count>=self.coolDownTime:
                self.isHitting = False
                self.count = 0
        screen.blit(self.image, self.rect)


class Mole(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = [pygame.transform.scale(pygame.image.load(config.MOLE_IMAGEPATHS[0]), (101, 103)),
                       pygame.transform.scale(pygame.image.load(config.MOLE_IMAGEPATHS[1]), (101, 103))]
        self.image = self.images[0]

        self.rect = self.image.get_rect()
        self.isHit = False

    def getHit(self):
        self.isHit = True

    def setPosition(self, position):
        self.rect.left, self.rect.top = position

    def draw(self, screen):
        if not self.isHit:
            self.image = self.images[0]
        else:
            self.image = self.images[1]

        screen.blit(self.image, self.rect)
            
    def reset(self, position):
        self.isHit = False
        self.setPosition(position)