import pygame
import random

RED_VAL = random.randint(0, 255)
GRE_VAL = random.randint(0, 255)
BLU_VAL = random.randint(0, 255)

HEALTH = 766 - (RED_VAL + GRE_VAL + BLU_VAL)

COLOR = (RED_VAL, GRE_VAL, BLU_VAL)

WIDTH = 100
HEIGHT = 50

class Brick(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__()
        self.image = pygame.Surface([WIDTH, HEIGHT])
        self.image.fill(COLOR)

        pygame.draw.rect(self.image, COLOR, [0,0,WIDTH,HEIGHT])
        self.rect = self.image.get_rect()