
import pygame
import os

class GameMode:
    """ This is the GameMode class where other more specialized
    classes have to be derived from """

    def __init__(self, screen, game, message, fps = 60):
        self.name = None
        self.game = game
        # screen properties
        self.screen = screen
        self.scr_w = screen.get_width()
        self.scr_h = screen.get_height()
        self.fps = fps
        # select some standard font to use, size, bold, italics
        #self.font = pygame.font.SysFont("impact", 25, True, False)
        self.font = pygame.font.Font(os.path.join('data', 'fonts', 'ARCADECLASSIC.TTF'),25)
        self.text = self.font.render(str(message), True, [255, 255, 255])
        self.textheight = self.text.get_height()
        self.textwidth = self.text.get_width()
        self.active = False # mode currently active = true or not = false

    def enter(self):
        """ enter mode """
        #self.name = name
        self.active = True



    def exit(self):
        """ exit mode """
        self.active = False

    def handle_events(self):
        done = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
#1
                    self.exit()
        return done

    def update(self):
        """ invoked each frame, has to be overwritten """

    def draw_frame(self):
        self.screen.fill([0, 0, 0])
        # per default put some text on the screen showing the modes name
        self.screen.blit(self.text, [(self.scr_w - self.textwidth) // 2, (self.scr_h - self.textheight) // 2 ])
        pygame.display.update()



