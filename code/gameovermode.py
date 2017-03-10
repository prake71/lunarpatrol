import pygame
import gamemode
import intro
import soundmanager

class GameOverMode(gamemode.GameMode):
    """ Attract Mode - get the player excited to play our game """
    def __init__(self, screen, game, message="Game Over!"):
        super().__init__(screen, game, message) # calls constructor of base class
#1
        self.name = "GameOverMode"
        #self.message = message
        self.screen = screen
        self.outro = None
        self.all_sprites_list = None
        self.sm = soundmanager.SoundManager()

    def enter(self):
        self.active = True
        self.outro = intro.Intro(self.screen, 100, self.screen.get_height()+50, "Credits")
        self.all_sprites_list = pygame.sprite.Group(self.outro)
        self.sm.play_ambient('SpaceLoungeLoop.wav', 0.1)
    def update(self):
        self.all_sprites_list.update()

    def draw_frame(self):
        self.screen.fill([0,0,0])

        self.all_sprites_list.draw(self.screen)
        pygame.display.update()

    def exit(self):
        self.all_sprites_list.empty()
        self.sm.stop_ambient()
        self.active = False
