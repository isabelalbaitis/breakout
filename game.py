import pygame
from paddle import Paddle
from brick import Brick
import random

WIDTH, HEIGHT = 1010,610
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

		random.seed(1)
		for j in range(1, 300, 52):
			for i in range(1, 1000, 102):
				r = random.randint(0,255)
				g = random.randint(0,255)
				b = random.randint(0,255)

				brk = Brick(r,g,b)

				brk.rect.x = i - 1
				brk.rect.y = j - 1
				bricks.add(brk)

		all_sprites.add(bricks)
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