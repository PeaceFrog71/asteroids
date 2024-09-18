import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import AsteroidField


def main():
	print("Starting asteroids!")
	pygame.init()
	game_clock = pygame.time.Clock()
	dt = 0
	
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	running = True

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable, )
	AsteroidField.containers = (updatable)
	Shot.containers = (shots, updatable, drawable)

	player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
	gamefield = AsteroidField()

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill(BLACK)
		for item in updatable:
			item.update(dt)
		for asteroid in asteroids:
			if player.collision_check(asteroid):
				print("Game Over!")
				return
		for item in drawable:
			item.draw(screen)


		pygame.display.flip()

		dt = game_clock.tick(80)/1000
		# print(f"dt = {dt}").
		# print(f"FPS = {game_clock.get_fps()}")
	pygame.quit()
	 
if __name__ == "__main__":
	main()
