import pygame
from constants import *
from player import *


def main():
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")    
	pygame.init()
	game_clock = pygame.time.Clock()
	dt = 0
	
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	running = True

	player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill(BLACK)
		player.draw(screen)
		pygame.display.flip()
		dt = game_clock.tick(60)/1000

		

		

	pygame.quit()
	 


if __name__ == "__main__":
	main()
