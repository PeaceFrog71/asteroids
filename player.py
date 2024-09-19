import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0

    # in the player class
    def ship(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position - forward * self.radius
        b = self.position + forward * self.radius - right
        c = self.position + forward/2 * self.radius - right/2
        d = self.position + forward/2 * self.radius + right/2
        e = self.position + forward * self.radius + right
        
        #print(f"a={a}\nb={b}\nc={c}\nd={d}\n")
        return [a, b, c, d, e]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, WHITE, self.ship(), width=1)

    def rotate(self, dt):
        rotational_speed = PLAYER_TURN_SPEED * dt
        #print(f"PRS = {speed_corrected}")
        self.rotation += rotational_speed

    def update(self, dt):
        self.shot_timer -= dt
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
            self.shoot(dt, SHOT_SPEED)

    def move(self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        # print(f"Forward is: {forward}")

    def shoot(self, dt, shot_speed):
        if self.shot_timer > 0:
            return

        self.shot_timer = SHOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * shot_speed