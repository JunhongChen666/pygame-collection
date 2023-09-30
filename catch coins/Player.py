import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, images):
        # super represents the Sprite class
        super().__init__()
        self.speed = speed
        # use the image as the surface
        self.images = images
        self.image = images[0]
        #separate images into two parts
        self.images_right = images[:5]
        self.images_left = images[5:]

        # self.switch_count = 0
        # self.switch_count_max = 3
        self.image_index = 0


        # get the rectangular bounding box fo the surface, put the center of the image to (x, y)
        self.rect = self.image.get_rect(center=(x, y))

    def draw(self, screen):
        # draw an image on the screen
        screen.blit(self.image, self.rect)

# increase the x position of the game object
    def move_right(self, WIDTH):
        self.images = self.images_right
        #do something to change the index so that I can get different images using that index.
        self.image_index = (self.image_index+1) % len(self.images)
        self.image = self.images[self.image_index]

        self.rect.centerx = min(self.rect.centerx + self.speed, WIDTH- self.rect.width/2)
# decrease the x position of the game object

    def move_left(self):
        self.images = self.images_left
        #do something to change the index so that I can get different images using that index.
        self.image_index = (self.image_index+1) % len(self.images)
        self.image = self.images[self.image_index]
        self.rect.centerx = max(self.rect.centerx - self.speed, self.rect.width/2)

# detect the keyboard is pressed can call the move_right() or the move_left() function.
    def update(self, WIDTH):
        # 1. capture the keys that is being pressed
        keys = pygame.key.get_pressed()
        # 2. if the right-arrow key is pressed, call the move_right() function
        if keys[pygame.K_RIGHT]:
            self.move_right(WIDTH)
        # 3. if the left-arrow key is pressed, call the move_left() function
        if keys[pygame.K_LEFT]:
            self.move_left()