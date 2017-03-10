# http://stackoverflow.com/questions/17454257/a-bit-confused-with-blitting-pygame

import pygame
import os

class Intro(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, fname="intro.txt"):
        super().__init__()

        self.screen = screen
        self.image = pygame.Surface([self.screen.get_width() // 2, self.screen.get_height() // 2])
        self.image.fill([0, 0, 0])
        self.image.set_colorkey([0, 0, 0])

        self.text = None
        self.textlines = []

        self.font = pygame.font.Font(os.path.join('data', 'fonts', 'Arcade.ttf'), 20)
        self.fname = os.path.join('data', fname)
        #f = open("intro.txt", "r")
        f = open(self.fname, 'r')
        lines = f.readlines()

        sum_sizes = [0,0]
        for line in lines:
#1
            self.text = self.font.render(line.strip(), True, [255, 255, 255], [0,0,0])
            self.text.set_colorkey((0,0,0))
            self.textlines.append(self.text)
            (size_x, size_y) = self.text.get_size()
            if size_x > sum_sizes[0]:
                sum_sizes[0] = size_x
            sum_sizes[1] += size_y

#1
        self.image = pygame.Surface([sum_sizes[0], sum_sizes[1]])

        for i in range(len(self.textlines)):
            self.image.blit(self.textlines[i], ((self.image.get_width() - self.textlines[i].get_width()) // 2, i * self.textlines[i].get_height()))

        self.rect = self.image.get_rect()
        self.rect.x = (self.screen.get_width() - self.image.get_width()) // 2  # + 80
        self.rect.top = self.y_start = y


    def scroll(self, speed=1):
        self.rect.y -= 1+speed
        self._checkbounds()

    def _checkbounds(self):
        if self.rect.bottom < 0:
            self.rect.top = self.y_start

    def update(self):
        self.scroll(0)



