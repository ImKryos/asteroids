import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        # randomize angle of split
        random_angle = random.uniform(20, 50) 

        # creae two new vectors that are rotated by random angle
        a = self.velocity.rotate(random_angle) 
        b = self.velocity.rotate(-random_angle)

        # compute new radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # create 2 new asteroid objects at the current position with the new radius
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2
