import pygame, sys
import config

class Button:
    def __init__(self, screen, colour, text, size ):

        self.rect = pygame.Rect((0, 0), size)
        self.rect.center = (993/2, 477/2)
        pygame.draw.rect(screen, colour, self.rect)

        font = pygame.font.Font(config.FONT_PATH, 70)
        content = font.render(text, True, config.WHITE)
        text_rect = content.get_rect()
        text_rect.center = (993/2, 477/2)
        screen.blit(content, text_rect)

    def click(self, position):
        #if will detect if the position is inside a rectangle, if the position is inside the rectangle, returns True. Otherwise, returns false
        return self.rect.collidepoint(position)

def showStartInterface(screen):

    clock = pygame.time.Clock()
    BGIMG = pygame.image.load(config.GAME_BG_IMAGEPATH)
    while True:
        clock.tick(10)
        screen.blit(BGIMG, (0, 0))
        button = Button(screen, config.BROWN, "Start", (300, 100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                 if button.click(pygame.mouse.get_pos()):
                      return
        pygame.display.update()

def showEndInterface(screen):
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(True)
    BGIMG = pygame.image.load(config.GAME_BG_IMAGEPATH)
    while True:
        clock.tick(10)
        screen.blit(BGIMG, (0, 0))
        button = Button(screen, config.BROWN, "Restart", (300, 100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                 if button.click(pygame.mouse.get_pos()):
                      return True
        pygame.display.update()