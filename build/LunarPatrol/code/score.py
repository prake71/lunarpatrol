import pygame
from pathlib import Path
import os


class Score(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        super().__init__()

        # screen properties
        self.screen = screen
        self.score = 0
        self.score_str = '{:0>6}'.format(self.score)
        self.font = pygame.font.Font(os.path.join('data', 'fonts', 'ARCADECLASSIC.TTF'), 20)

        self.image_score = self.font.render(self.score_str, True, [255, 255, 255])
        self.image_txt = self.font.render("Player 1", True, [255,255,255])
        self.size_score_img = self.image_score.get_size()
        self.size_txt_img = self.image_txt.get_size()
        self.sum_size_x = self.size_txt_img[0]# + self.size_txt_img[0]
        self.sum_size_y = self.size_score_img[1] + self.size_txt_img[1]
        self.size = [self.sum_size_x, self.sum_size_y]
        self.image = pygame.Surface(self.size)
        self.image.blit(self.image_txt, ((self.image.get_width() - self.image_txt.get_width()) // 2, 0 * self.image_txt.get_width()))
        self.image.blit(self.image_score,
                        ((self.image.get_width() - self.image_score.get_width()) // 2, 1 * self.image_score.get_width()))
        self.image.set_colorkey([0,0,0])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.score_str = '{:0>6}'.format(self.score)
        self.image.fill([0,0,0])
        self.image_score = self.font.render(self.score_str, True, [255, 255, 255])

        self.image.blit(self.image_txt,
                        ((self.image.get_width() - self.image_txt.get_width()) // 2, 0 * self.image_txt.get_height()))
        self.image.blit(self.image_score,
                        ((self.image.get_width() - self.image_score.get_width()) // 2, 1 * self.image_score.get_height()))

    def reset(self):
        self.score = 0
        self.score_str = '{:0>6}'.format(self.score)


class HiScore(Score):
    def __init__(self, screen, x, y):
        super().__init__(screen, x, y)

        self.fname = os.path.join('data', 'hiscore')
        self.image_txt = self.font.render("Hi Score", True, [255, 255, 255])
        # load hiscore file
        self._load_hiscore_file()


    def _load_hiscore_file(self):
        try:
            with open(self.fname) as f:
                self.score_str = f.readline().strip()
                self.score = int(self.score_str)
        except IOError:
            print("file not found!")

    def save_hiscore_file(self):
        with open(self.fname, 'r+') as out:
            out.write(str(self.score) + '\n')
            out.truncate()




