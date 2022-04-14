import pygame

pygame.init()

WHITE = (255,255,255)
BLACK_TRANSLUCENT = (100,100,100)
BLACK = (0,0,0)
GREEN = (0,255,0)

WIDTH, HEIGHT = 1000,600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

FONT = pygame.font.SysFont(None, 30)

SCORE_LABEL_TEXT = FONT.render("Score: ", True, WHITE)
LIVES_LABEL_TEXT= FONT.render("Lives: ", True, WHITE)


class Overlay(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pygame.init()

        self.image = pygame.Surface((300,50))
        self.image.set_colorkey(BLACK)

        self.score = 0
        self.lives = 5

        self.image.blit(SCORE_LABEL_TEXT, (5,10))
        self.image.blit(LIVES_LABEL_TEXT, (205,10))

        self.score_text = FONT.render(str(self.score),True,WHITE, BLACK)
        self.image.blit(self.score_text,(75,10))

        self.lives_text = FONT.render(str(self.lives),True,WHITE,BLACK)
        self.image.blit(self.lives_text, (280,10))

        pygame.display.flip()
        self.rect = self.image.get_rect()

    def inc_score(self):
        self.score += 1
        print(self.score)

    def dec_lives(self):
        self.lives -= 1
        print(self.lives)

    def update(self):

        self.score_text = FONT.render(str(self.score), True, WHITE, BLACK)
        self.image.blit(self.score_text, (75, 10))

        self.lives_text = FONT.render(str(self.lives), True, WHITE, BLACK)
        self.image.blit(self.lives_text, (280, 10))

        pygame.display.flip()

    def get_lives(self):
        return self.lives
