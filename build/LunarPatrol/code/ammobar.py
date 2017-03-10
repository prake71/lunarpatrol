import pygame
from constants import *

class AmmoBar(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, color = (191, 244, 66)):
        super().__init__()

        self.image = pygame.Surface([100, 20])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.ammo_stock = AMMO_STOCK_MAX

    def update(self):
        self.image.fill([191,244,66])
        self.image.fill((0,0,0), pygame.Rect(0,0, 100 - ((100  * self.ammo_stock) // AMMO_STOCK_MAX), 20))

