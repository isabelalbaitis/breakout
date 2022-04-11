import pygame
from paddle import Paddle

WIDTH, HEIGHT = 1000,600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout")

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

paddle = Paddle(BLACK, 100, 10)

all_sprites = pygame.sprite.Group()

all_sprites.add(paddle)


class Game():
	def __init__(self):
		paddle.rect.x = 450
		paddle.rect.y = 550
		self.game()

	def draw_window(self):
		WINDOW.fill(WHITE)
		all_sprites.draw(WINDOW)
		pygame.display.update()


	def game(self):
		clock = pygame.time.Clock()
		run = True
		while run:
			clock.tick(FPS)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
			all_sprites.draw(WINDOW)
			self.draw_window()
		pygame.quit()

	all_sprites.update()
	all_sprites.draw(WINDOW)

def main():
	g = Game()
	g.__init__()


if __name__ == "__main__":
	main()