import pygame
import os

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