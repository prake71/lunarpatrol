import pygame
import os

class SoundManager:
    def __init__(self):
        """ manages sound data to ensure there are no duplicate
        sound files loaded into memory.
        """
        self.path_prefix = os.path.join('data', 'sounds')
        self.sound_map = {}
        pygame.mixer.init()
        pygame.mixer.set_reserved(1)
        self.ambient_channel = pygame.mixer.Channel(0)
        self.ambient_sound = None

    def load_sound(self, filename):
        """ load a sound file or return the existing instane of the
        loaded sound data """
        new_sound = self.sound_map.get(filename, None)
        if new_sound:
            return new_sound
        new_sound = pygame.mixer.Sound(os.path.join(self.path_prefix, filename))
        self.sound_map[filename] = new_sound
        return new_sound

    def play_ambient(self, filename, volume=1.0, stereo=0.5):
        """ play ambient sound """
        self.ambient_sound = self.load_sound(filename)
        self.ambient_channel.stop()
        #self.ambient_channel.set_volume(volume, stereo)
        self.ambient_channel.set_volume(volume)
        self.ambient_channel.play(self.ambient_sound, -1, -1)

    def stop_ambient(self):
        """ stop ambient sound """
        self.ambient_channel.stop()

    def set_ambient_properties(self, volume, stereo):
        """ set the volume porperties on the ambient
        sound channel """
        self.ambient_channel.set_volume(volume, stereo)


