import pygame

from random import randrange, choice

class Starfield:
    def __init__(self, screen, max_stars, star_speed):
        self.screen = screen
        self.stars = []
        for i in range(max_stars):
            star = [randrange(0, screen.get_width() - 1), randrange(0, screen.get_height() - 1), choice([1, 2, 3]) ]
            self.stars.append(star)

    def update(self):
        for star in self.stars:
            star[1] += star[2]
            # If the star hit the bottom border then we reposition
            # it in the top of the screen with a random X coordinate.
            if star[1] >= self.screen.get_height():
                star[1] = 0
                star[0] = randrange(0, self.screen.get_width())
                star[2] = choice([1,2,3])

    def draw(self):
        for star in self.stars:
            # adjust the star color according to the speed
            # the slower the star, the darker should be its color
            if star[2] == 1:
                color = (100, 100, 100)
            elif star[2] == 2:
                color = (190, 190, 190)
            elif star[2] == 3:
                color = (255, 255, 255)

            self.screen.fill(color, (star[0], star[1], star[2], star[2]))


