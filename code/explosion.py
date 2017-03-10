import pygame
import spritesheet
import os


class Explosion(pygame.sprite.Sprite):
    """
    This is a explosion aninmation class
    """

    def __init__(self, screen, x, y, fps=60):
        super().__init__()  # calls constructor of base class
        # technical variables
        self.screen = screen
        self.framerate = fps
        self.image = pygame.Surface([64, 64])
        self.image.fill(self.screen.get_at((0, 0)))
        # animation related parameters
        self.image_sequence = []  # store the pictures for the animation
        self.image_sequence_len = 16  # number of pictures of animation
        self.anim_speed_secs = 0.5  # only modify this for the explosion in
        # seconds
        # calculate the number of frames the animation should last
        # animation's speed in frames
        self.anim_speed_frames = self.anim_speed_secs * self.framerate
        # calculate at how many ticks the frame should change
        # suppose we have an animation which should last 120 frames
        # which means 2 seconds at a framerate of 60, and we have
        # animation sequence of 10 pictures so the picture has to
        # change every 120 // 10 = 12 ticks/updates
        self.anim_frame_freq = self.anim_speed_frames // self.image_sequence_len
        self.anim_frame_idx = 0
        self.tick = 0  # for counting number of updates

        self.explosion_sound = None  # used in _init_sound()

        # location and size variables
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (self.x, self.y)

        # game rule variables

        # state variables
        self.started = False  # animation startet and running
        self.finished = False  # animation/explosion finished

        # initialize graphics
        self._init_graphics()
        # initialize sound
        self._init_sound()

    def _init_graphics(self):
        self.spritesheet = spritesheet.Spritesheet(os.path.join('data', 'images', 'Explosion_Sheet_12_001.png'))
        for row in range(4):
            for col in range(4):
                tmp_image = self.spritesheet.get_image(col * 64, row * 64, 64, 64)
                self.image_sequence.append(tmp_image)

        self.image_sequence_len = len(self.image_sequence)

    def _init_sound(self):
        pygame.mixer.init()
        self.explosion_sound = pygame.mixer.Sound(os.path.join('data', 'sounds', 'explosion_somewhere_far.ogg'))

    def update(self):
        '''
        change the image every anim_frame_freq frames
        '''
        if self.started:
#1
            self.tick += 1
            if self.tick > self.anim_frame_freq:
                self.anim_frame_idx += 1
                self.image = self.image_sequence[self.anim_frame_idx % self.image_sequence_len]
                self.rect = self.image.get_rect()
                self.rect.center = (self.x, self.y)
#1
                self.tick = 0
            if self.anim_frame_idx == self.image_sequence_len:
                self.anim_frame_idx = 0
                self.finished = True
                self.started = False
        if self.finished:
            self.kill()

    def explode(self):
        self.explosion_sound.play()
        self.started = True

