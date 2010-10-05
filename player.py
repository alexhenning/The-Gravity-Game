
import math, random, pygame
import gravity

class Player(gravity.GravityWell):
    def __init__(self, coord, rad):
        gravity.GravityWell.__init__(self, coord, rad)
    def draw(self, screen):
        pygame.draw.circle(screen, (25, 200, 25), tuple(self.coord), self.rad)
    
