import pygame
import os

class PowerUpAmmo(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        super().__init__()

        self.screen = screen

        self.image = pygame.image.load(os.path.join('data', 'images', 'AmmoPowerUp_002.png')).convert()

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = self.y_start = y
        self.image.set_colorkey([0, 0, 0])
        self.rect.inflate_ip(-20, -20)

    def update(self):
        self.rect.y += 1

    def _check_bounds(self):
        if self.rect.y > self.screen.get_height() + self.image.get_height():
            self.rect.y = self.y_start
            self.kill()
