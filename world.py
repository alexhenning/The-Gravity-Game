
import math, random, pygame
import gravity, player

def getRandomGravityWells():
    return gravity.GravityWell([random.randint(10, 790), random.randint(10, 590)], random.randint(1, 10))

def applyForces(mover, puller):
    mover.x_force -= ((mover.coord[0] - puller.coord[0]) / 1000.0) * (puller.rad/float(mover.rad))
    mover.y_force -= ((mover.coord[1] - puller.coord[1]) / 1000.0) * (puller.rad/float(mover.rad))

def dist(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

class Level:
    def __init__(self, numGravityWells, player):
        self.player = player
        self.gravityWells = []
        [self.addWell() for i in range(numGravityWells)]
    def runIter(self):
        for i in self.gravityWells + [self.player]:
            for j in self.gravityWells + [self.player]:
                applyForces(i, j)
        for i in self.gravityWells + [self.player]: i.applyForces()
    def isOver(self):
        for i in self.gravityWells:
            if dist(self.player.coord, i.coord) <= self.player.rad + i.rad:
                return True
        return False
    def addWell(self):
        well = getRandomGravityWells()
        while dist(self.player.coord, well.coord) <= 100:
            well = getRandomGravityWells()
        self.gravityWells.append(well)
    def draw(self, screen):
        for i in self.gravityWells + [self.player]:
            i.draw(screen)
        
