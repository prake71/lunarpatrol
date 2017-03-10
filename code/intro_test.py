# http://stackoverflow.com/questions/17454257/a-bit-confused-with-blitting-pygame

import pygame

class Intro(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        super().__init__()

        self.screen = screen
        self.image = pygame.Surface([self.screen.get_width() // 2, self.screen.get_height() // 2])
        self.image.fill([0,0,0])
        self.image.set_colorkey([0,0,0])

        self.text = None
        self.textlines = []

        self.font = pygame.font.Font("../data/fonts/Arcade.ttf", 20)

        f = open("intro.txt", "r")
        lines = f.readlines()

        sum_sizes = [0,0]
        for line in lines:
#1
            self.text = self.font.render(line.strip(), True, [255, 255, 255])
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
        self.rect.x = (self.screen.get_width() - self.image.get_width()) // 2
        self.rect.y = self.y_start = y


    def scroll(self, speed):
        self.rect.y -= 1+speed
        self._checkbounds()

    def _checkbounds(self):
        if self.rect.bottom < 0:
            self.rect.y = self.y_start

    def update(self):
        self.scroll(0)

def main():
    fps = 60
    screen = pygame.display.set_mode((600, 600))

    canvas = pygame.Surface((600, 600))
    camera1 = pygame.Rect(100, 0, 400, 300)

    pygame.init()

    my_intro = Intro(canvas, 100, canvas.get_height())
    my_sprite_group = pygame.sprite.GroupSingle(my_intro)

    clock = pygame.time.Clock()
    while True:
        clock.tick(fps)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit(0)

        my_sprite_group.update()

        screen.fill((0,0,0))
        my_sprite_group.draw(canvas)
        screen.blit(canvas, (100,100), camera1)


        pygame.display.flip()

if __name__ == "__main__":
    main()
