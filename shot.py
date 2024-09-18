from constants import *
from circleshape import *
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius=SHOT_RADIUS)
        self.color = WHITE
        self.velocity = 0



    def draw(self, screen):
        pygame.draw.circle(screen, center=(self.position.x,self.position.y), width=0, color=self.color, radius=SHOT_RADIUS)


    def update(self, dt):
        self.position += (self.velocity * SHOT_SPEED * -dt)
        print(f"Shot position is @ {self.position} with a velocity of {self.velocity}")