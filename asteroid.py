from constants import *
from circleshape import *
import pygame


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(center=(self.x,self.y), width=2, color=WHITE, radius=self.radius)


    def update(self, dt):
        self.position += self.velocity * dt


