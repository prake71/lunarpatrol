import pygame
import os

class Pirate(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        super().__init__()

        self.screen = screen
        self.image_03 = pygame.image.load(os.path.join('data', 'images', 'PirateShip_03_001.png')).convert()
        self.image_09 = pygame.image.load(os.path.join('data', 'images', 'PirateShip_09_001.png')).convert()
        self.image_09.set_colorkey([0,0,0])
        self.image_03.set_colorkey([0,0,0])
        self.image = self.image_03
        self.image.set_colorkey([0,0,0])
        self.rect = self.image_03.get_rect()

        self.rect.x = x
        self.rect.y = y

        if x < 0:
            self.rect.x = -100
            self.dx = 1
            self.image = self.image_03
        elif x > self.screen.get_width():
            self.rect.x = self.screen.get_width() + 100
            self.image = self.image_09
            self.dx = -1

        self.dy = 0
        self.speed = 1

    def update(self):
        self.rect.x += self.speed * self.dx
        self._check_bounds()

    def _check_bounds(self):
        if self.rect.x > self.screen.get_width() + 150 or self.rect.x < -150:
            self.kill()


