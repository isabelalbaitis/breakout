import pygame
BLACK = (0,0,0)
WHITE = (255, 255, 255)

class Paddle(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0,0,width,height])

        self.rect = self.image.get_rect()