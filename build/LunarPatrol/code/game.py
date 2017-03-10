
import attractmode
import playmode
import gameovermode

class Game:
    """ Game Class """

    def __init__(self, screen, fps = 60):
        """ Constructor """
        # technical variables
        self.screen = screen
        self.framerate = fps
        self.scr_w = screen.get_width()
        self.scr_h = screen.get_height()

        # game mode handling
        self.game_modes = [ attractmode.AttractMode(self.screen, "Attract"), playmode.PlayMode(self.screen, "Play"), gameovermode.GameOverMode(self.screen, "GameOver")]
        self.game_mode_num = len(self.game_modes)
        self.game_mode_max_idx = self.game_mode_num - 1
        self.game_mode_cur_idx = 0 # specify the current game mode
        self.game_mode = self.game_modes[self.game_mode_cur_idx]
        self.game_mode.enter()


    def handle_events(self):
        """ handle upcoming events """
        done = False
        done = self.game_mode.handle_events()
        return done

    def update(self):
        """ update game objects, process game logic """
#1
        if self.game_mode.active == False:
            self.game_mode_cur_idx += 1
            self.game_mode = self.game_modes[self.game_mode_cur_idx % self.game_mode_num]
            self.game_mode.enter()
        self.game_mode.update()


    def draw_frame(self, screen):
        """ draw all objects on screen """
        self.game_mode.draw_frame()



