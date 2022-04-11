import pygame
from paddle import Paddle
from brick import Brick
from ball import Ball
from overlay import Overlay
import random

WIDTH, HEIGHT = 1000,600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout")

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

paddle = Paddle(BLACK)
ball = Ball()
overlay = Overlay()

bricks = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

class Game():

	def __init__(self):
		# Places paddle in initial placement
		paddle.rect.x = 450
		paddle.rect.y = 550

		# Starts ball below the bricks all the way to the left
		ball.rect.x = 2
		ball.rect.y = 320

		# Sets up bricks with random colors on the board
		random.seed(1)
		for j in range(0, 300, 50):
			for i in range(1, 1000, 100):
				r = random.randint(0,255)
				g = random.randint(0,255)
				b = random.randint(0,255)

				brk = Brick(r,g,b)

				brk.rect.x = i - 1
				brk.rect.y = j - 1
				bricks.add(brk)

		all_sprites.add(bricks)
		all_sprites.add(paddle)
		all_sprites.add(ball)
		all_sprites.add(overlay)

		self.game()

	def draw_window(self):
		WINDOW.fill(WHITE)
		all_sprites.draw(WINDOW)
		pygame.display.update()

		# Checks if ball bounces against side walls
		if ball.rect.x >= 1000 or ball.rect.x <= 0:
			ball.velocity[0] = -ball.velocity[0]
		# Checks if ball bounces against ceiling
		if ball.rect.y < 0:
			ball.velocity[1] = -ball.velocity[1]
		# Checks if ball hits the floor
		if ball.rect.y > 550:
			ball.velocity[0] = 0
			ball.velocity[1] = 0
			overlay.dec_lives()

		# Checks if ball collided with paddle
		if pygame.sprite.collide_mask(ball, paddle):
			ball.rect.x -= ball.velocity[0]
			ball.rect.y -= ball.velocity[1]
			ball.bounce()

		# Checks if ball collided with a brick
		bricks_to_hit = pygame.sprite.spritecollide(ball, bricks, False)
		for brick in bricks_to_hit:
			ball.bounce()
			if brick.hit() == True:
				overlay.inc_score()

		# Updates ball position
		ball.update()

	def get_window(self):
		return WINDOW

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