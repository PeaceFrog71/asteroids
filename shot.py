from constants import *
from circleshape import *
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, radius= SHOT_RADIUS, rotation=0):
        super().__init__(x, y, radius)
        self.color = WHITE
        self.velocity = pygame.Vector2(0,1) * SHOT_SPEED
        self.velocity = self.velocity.rotate(rotation)
        self.radius = radius


    def draw(self, screen):
        pygame.draw.circle(screen, center=(self.position.x,self.position.y), width=0, color=self.color, radius=self.radius)


    def update(self, dt):
        self.position += (self.velocity * -dt)
        #print(f"Shot position is @ {self.position} with a velocity of {self.velocity}")