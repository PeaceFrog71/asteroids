from constants import *
from circleshape import *
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, radius= SHOT_RADIUS):
        super().__init__(x, y, radius)
        self.color = WHITE
 
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius)


    def update(self, dt):
        self.position += (self.velocity * -dt)
        