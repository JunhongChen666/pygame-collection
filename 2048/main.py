import pygame
import sys
import config as cfg
from game import Game_2048
import utils

def main(cfg):
    pygame.init()
    screen = pygame.display.set_mode(cfg.SCREENSIZE)
    pygame.display.set_caption("2048")
    clock = pygame.time.Clock()

    game = Game_2048(cfg.MAX_SCORE_FILEPATH)
    running = True
    while running:
        clock.tick(cfg.FPS)
        screen.fill(cfg.BG_COLOR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()  # release any resources that Pygame has acquired during its initialization
                sys.exit()  # terminate the python code
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                    direction  = {pygame.K_UP: "UP", pygame.K_DOWN: "DOWN", pygame.K_RIGHT: "RIGHT", pygame.K_LEFT: "LEFT"}
                    game.set_direction(direction[event.key])

        if game.is_gameover():
            utils.save_max_score(game.file_path, game.max_score)
            running = False


        utils.drawMatrix(screen, game.game_matrix, cfg)
        start_x, start_y = utils.drawScore(screen, game.score, game.max_score, cfg)
        utils.drawGameIntro(screen, start_x, start_y, cfg)
        game.update()
        pygame.display.update()

    return utils.endInterface(screen, cfg)



if __name__ == '__main__':
    while True:
        if not main(cfg):
            break


