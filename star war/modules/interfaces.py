import pygame, sys
import config as cfg

class Button:
    def __init__(self, screen, position, text):
        self.position = position
        size = (310, 65)
        self.rect = pygame.Rect(position, size)
        pygame.draw.rect(screen, (150, 150, 150), self.rect)

        font = pygame.font.Font(cfg.FONTPATH, 50)
        content = font.render(text, True, (255, 0, 0))
        text_rect = content.get_rect()
        text_rect.center = self.rect.center
        screen.blit(content, text_rect)

    def is_clicked(self, position):
        return self.rect.collidepoint(position)


def show_start_interface(screen):
    clock = pygame.time.Clock()
    BG_IMG = pygame.image.load(cfg.IMAGEPATHS['seamless_space']).convert()
    while True:
        clock.tick(10)
        screen.blit(BG_IMG,(0,0))
        button_1 = Button(screen, (330, 190), "1-Player")
        button_2 = Button(screen, (330, 305), "2-Player")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_1.is_clicked(pygame.mouse.get_pos()):
                    return 1
                elif button_2.is_clicked(pygame.mouse.get_pos()):
                    return 2
                
        pygame.display.update()



def show_end_interface(screen):
    clock = pygame.time.Clock()
    BG_IMG = pygame.image.load(cfg.IMAGEPATHS['seamless_space']).convert()
    while True:
        clock.tick(10)
        screen.blit(BG_IMG, (0, 0))
        button_1 = Button(screen, (330, 190), "Restart")
        button_2 = Button(screen, (330, 305), "Quit")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_1.is_clicked(pygame.mouse.get_pos()):
                    return
                elif button_2.is_clicked(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def draw_score(screen, score_1, score_2):
    font = pygame.font.Font(None, 20)
    score_1_text = f"player1 score: {score_1}"
    score_2_text = f"player2 score: {score_2}"
    text_1 = font.render(score_1_text, True, (97, 150, 166))
    text_2 = font.render(score_2_text, True, (255, 0, 0))
    screen.blit(text_1, (2, 5))
    screen.blit(text_2, (2, 35))