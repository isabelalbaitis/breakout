import pygame

pygame.init()

WIDTH = 1000
HEIGHT = 50
WHITE = (255,255,255)
BLACK = (0,0,0)

class Overlay(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pygame.init()
        label_font = pygame.font.SysFont('freestanding.ttf', 30)

        self.score = 0
        self.lives = 5

        self.image = pygame.Surface([WIDTH, HEIGHT])
        self.image.fill(BLACK)
        self.image.set_colorkey(WHITE)

        score_str = "Score: " + str(self.score)
        lives_str = "Lives: " + str(self.lives)

        self.score_text = label_font.render(score_str, False, WHITE)
        self.lives_text = label_font.render(lives_str, True, WHITE)

        self.image.blit(self.score_text,(20,10))
        self.image.blit(self.lives_text,(100,10))

        pygame.draw.rect(self.image, BLACK, [0,0,WIDTH,HEIGHT])
        self.rect = self.image.get_rect()

        pygame.display.update()

    def inc_score(self):
        self.score += 1

    def dec_lives(self):
        self.lives -= 1
