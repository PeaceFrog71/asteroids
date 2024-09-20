import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from scoreboard import Scoreboard


def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	game_clock = pygame.time.Clock()
	dt = 0
	running = True


	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (shots, updatable, drawable)

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroid_field = AsteroidField()
	scoreboard = Scoreboard(FONT_PATH, FONT_SIZE, screen)


	while running:
		refresh_list = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		for obj in updatable:
			obj.update(dt)
		for asteroid in asteroids:
			if refresh_list:
				refresh_list = False
				break
			if asteroid.collision_check(player):
				print("Game Over!")
				sys.exit()
			for shot in shots:
				if asteroid.collision_check(shot):
					shot.kill()
					scoreboard.update_score(1 * asteroid.radius)
					asteroid.split()
					
					refresh_list = True
					break

		screen.fill(BLACK)
		scoreboard.render()
		for obj in drawable:
			obj.draw(screen)


		pygame.display.flip()

		dt = game_clock.tick(200) / 1000
	 
if __name__ == "__main__":
	main()
