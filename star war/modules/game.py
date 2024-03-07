import config as cfg
import pygame
import sys
from interfaces import show_end_interface, show_start_interface, draw_score
from modules import Ship, Bullet, Asteroid


def show_game_interface(screen, cfg, num_player):
    # import back_ground image
    BG_IMG = pygame.image.load(cfg.IMAGEPATHS['seamless_space']).convert()
    BULLET_IMG = pygame.image.load(cfg.IMAGEPATHS['bullet']).convert_alpha()
    BULLET_IMG = pygame.transform.scale(BULLET_IMG, (10, 10))
    RED_SHIP_IMG = pygame.image.load(cfg.IMAGEPATHS['red_ship']).convert_alpha()
    RED_SHIP_IMG = pygame.transform.scale(RED_SHIP_IMG, (36, 36))
    BLUE_SHIP_IMG = pygame.image.load(cfg.IMAGEPATHS['blue_ship']).convert_alpha()
    BLUE_SHIP_IMG = pygame.transform.scale(BLUE_SHIP_IMG, (36, 36))
    EXPLODE_IMG = pygame.image.load(cfg.IMAGEPATHS['ship_exploded']).convert_alpha()
    ASTEROID_IMG = pygame.image.load(cfg.IMAGEPATHS['asteroid']).convert_alpha()

    # define sprite groups
    player_group = pygame.sprite.Group()
    bullet_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()

    # initialize spaceship
    player_group.add(Ship(RED_SHIP_IMG, EXPLODE_IMG, 1, BULLET_IMG))
    if num_player == 2:
        player_group.add(Ship(BLUE_SHIP_IMG, EXPLODE_IMG, 2, BULLET_IMG))

    bg_move_dis = 0

    #time interval for getnerating asteroids
    asteroid_ticks = 90

    score_1 = 0
    score_2 = 0
    # while loop
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(60)
        screen.blit(BG_IMG, (0, -BG_IMG.get_rect().height + bg_move_dis))
        screen.blit(BG_IMG, (0, bg_move_dis))
        bg_move_dis = (bg_move_dis + 2) % BG_IMG.get_rect().height

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # shuts down all the Pygame modules that have been initialized, release the resources
                pygame.quit()
                # terminate the program immediately
                sys.exit()

        # detect player actions
        keys = pygame.key.get_pressed()
        for idx, player in enumerate(player_group):
            if idx==0:
                if keys[pygame.K_RIGHT]:
                    player.move("RIGHT")
                if keys[pygame.K_LEFT]:
                    player.move("LEFT")
                if keys[pygame.K_UP]:
                    player.move("UP")
                if keys[pygame.K_DOWN]:
                    player.move("DOWN")
                if keys[pygame.K_l] and player.cooling_time==0:
                    bullet = player.shot()
                    bullet_group.add(bullet)
                    player.cooling_time = 20

            if idx==1:
                if keys[pygame.K_d]:
                    player.move("RIGHT")
                if keys[pygame.K_a]:
                    player.move("LEFT")
                if keys[pygame.K_w]:
                    player.move("UP")
                if keys[pygame.K_s]:
                    player.move("DOWN")
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
        if asteroid_ticks==0:
            asteroid_group.add(Asteroid(ASTEROID_IMG))
            asteroid_ticks = 90
        else:
            asteroid_ticks -=1
        for asteroid in asteroid_group:
            asteroid.move()
            asteroid.draw(screen)


        draw_score(screen, score_1, score_2)
        pygame.display.update()


def main():
    pygame.init()
    screen = pygame.display.set_mode(cfg.SCREENSIZE)
    pygame.display.set_caption("star war")
    num_player = show_start_interface(screen, )
    print("num_player", 2)
    running = True
    while running:
        if num_player == 1:
            show_game_interface(screen, cfg, num_player)
        elif num_player == 2:
            show_game_interface(screen, cfg, num_player)

        show_end_interface(screen)


if __name__ == '__main__':
    main()
