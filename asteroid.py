from constants import *
from circleshape import *
import pygame


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, center=(self.position.x,self.position.y), width=2, color=GREEN, radius=self.radius)


    def update(self, dt):
        self.position += (self.velocity * dt)


