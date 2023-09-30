import pygame

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, image):
        super().__init__()
        self.speed = speed

        self.image = image
        self.rect = self.image.get_rect(center=(x, y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, HEIGHT):
        self.rect.y = self.rect.y + self.speed
        return self.rect.y>=HEIGHT
