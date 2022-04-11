import pygame
import random

WIDTH = 100
HEIGHT = 50

class Brick(pygame.sprite.Sprite):
    def __init__(self, red_val, grn_val, blu_val):
        pygame.sprite.Sprite.__init__(self)
        self.RED_VAL = red_val
        self.GRE_VAL = grn_val
        self.BLU_VAL = blu_val

        self.HEALTH = 766 - (red_val + grn_val + blu_val)
        self.COLOR = (red_val, grn_val, blu_val)

        self.image = pygame.Surface([WIDTH, HEIGHT])
        self.image.fill(self.COLOR)

        pygame.draw.rect(self.image, self.COLOR, [0,0,WIDTH,HEIGHT])
        self.rect = self.image.get_rect()