import pygame
import explosion

'''
Testing the Explosion class
'''
FPS = 60

# initialize
pygame.init()

screen = pygame.display.set_mode([640, 480])

pygame.display.set_caption("Test #1 for Explosion class")

done = False

all_sprites = pygame.sprite.Group()
my_explosion = explosion.Explosion(screen, 320, 240, FPS)
all_sprites.add(my_explosion)

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                my_explosion.explode()

    all_sprites.update()
    screen.fill([0, 0, 0])
    all_sprites.draw(screen)

    clock.tick(FPS)
    pygame.display.flip()
pygame.quit()