import pygame


class Spritesheet(object):
    """
    Spritesheet class
    This class provides funtions for handle sheets of
    bitmaps aka sprite sheets

    """

    """
    ----------------------------
    member variables
    ----------------------------
    """
    sprite_sheet = None  # storage for our bitmap
    """
    ----------------------------
    private functions
    ----------------------------
    """

    # Constructor
    def __init__(self, filename, convert=None):
        # load(filename) -> Surface
        self.sprite_sheet = pygame.image.load(filename)  # .convert_alpha()

    """
    ----------------------------
    protected functions
    ----------------------------
    """

    """
    ----------------------------
    public functions
    ----------------------------
    """

    def get_image(self, x, y, width, height):
        """ Grab a single image out of a larger spritesheet
            Pass in the x, y location of the sprite
            and the width and heigth of the sprite. """

        # Create a new blank image
        image = pygame.Surface([width, height])  # .convert_alpha()

        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        # Assuming black works as the transparent color
        image.set_colorkey([0, 0, 0])

        # Return the image
        return image
