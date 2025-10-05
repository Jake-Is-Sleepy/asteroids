import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,(255,255,255),self.position, self.radius, 2)
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        angle = random.uniform(20, 50)
        velA = self.velocity.rotate(angle)
        velB = self.velocity.rotate(-angle)
        asteroidA = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        asteroidB = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        asteroidA.velocity = velA * 1.2
        asteroidB.velocity = velB * 1.2