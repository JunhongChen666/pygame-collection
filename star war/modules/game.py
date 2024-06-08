import config as cfg
import pygame
import sys
from interfaces import *
from modules import *


def show_game_interface(screen, game, num_player):
    # import back_ground image
    BG_IMG = pygame.image.load(cfg.IMAGEPATHS['seamless_space']).convert()
    ASTEROID_IMG = pygame.image.load(cfg.IMAGEPATHS['asteroid']).convert_alpha()

    # define sprite groups
    player_group = game.setupPlayerGroup(num_player)
    bullet_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    spawn_asteroid = pygame.USEREVENT+1
    pygame.time.set_timer(spawn_asteroid, 1000)

    bg_move_dis = 0

    score_1 = 0
    score_2 = 0

    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(60)
        #background image animation
        screen.blit(BG_IMG, (0, -BG_IMG.get_rect().height + bg_move_dis))
        screen.blit(BG_IMG, (0, bg_move_dis))
        bg_move_dis = (bg_move_dis + 2) % BG_IMG.get_rect().height

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # shuts down all the Pygame modules that have been initialized, release the resources
                pygame.quit()
                # terminate the program immediately
                sys.exit()
            if event.type == spawn_asteroid:
                asteroid_group.add(Asteroid(ASTEROID_IMG))

        # detect player actions
        keys = pygame.key.get_pressed()
        for player in player_group:
            if player.player_id==1:
                if keys[pygame.K_RIGHT]:
                    player.changeDirection([1, 0])
                if keys[pygame.K_LEFT]:
                    player.changeDirection([-1, 0])
                if keys[pygame.K_UP]:
                    player.changeDirection([0, 1])
                if keys[pygame.K_DOWN]:
                    player.changeDirection([0, -1])
                player.move()
                player.changeDirection([0, 0])
                if keys[pygame.K_l] and player.cooling_time==0:
                    bullet = player.shot()
                    bullet_group.add(bullet)
                    player.cooling_time = 20
            if player.player_id==2:
                if keys[pygame.K_d]:
                    player.changeDirection([1, 0])
                if keys[pygame.K_a]:
                    player.changeDirection([-1, 0])
                if keys[pygame.K_w]:
                    player.changeDirection([0, 1])
                if keys[pygame.K_s]:
                    player.changeDirection([0, -1])
                player.move()
                player.changeDirection([0, 0])
                if keys[pygame.K_SPACE] and player.cooling_time==0:
                    bullet = player.shot()
                    bullet_group.add(bullet)
                    player.cooling_time = 20

            if player.cooling_time > 0:
                player.cooling_time -= 1

        #deal with ships
        for player in player_group:
            if pygame.sprite.spritecollide(player, asteroid_group, True, None):
                player.explode_step =1
            elif player.explode_step > 0:
                if player.explode_step <= 3:
                    player.explode(screen)
                else:
                    player_group.remove(player)
                    if len(player_group)==0:
                        return
            else:
                player.draw(screen)


        #deal with bullets
        for bullet in bullet_group:
            bullet.move()
            if pygame.sprite.spritecollide(bullet, asteroid_group, True, None):
                bullet_group.remove(bullet)
                if bullet.player_id == 1:
                    score_1 += 1
                else:
                    score_2 += 1
            bullet.draw(screen)

        #deal with asteriods
        for asteroid in asteroid_group:
            asteroid.move()
            asteroid.draw(screen)


        draw_score(screen, score_1, score_2)
        pygame.display.update()

def main():
    pygame.init()
    screen = pygame.display.set_mode(cfg.SCREENSIZE)
    pygame.display.set_caption("star war")
    num_player = show_start_interface(screen)
    game = Game()
    running = True
    while running:
        if num_player == 1:
            show_game_interface(screen, game, num_player)
        elif num_player == 2:
            show_game_interface(screen, game, num_player)

        running = show_end_interface(screen)
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
