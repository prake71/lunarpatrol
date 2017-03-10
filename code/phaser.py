import pygame


class Phaser(pygame.sprite.Sprite):
    """
    This is a starship phaser
    """

    def __init__(self):
        # call parent class
        super().__init__()
        self.image = pygame.Surface([4, 10])
        self.image.fill([255, 255, 255])  # bullet in white

        self.rect = self.image.get_rect()
        self.collided = False

    def update(self):
        # bullet's move
        self.rect.y -= 10  # from bottom to top - vertically
        if self.rect.y <= -20 or self.collided:
            self.kill()