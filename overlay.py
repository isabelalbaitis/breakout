import pygame

pygame.init()

SCORE = 0
LIVES = 5
WIDTH = 1000
HEIGHT = 600
WHITE = (255,255,255)
LABEL_FONT = pygame.font.SysFont('freesansbold.ttf',30)

class Overlay():
    def __init__(self, game):
        score_label = LABEL_FONT.render('Score:', True, WHITE)
        lives_label = LABEL_FONT.render('Lives:', True, WHITE)

        game.get_window().blit(score_label,(20,20))
        game.get_window().blit(lives_label,(20,20))
        pygame.display.update()


    def set_score(self, score):
        self.SCORE = score

    def get_score(self):
        return self.SCORE

    def set_lives(self, lives):
        self.LIVES = lives

    def get_lives(self):
        return self.LIVES