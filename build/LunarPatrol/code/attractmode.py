import pygame
import gamemode
import intro
import spaceship
import enemy
import gametitle
import soundmanager

class AttractMode(gamemode.GameMode):
    """ Attract Mode - get the player excited to play our game """
    def __init__(self, screen, game, message="Lunar Patrol"):
        super().__init__(screen, game, message) # calls constructor of base class
#1
        self.name = "AttractMode"
        #self.message = message
        self.intro = None
        self.all_sprites_list = None
        self.tick_xmax = self.screen.get_width()
        self.tick_ymax = self.screen.get_height()
        self.xtick = 0
        self.ytick = 0
        self.horizontal_line = False
        self.vertical_line = False
        self.canvas = pygame.Surface((self.screen.get_width() // 2, self.screen.get_height() // 1))
        self.camera_upper_left_x = 0
        self.camera_upper_left_y = 0
        self.camera = pygame.Rect(self.camera_upper_left_x, self.camera_upper_left_y, self.canvas.get_width(), self.canvas.get_height())
        self.title = None
        self.title_camera = None
        self.title_sprite_list = None
        self.intro_sprite_list = None
        self.sm = soundmanager.SoundManager()
        self.my_sound = None

    def enter(self):
        self.active = True


        self.intro = intro.Intro(self.canvas, self.canvas.get_width() - 400, self.canvas.get_height())
        self.intro_sprite_list = pygame.sprite.Group(self.intro)
        self.title = gametitle.GameTitle(self.screen, 50, self.screen.get_height() // 4)
        #self.title_camera = pygame.Rect(50, self.screen.get_height() // 4, self.title.image.get_size()[0], self.title.image.get_size()[1])
        self.title_sprite_list = pygame.sprite.Group(self.title)
        self.sm.play_ambient('SpaceLoop.wav')



    def update(self):
        self.intro_sprite_list.update()

    def draw_frame(self):
        self.screen.fill([0,0,0])
        # draw horizontal line
        if self.xtick < self.tick_xmax:
            pygame.draw.line(self.screen, (191, 244, 66), (0, self.screen.get_height() // 4 + 60), (0 + self.xtick, self.screen.get_height() // 4 + 60))
            self.xtick += 2
        else:
            pygame.draw.line(self.screen, (191, 244, 66), (0, self.screen.get_height() // 4 + 60),
                             (0 + self.tick_xmax, self.screen.get_height() // 4 + 60))
            self.horizontal_line = True
#1

        #if self.horizontal_line:
        # draw vertical line
        if self.ytick < self.tick_ymax:
            pygame.draw.line(self.screen, (191,244, 66), (self.screen.get_width() // 3 + 30 , 0), (self.screen.get_width() // 3, 0 + self.ytick))
            self.ytick += 2
        else:
            pygame.draw.line(self.screen, (191, 244, 66), (self.screen.get_width() // 3 + 30, 0), (self.screen.get_width() // 3, 0 + self.tick_ymax))
            self.vertical_line = True

        self.intro_sprite_list.draw(self.canvas)
        self.title_sprite_list.draw(self.screen)
        # self.screen.fill([0,0,0], pygame.Rect( )
        self.screen.blit(self.canvas, (301, 220), self.camera )
        #self.screen.blit(self.canvas, (self.camera_upper_left_x + 50, self.camera_upper_left_y), pygame.Rect(self.intro.rect.x,self.intro.rect.y,499,385))
        #self.screen.blit(self.canvas, (50, self.screen.get_height() // 4), self.title_camera)
        pygame.display.flip()



    def exit(self):
        self.active = False
        self.intro_sprite_list.empty()
        self.title_sprite_list.empty()
        self.canvas.fill([0,0,0])
        self.ytick = 0
        self.xtick = 0
        self.sm.stop_ambient()


