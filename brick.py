import pygame

WIDTH = 100
HEIGHT = 50

class Brick(pygame.sprite.Sprite):
    def __init__(self, red_val, grn_val, blu_val):
        pygame.sprite.Sprite.__init__(self)
        self.red = red_val
        self.gre = grn_val
        self.blu = blu_val

        self.red_subtr = self.red / 32
        self.gre_subtr = self.gre / 32
        self.blu_subtr = self.blu / 32

        self.health = 766 - (red_val + grn_val + blu_val)
        self.color = (red_val, grn_val, blu_val)

        self.image = pygame.Surface([WIDTH, HEIGHT])
        self.image.fill(self.color)

        pygame.draw.rect(self.image, self.color, [0, 0, WIDTH, HEIGHT])
        self.rect = self.image.get_rect()

    # Returns true on kill
    def hit(self):
        self.health -= 25
        if self.health <= 0:
            pygame.sprite.Sprite.kill()
            return True
        else:
            self.red -= self.red_subtr
            self.gre -= self.gre_subtr
            self.blu -= self.blu_subtr

            if self.red < 0:
                self.red = 0

            if self.gre < 0:
                self.gre = 0

            if self.blu < 0:
                self.blu = 0

            self.color = (self.red, self.gre, self.blu)
            self.image.fill(self.color)
            return False