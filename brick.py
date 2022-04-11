import pygame

WIDTH = 100
HEIGHT = 50

class Brick(pygame.sprite.Sprite):
    def __init__(self, red_val, grn_val, blu_val):
        pygame.sprite.Sprite.__init__(self)
        self.RED = red_val
        self.GRE = grn_val
        self.BLU = blu_val

        self.HEALTH = 766 - (red_val + grn_val + blu_val)
        self.COLOR = (red_val, grn_val, blu_val)

        self.image = pygame.Surface([WIDTH, HEIGHT])
        self.image.fill(self.COLOR)

        pygame.draw.rect(self.image, self.COLOR, [0,0,WIDTH,HEIGHT])
        self.rect = self.image.get_rect()

    # Returns true on kill
    def hit(self):
        self.HEALTH -= 25
        if self.HEALTH <= 0:
            pygame.sprite.Sprite.kill()
            return True
        else:
            self.RED -= 8
            self.GRE -= 8
            self.BLU -= 8
            self.COLOR = (self.RED, self.GRE, self.BLU)
            self.image.fill(self.COLOR)
            return False