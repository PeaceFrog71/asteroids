from constants import *
from circleshape import *
from shot import *
import pygame


# Base class for game objects
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, radius=PLAYER_RADIUS)
        self.rotation = 0
        self.fire_timer = 0

    # in the player class
    def ship(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position - forward * self.radius
        b = self.position + forward * self.radius - right
        c = self.position + forward/2 * self.radius
        d = self.position + forward * self.radius + right
        
        #print(f"a={a}\nb={b}\nc={c}\nd={d}\n")
        return [a, b, c, d]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, GREEN, points=self.ship(), width=2)

    def rotate(self, dt):
        speed_corrected = PLAYER_TURN_SPEED * dt
        #print(f"PRS = {speed_corrected}")
        self.rotation += speed_corrected

    def update(self, dt):
        self.fire_timer -= dt
        keys = pygame.key.get_pressed()
        #print(f"dt = {dt}")
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            self.move(dt)
        if keys[pygame.K_w]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)

    def move(self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        # print(f"Forward is: {forward}")

    def shoot(self, dt):
        if self.fire_timer > 0:
            return

        self.fire_timer = SHOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y, radius= SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * SHOT_SPEED
        #print(f"Shot velocity is: {velocity}")