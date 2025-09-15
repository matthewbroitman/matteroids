import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            spur = self.velocity.rotate(random_angle)
            alt_spur = self.velocity.rotate(-random_angle)
            child_radius = self.radius-ASTEROID_MIN_RADIUS
            child1 = Asteroid(self.position.x,self.position.y,child_radius)
            child2 = Asteroid(self.position.x,self.position.y,child_radius)
            child1.velocity = spur * 1.2
            child2.velocity = alt_spur * 1.2

