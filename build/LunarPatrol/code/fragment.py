import pygame
import random



class Fragment(pygame.sprite.Sprite):
    """ Class for bursting objects
    inspired by http://thepythongamebook.com/en:pygame:step015
    """
    gravity = False  # fragments fall down ?

    def __init__(self, screen, x, y):
        super().__init__()
#1
        self.seconds = 0.01
        self.pos = [0.0, 0.0]
        self.pos[0] = x
        self.pos[1] = y
        self.image = pygame.Surface((10, 10))

        self.image.set_colorkey((0, 0, 0))  # black transparent
        # circle(Surface, color, pos, radius, width=0) -> Rect
        color = random.randint(0,255)
        pygame.draw.circle(self.image, (color, color, color), (5, 5),
                           random.randint(2, 5))
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = self.pos  # if you forget this line the sprite sit in the topleft corner
        self.lifetime = 1 + random.random() * 5  # max 6 seconds
        self.time = 0.0
        self.fragmentmaxspeed = 200 * 2  # try out other factors !
        self.dx = random.randint(-self.fragmentmaxspeed, self.fragmentmaxspeed)
        self.dy = random.randint(-self.fragmentmaxspeed, self.fragmentmaxspeed)

    def update(self):
        self.time += self.seconds
        if self.time > self.lifetime:
            self.kill()
        self.pos[0] += self.dx * self.seconds
        self.pos[1] += self.dy * self.seconds
        if Fragment.gravity:
            self.dy += 9.81  # gravity suck fragments down
        self.rect.centerx = round(self.pos[0], 0)
        self.rect.centery = round(self.pos[1], 0)
