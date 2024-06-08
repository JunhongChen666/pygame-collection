import config
import pygame
import sys
import random
from modules import *
from interfaces import *

def startGame(screen, game, font):
    #hide mouse
    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()
    BGIMG = pygame.image.load(config.GAME_BG_IMAGEPATH)
    hammer = game.setupHammer()
    mole = game.setupMole()
    mole.reset(random.choice(config.HOLE_POSITIONS))

    change_hole_event = pygame.USEREVENT+1
    flag = False

    init_time = pygame.time.get_ticks()
    pygame.time.set_timer(change_hole_event, 800)
    score = 0
    time_remain = 0
    while True:
        clock.tick(30)
        time_remain = round((1000 - (pygame.time.get_ticks() - init_time)) / 1000.)
        screen.blit(BGIMG, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                 hammer.hit()
            if event.type == change_hole_event:
                hole_pos = random.choice(config.HOLE_POSITIONS)
                mole.reset(hole_pos)
        #adjust the spawn speed
        if 20 < time_remain and time_remain <= 40 and not flag:
            pygame.time.set_timer(change_hole_event, 650)
            flag = True
        elif 0 < time_remain and time_remain<=20 and flag:
            pygame.time.set_timer(change_hole_event, 500)
            flag = False
        
        #mole
        if hammer.isHitting and not mole.isHit:
            isCollided = pygame.sprite.collide_mask(hammer, mole)
            if isCollided:
                score+=10
                mole.getHit()
        mole.draw(screen)


        #hammer
        pos = pygame.mouse.get_pos()
        hammer.setPosition(pos)
        hammer.draw(screen)

        #draw score and text
        score_text = font.render('Score: '+str(score), True, config.WHITE)
        count_down_text = font.render('Time: '+str(time_remain), True, config.WHITE)
        screen.blit(count_down_text, (875, 8))
        screen.blit(score_text, (875, 50))

        if time_remain < 0: 
            break
        pygame.display.update()

def main():
    pygame.init()
    screen = pygame.display.set_mode(config.SCREENSIZE)
    pygame.display.set_caption("Whac-A-Mole")
    game = Game()
    font = pygame.font.Font(config.FONT_PATH, 40)
    showStartInterface(screen)
    running = True
    while running:
        startGame(screen, game, font)
        running = showEndInterface(screen)

    pygame.quit()
    sys.exit()

main()
