import pygame
import random
import os
from load import IMAGE_PATHS, BGM_PATH, GET_PATH, GOLD_IMG_PATH, BLACK, RED, WHITE
from Player import Player
from Coin import Coin

def load_resources():
    #load the bgm
    pygame.mixer.music.load(BGM_PATH)
    #turn down the volume of the bgm
    pygame.mixer.music.set_volume(0.1)
    # let the bgm plays forever
    pygame.mixer.music.play(-1)

    #load the sound effect
    get_sound = pygame.mixer.Sound(GET_PATH)
    #turn down the volume of the sound effect
    get_sound.set_volume(0.1)

    #images
    IMAGES = [pygame.image.load(path) for path in IMAGE_PATHS]
    GOLD_IMG = pygame.image.load(GOLD_IMG_PATH)
    return get_sound, IMAGES, GOLD_IMG

def drawCountdown(countdownFont, screen):
    text = "Count down: " + str((60000 - pygame.time.get_ticks())//60000) + \
        ":"+str((60000-pygame.time.get_ticks()) // 1000 % 60).zfill(2)
    text = countdownFont.render(text, True, RED, BLACK)
    screen.blit(text, (0, 0))

def drawScore(scoreFont, score, screen):
    # str() will turn an integer into a string variable
    score = str(score)
    score = scoreFont.render(score, True, WHITE, BLACK)
    screen.blit(score, (0, 15))

'''
create end interface
'''
def show_end_interface(screen, score, WIDTH, HEIGHT):
    BLACK
    end_font = pygame.font.Font(None, 200)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.fill(BLACK)
        text = end_font.render(str(score), True, WHITE, BLACK)
        text_rect = text.get_rect(center = (WIDTH//2, HEIGHT//2)) 
        screen.blit(text, text_rect)
        pygame.display.update()

def main():
    BLACK = (0, 0, 0)
    MAXLOOPCOUNT = 20

    pygame.init()
    WIDTH = 800
    HEIGHT = 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("catch coins")
    clock = pygame.time.Clock()
    get_sound, IMAGES, GOLD_IMG = load_resources()

    scoreFont = pygame.font.Font(None, 50)
    countdownFont = pygame.font.Font(None, 30)

    player = Player(WIDTH/2, HEIGHT-40, 10, IMAGES)
    coins = pygame.sprite.Group()

    loopcount = 0
    score = 0
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(BLACK)

        # in every iteration, loopcount will increase by 1
        loopcount = loopcount + 1
        if loopcount >= MAXLOOPCOUNT:
            # create a food object
            coin = Coin(random.randint(0, WIDTH),
                        10, 3, GOLD_IMG)
            coins.add(coin)
            loopcount = 0
        for coin in coins:
            coin.draw(screen)
            if coin.update(HEIGHT):
                coins.remove(coin)

        # True means after collision, objects in the group will be destroyed
        collisions = pygame.sprite.spritecollide(player, coins, True)

        # when collisions happen, it will do the following things
        for collision in collisions:
            score = score + 1
            get_sound.play()

        #timer
        if pygame.time.get_ticks() >= 60000:
            break

        drawCountdown(countdownFont,screen)
        drawScore(scoreFont, score, screen)
        # 4. call the player's update() function
        player.update(WIDTH)
        player.draw(screen)
        pygame.display.update()

    show_end_interface(screen, score, WIDTH, HEIGHT)

if __name__ == "__main__":
    main()
    






