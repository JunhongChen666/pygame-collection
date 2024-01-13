import pygame
import config as cfg

def getColorByNumber(number):
    number2color_dict = {
        2: ['#eee4da', '#776e65'], 4: ['#ede0c8', '#776e65'], 8: ['#f2b179', '#f9f6f2'],
        16: ['#f59563', '#f9f6f2'], 32: ['#f67c5f', '#f9f6f2'], 64: ['#f65e3b', '#f9f6f2'],
        128: ['#edcf72', '#f9f6f2'], 256: ['#edcc61', '#f9f6f2'], 512: ['#edc850', '#f9f6f2'],
        1024: ['#edc53f', '#f9f6f2'], 2048: ['#edc22e', '#f9f6f2'], 4096: ['#eee4da', '#776e65'],
        8192: ['#edc22e', '#f9f6f2'], 16384: ['#f2b179', '#776e65'], 32768: ['#f59563', '#776e65'],
        65536: ['#f67c5f', '#f9f6f2'], 'null': ['#9e948a', None]
    }
    return number2color_dict[number]


def drawMatrix(screen, game_matrix, cfg):
    for i in range(len(game_matrix)):
        for j in range(len(game_matrix[0])):
            number = game_matrix[i][j]
            x = cfg.MARGIN_SIZE * (j + 1) + cfg.BLOCK_SIZE * j
            y = cfg.MARGIN_SIZE * (i + 1) + cfg.BLOCK_SIZE * i
            # create rectangle (screen, rect_colour, (rect_x, rect_y, rect_width, rect_height))
            pygame.draw.rect(screen, getColorByNumber(number)[0], (x, y, cfg.BLOCK_SIZE, cfg.BLOCK_SIZE))
            # draw text
            if number != 'null':
                font_color = getColorByNumber(number)[1]
                font_size = cfg.BLOCK_SIZE - 10 * len(str(number))
                font = pygame.font.Font(cfg.FONTPATH, font_size)
                text = font.render(str(number), True, font_color)
                text_rect = text.get_rect()
                text_rect.centerx, text_rect.centery = x + cfg.BLOCK_SIZE / 2, y + cfg.BLOCK_SIZE / 2
                screen.blit(text, text_rect)


def drawScore(screen, score, max_score, cfg):
    font_color = (255, 255, 255)
    font_size = 30
    font = pygame.font.Font(cfg.FONTPATH, font_size)
    text_max_score = font.render('Best: %s' % max_score, True, font_color)
    text_score = font.render('Score: %s' % score, True, font_color)
    start_x = cfg.BLOCK_SIZE * cfg.GAME_MATRIX_SIZE[1] + cfg.MARGIN_SIZE * (cfg.GAME_MATRIX_SIZE[1] + 1)
    screen.blit(text_max_score, (start_x+10, 10))
    screen.blit(text_score, (start_x+10, 20+text_score.get_rect().height))
    start_y = 30 + text_score.get_rect().height + text_max_score.get_rect().height
    return (start_x, start_y)

def drawGameIntro(screen, start_x, start_y, cfg):
    start_y += 40
    font_color = (255, 255, 255)
    font_size_big = 30
    font_size_small = 20
    font_big = pygame.font.Font(cfg.FONTPATH, font_size_big)
    font_small = pygame.font.Font(cfg.FONTPATH, font_size_small)
    intros = ['TIPS:', 'Use arrow keys to move the number blocks.', 'Adjacent blocks with the same number will', 'be merged. Just try to merge the blocks as', 'many as you can!']
    for idx, intro in enumerate(intros):
        font = font_big if idx == 0 else font_small
        text = font.render(intro, True, font_color)
        screen.blit(text, (start_x+10, start_y))
        start_y += text.get_rect().height + 10


def save_max_score(file_path, score):
    try:
        with open(file_path, "w") as file:
            file.write(str(score))
    except IOError as e:
        print(f"an error occur: {e}")

def read_max_score(file_path):
    try:
        with open(file_path, "r") as file:
            max_score = file.readline()
            return int(max_score)
    except FileNotFoundError as e:
        print(f"The file was not found: {e}")
    except IOError as e:
        print(f"An error occurred: {e}")

def endInterface(screen, cfg):
    print("end")
    font_size_big = 60
    font_size_small = 30
    font_color = (255, 255, 255)
    font_big = pygame.font.Font(cfg.FONTPATH, font_size_big)
    font_small = pygame.font.Font(cfg.FONTPATH, font_size_small)

    surface = screen
    surface.fill((127, 255, 212, 2))

    text = font_big.render('Game Over!', True, font_color)
    text_rect = text.get_rect()
    text_rect.centerx, text_rect.centery = cfg.SCREENSIZE[0]/2, cfg.SCREENSIZE[1]/2-50
    surface.blit(text, text_rect)

    button_width, button_height = 100, 40
    button_start_x_left = cfg.SCREENSIZE[0] / 2 - button_width - 20
    button_start_x_right = cfg.SCREENSIZE[0] / 2 + 20
    button_start_y = cfg.SCREENSIZE[1] / 2 - button_height / 2 + 20
    pygame.draw.rect(surface, (0, 255, 255), (button_start_x_left, button_start_y, button_width, button_height))

    text_restart = font_small.render('Restart', True, font_color)
    text_restart_rect = text_restart.get_rect()
    text_restart_rect.centerx, text_restart_rect.centery = button_start_x_left + button_width / 2, button_start_y + button_height / 2
    surface.blit(text_restart, text_restart_rect)

    pygame.draw.rect(surface, (0, 255, 255), (button_start_x_right, button_start_y, button_width, button_height))

    text_quit = font_small.render('Quit', True, font_color)
    text_quit_rect = text_quit.get_rect()
    text_quit_rect.centerx, text_quit_rect.centery = button_start_x_right + button_width / 2, button_start_y + button_height / 2
    surface.blit(text_quit, text_quit_rect)

    while True:
        screen.blit(surface, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button:
                if text_quit_rect.collidepoint(pygame.mouse.get_pos()):
                    return False
                if text_restart_rect.collidepoint(pygame.mouse.get_pos()):
                    return True
        pygame.display.update()


