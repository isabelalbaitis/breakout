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

ZERO = FONT.render("0", True,WHITE)
ONE = FONT.render("1", True,WHITE)
TWO = FONT.render("2", True,WHITE)
THREE = FONT.render("3", True,WHITE)
FOUR = FONT.render("4", True,WHITE)
FIVE = FONT.render("5", True,WHITE)
SIX = FONT.render("6", True,WHITE)
SEVEN = FONT.render("7", True,WHITE)
EIGHT = FONT.render("8", True,WHITE)
NINE = FONT.render("9", True,WHITE)


class Overlay(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pygame.init()

        self.image = pygame.Surface((300,50))
        self.image.set_colorkey(BLACK)

        self.score = 0
        self.lives = 5

        self.image.blit(SCORE_LABEL_TEXT, (10,10))
        self.image.blit(LIVES_LABEL_TEXT, (210,10))

        self.score_text = FONT.render(str(self.score),True,WHITE, BLACK)
        self.image.blit(self.score_text,(80,10))

        self.lives_text = self.get_number_text(self.lives)
        self.image.blit(self.lives_text, (280,10))

        pygame.display.flip()
        self.rect = self.image.get_rect()

    def get_number_text(self, number):
        if number == 0:
            return ZERO
        if number == 1:
            return ONE
        if number == 2:
            return TWO
        if number == 3:
            return THREE
        if number == 4:
            return FOUR
        if number == 5:
            return FIVE
        if number == 6:
            return SIX
        if number == 7:
            return SEVEN
        if number == 8:
            return EIGHT
        if number == 9:
            return NINE

    def inc_score(self):
        self.score += 1
        print(self.score)

    def dec_lives(self):
        self.lives -= 1
        print(self.lives)

    def update(self):
        self.score_text = FONT.render(str(self.score), True, WHITE, BLACK)
        self.image.blit(self.score_text, (80, 10))

        self.lives_text = self.get_number_text(self.lives)
        self.image.blit(self.lives_text, (480, 10))

        pygame.display.flip()

    def get_lives(self):
        return self.lives
