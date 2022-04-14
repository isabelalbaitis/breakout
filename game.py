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
GREEN = (0,255,0)
RED = (255,0,0)

paddle = Paddle(BLACK)
ball = Ball()
overlay = Overlay()

overlay_group = pygame.sprite.Group()
bricks = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

class Game():

	def __init__(self):
		pygame.mixer.init()
		pygame.mixer.music.load("Nicki Minaj- SuperBass (Studio Acapella).mp3")
		pygame.mixer.music.play(100,0.0,0)

		# Places paddle in initial placement
		paddle.rect.x = 400
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

		self.active = True
		self.game()

	def draw_window(self):
		WINDOW.fill(WHITE)
		all_sprites.draw(WINDOW)
		pygame.display.update()

		# Checks if ball bounces against side walls
		if ball.rect.x >= 990 or ball.rect.x <= 0:
			ball.velocity[0] = -ball.velocity[0]

		# Checks if ball bounces against ceiling
		if ball.rect.y < 0:
			ball.velocity[1] = -ball.velocity[1]

		# Checks if ball hits the floor
		if ball.rect.y > 560:
			ball.rect.y = 320
			ball.rect.x = 2
			ball.velocity[0] = 0
			ball.velocity[1] = 0
			#overlay.dec_lives()
			self.new_life()

		# Checks if ball collided with paddle
		if pygame.sprite.collide_mask(ball, paddle):
			ball.rect.x -= ball.velocity[0]
			ball.rect.y -= ball.velocity[1]
			ball.bounce()

		# Checks if ball collided with a brick
		bricks_to_hit = pygame.sprite.spritecollide(ball, bricks, False)
		for brick in bricks_to_hit:
			ball.rect.x -= ball.velocity[0]
			ball.rect.y -= ball.velocity[1]
			ball.bounce()
			if brick.hit() == True:
				overlay.inc_score()

		# Updates ball position
		ball.update()

		# Updates overlay
		overlay.update()

		pygame.display.flip()
		pygame.display.update()

	def new_life(self):
		if overlay.get_lives() > 1:
			overlay.dec_lives()
			pygame.time.delay(1000)
			ball.velocity[0] = random.randint(4, 8)
			ball.velocity[1] = random.randint(1, 8)

		else:
			font = pygame.font.Font(None, 70)
			game_over_text = font.render("GAME OVER ", 1, RED)
			WINDOW.blit(game_over_text, (350, 225))
			self.active = False



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

			if self.active:
				self.draw_window()

		pygame.quit()


def main():
	g = Game()
	g.__init__()


if __name__ == "__main__":
	main()