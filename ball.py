import pygame
import random

BLACK = (0,0,0)
WIDTH = 10
HEIGHT = 10

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([WIDTH, HEIGHT])
        self.image.fill(BLACK)

        pygame.draw.rect(self.image, BLACK, [0,0,WIDTH,HEIGHT])

        # Velocity of the ball
        # First value is x-direction velocity
        # Second value is y-direction velocity
        self.velocity = [random.randint(2,4), random.randint(1,4)]

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = random.randint(-8,8)

        # Prevents ball from bouncing across screen infinitely
        while self.velocity[1] == 0:
            self.velocity[1] = random.randint(-8,8)