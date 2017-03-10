import pygame
import random
import os


class Enemy(pygame.sprite.Sprite):
    """ This is a class for any kind of enemy """
    def __init__(self, screen, x, y, color=(183, 183, 183)):
        super().__init__()
        # technical variables
        self.screen = screen
        self.scr_w = self.screen.get_width()
        self.scr_h = self.screen.get_height()

        # self.image = pygame.Surface([20, 15])
        self.image = pygame.image.load(os.path.join('data', 'images', 'Rock_002.png') ).convert()
        self.image = pygame.transform.scale(self.image, (30,30))
        #self.image.fill(color)

        self.image.set_colorkey([0,0,0])
        self.img_w = self.image.get_width()
        self.img_h = self.image.get_height()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # self.rect.inflate_ip(-15, -15)
        self.radius = 9
        self.dx = 1
        self.dy = 1


        self.speed = 1

    def update(self):
        """ move enemy """
        self.rect.x += self.speed * self.dx
        self.rect.y += self.dy
        self._check_bounds()


    def _check_bounds(self):
        # check horizontal direction
        if self.rect.x < 1:
            self.rect.x = 1
            self.dx *= -1
        if self.rect.x > self.scr_w - self.img_w:
            self.rect.x = self.scr_w - self.img_w
            self.dx *= -1
        # check vertical direction
        if self.rect.y < 1:
            self.rect.y = 1
            self.dy *= -1
        if random.randint(0, 1):
            if self.rect.y > self.scr_h - 10 * self.img_h:
                self.dy *= -1

    def kill(self):
        #for _ in range(random.randint(3,15)):
        #    fragment.Fragment(self.screen, self.rect.centerx, self.rect.centery)
        pygame.sprite.Sprite.kill(self)



    def change_speed(self, speed):
        self.speed = speed

