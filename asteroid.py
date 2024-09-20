import pygame
import random
from constants import *
from circleshape import CircleShape



class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.position, width=1, radius=self.radius)


    def update(self, dt):
        self.position += (self.velocity * dt)
        

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            self.spawn_children()

    def spawn_children(self):
        split_angle = random.randint(20, 50)
        child1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        child1.velocity = pygame.Vector2(self.velocity).rotate(split_angle) * 1.5
        child2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        child2.velocity = pygame.Vector2(self.velocity).rotate(-split_angle) * 1.5
