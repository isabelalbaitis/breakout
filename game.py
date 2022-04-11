import pygame
from paddle import Paddle
from brick import Brick

WIDTH, HEIGHT = 1000,600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout")

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

paddle = Paddle(BLACK)

bricks = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()

all_sprites.add(paddle)


class Game():
	def __init__(self):
		paddle.rect.x = 450
		paddle.rect.y = 550
		self.get_bricks()
		self.game()

	def draw_window(self):
		WINDOW.fill(WHITE)
		all_sprites.draw(WINDOW)
		pygame.display.update()

	def get_bricks(self):
		brick_row = []
		for b in brick_row:
			b = Brick()
			bricks.add(b)
		all_sprites.add(bricks)


	def game(self):
		clock = pygame.time.Clock()
		run = True
		while run:
			clock.tick(FPS)
			for event in pygame.event.get():
				# Quit if user hits close
				if event.type == pygame.QUIT:
					run = False

			# Responding to keystrokes
			keystroke = pygame.key.get_pressed()
			if keystroke[pygame.K_RIGHT] or keystroke[pygame.K_d]:
				paddle.moveRight()
			if keystroke[pygame.K_LEFT] or keystroke[pygame.K_a]:
				paddle.moveLeft()

			self.draw_window()

		pygame.quit()


def main():
	g = Game()
	g.__init__()


if __name__ == "__main__":
	main()