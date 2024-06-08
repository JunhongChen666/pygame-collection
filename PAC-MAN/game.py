import pygame, sys
import cfg
from modules import Game
def startGame(screen, game, font1):
    clock = pygame.time.Clock()

    wallGroup = game.setupWalls()
    gateGroup = game.setupGate()
    foodGroup = game.setupFood()
    ghostGroup = game.setupGhosts()
    # ghostGroup = game.setupGhosts()
    player = game.setupPlayer()
    running = True
    score = 0
    win = True
    while running:
        clock.tick(10)
        screen.fill(cfg.BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(-1)
        
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                player.changeDirection([1, 0])
            if keys[pygame.K_LEFT]:
                player.changeDirection([-1, 0])
            if keys[pygame.K_UP]:
                player.changeDirection([0, -1])
            if keys[pygame.K_DOWN]:
                player.changeDirection([0, 1])

        if player.speed!=[0,0]:
            player.move(wallGroup, gateGroup)
            player.speed=[0, 0]
        player.draw(screen)

        for ghost in ghostGroup:
            if ghost.tracks_loc[1] < ghost.tracks[ghost.tracks_loc[0]][2]:
                ghost.changeDirection(ghost.tracks[ghost.tracks_loc[0]][0: 2])
                ghost.tracks_loc[1] += 1
            else:
                if ghost.tracks_loc[0] < len(ghost.tracks) - 1:
                    ghost.tracks_loc[0] += 1
                elif ghost.name == 'Clyde':
                    ghost.tracks_loc[0] = 2
                else:
                    ghost.tracks_loc[0] = 0
                ghost.changeDirection(ghost.tracks[ghost.tracks_loc[0]][0: 2])
                ghost.tracks_loc[1] = 0
            if ghost.tracks_loc[1] < ghost.tracks[ghost.tracks_loc[0]][2]:
                ghost.changeDirection(ghost.tracks[ghost.tracks_loc[0]][0: 2])
            else:
                if ghost.tracks_loc[0] < len(ghost.tracks) - 1:
                    loc0 = ghost.tracks_loc[0] + 1
                elif ghost.name == 'Clyde':
                    loc0 = 2
                else:
                    loc0 = 0
                ghost.changeDirection(ghost.tracks[loc0][0: 2])
            ghost.move(wallGroup, None)
        ghostGroup.draw(screen)
    
        #draw score
        score_text = font1.render("Score: %s" % score, True, cfg.RED)
        screen.blit(score_text, [10, 10])
        
        wallGroup.draw(screen)
        gateGroup.draw(screen)
        foodGroup.draw(screen)
        ghostGroup.draw(screen)

        #True: destroy the food after collided with player
        food_eaten = pygame.sprite.spritecollide(player, foodGroup, True, None)
        #cound the number of food eaten
        if food_eaten:
            score+=1
            if score==210:
                win = True
                break
        collideWithGhost = pygame.sprite.spritecollide(player, ghostGroup, False, None)
        if collideWithGhost:
            win = False
            break
        pygame.display.update()
    return win
        

def showText(screen, font, win):
    clock = pygame.time.Clock()
    msg = 'Game Over!' if not win else 'Congratulations, you won!'
    positions = [[235, 233], [65, 303], [170, 333]] if not win else [[145, 233], [65, 303], [170, 333]]
    surface = pygame.Surface((400, 200))
    surface.set_alpha(10)
    surface.fill((128, 128, 128))
    screen.blit(surface, (100, 200))
    texts = [font.render(msg, True, cfg.WHITE),
            font.render('Press ENTER to continue or play again.', True, cfg.WHITE),
            font.render('Press ESCAPE to quit.', True, cfg.WHITE)]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return True
                elif event.key == pygame.K_ESCAPE:
                    return False
        for idx, (text, position) in enumerate(zip(texts, positions)):
            screen.blit(text, position)
        pygame.display.flip()
        clock.tick(10)

def main():
    pygame.init()
    screen = pygame.display.set_mode(cfg.SCREENSIZE)
    pygame.display.set_caption("PAC-MAN")
    game = Game()
    font1 = pygame.font.Font(None, 25)
    font2 = pygame.font.Font(None, 30)
    running = True
    win = True
    while running:
        win = startGame(screen, game, font1)
        running = showText(screen, font2, win)



    pygame.quit()

if __name__ == '__main__':
    main()