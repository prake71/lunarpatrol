import pygame
import os

class GameTitle(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, gametitle="Lunar Patrol 1"):
        super().__init__()

        self.gametitle = gametitle
        self.screen = screen
        self.image = None
        self.text = None
        self.font = pygame.font.Font(os.path.join('data', 'fonts', 'ARCADECLASSIC.TTF'), 30)

        self.image = self.font.render(self.gametitle, True, [255, 255, 255])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass
    

