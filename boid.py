""" class for each individual boid.
boids are described in http://www.red3d.com/cwr/boids/
"""
from math import sqrt

class Boid:
    def __init__(self, position, velocity):
        self.pos = position
        self.vel = velocity


    def update_velocity(self, v):
        """ update velocity. """
        self.vel = (self.vel[0] + v[0],
                    self.vel[1] + v[0])


    def move(self):
        """ moving boid using the predefined velocity. """
        self.pos = (self.pos[0] + self.vel[0],
                    self.pos[1] + self.vel[1])


    def separation(self, neighbours):
        for neighbour in neighbours:
            self.distance_from_point(neighbour.pos)
        
    def alignment(self, neighbours):
        for boid in 
            
    def cohesion(self, neighbours):
        avg_pos = [0, 0]
        for boid in neighbours:
            

            

    def avoid_boundaries(self, domain):
        """ boids live inside a limited domain, in order to keep the boids in the 
        window ensure that the move in the opposite direction when they encounter
        a wall. This overshadows all other movement."""
        pass
        

        
    def distance_from_point(self, point):
        """ distance from position of boid to a given point. """
        assert isinstance(point, tuple), "A point is defined to be a tuple."
        assert len(point) == 2, "A point has two values."

        return sqrt((self.pos[0] - point[0])**2 +
                    (self.pos[1] - point[1])**2)

    
    
