import pygame
BLACK = (0,0,0)
WHITE = (255, 255, 255)

# Dimensions of the paddle
WIDTH = 200
HEIGHT = 10

# How many pixels the paddle moves per keystroke
SPEED = 10

class Paddle(pygame.sprite.Sprite):

    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([WIDTH, HEIGHT])
        self.image.fill(BLACK)

        pygame.draw.rect(self.image, color, [0,0,WIDTH,HEIGHT])

        self.rect = self.image.get_rect()

    def moveLeft(self):
        self.rect.x -= SPEED

        # Check that move will keep you on the screen
        if self.rect.x < 0:
            self.rect.x = 0

    def moveRight(self):
        self.rect.x += SPEED

        # Check that move will keep you on the screen
        if self.rect.x > 800:
            self.rect.x = 800