import pygame
import phaser
from constants import *
import soundmanager
import os



class SpaceShip(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        """ SpaceShip Sprite for Player 1 """
        super().__init__()

        self.screen = screen
        self.scr_w = self.screen.get_width()
        self.scr_h = self.screen.get_height()

        self.image = None

        self.dx = 0
        self.dy = 0
        self.speedup = 3

        self.hit = False
        self.dead = False

        self.ammo_stock = AMMO_STOCK_MAX

        self._init_graphics(x, y)
        self._init_sounds()

    def _init_graphics(self, x, y):
        self.image = pygame.image.load(os.path.join('data', 'images', 'StarShip_12_001.png')).convert()
        self.image.set_colorkey([0,0,0])
        self.rect = self.image.get_rect()
        #self.rect.inflate_ip(-50, -50)
        self.img_w = self.image.get_width()
        self.img_h = self.image.get_height()
        self.rect.x = x
        self.rect.y = y

    def _init_sounds(self):
        self.sm = soundmanager.SoundManager()
        self.shoot_sound = self.sm.load_sound("laser5.ogg")

    def _check_bounds(self):        # check horizontal direction
        if self.rect.x < 1:
            self.rect.x = 1
        if self.rect.x  > self.scr_w - self.img_w:
            self.rect.x = self.scr_w - self.img_w

        # check vertical direction
        if self.rect.y < 1:
            self.rect.y = 1
        if self.rect.y > self.scr_h - self.img_h:
            self.rect.y = self.scr_h - self.img_h

    def change_speed(self, x, y):
#1
        self.dx += x * self.speedup
        self.dy += y * self.speedup



    def shoot(self):
        if self.ammo_stock > 0:

            self.shoot_sound.play()

            my_phaser = phaser.Phaser()
            my_phaser.rect.x = self.rect.centerx
            my_phaser.rect.y = self.rect.centery - 26
            self.ammo_stock -= 1
            return my_phaser

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        self._check_bounds()
        self._check_keys()

    def reset(self):
        self.ammo_stock = 100

    def explode(self):
        pass



    def _check_keys(self):
        pass






