""" class for each individual boid """

class Boid:
    def __init__(self, position, velocity, id_num):
        self.pos = position
        self.vel = velocity
        self.id_num = id_num


    def update_velocity(self, v):
        """ update velocity. """
        self.vel = (self.vel[0] + v[0],
                    self.vel[1] + v[0])


    def move(self):
        """ moving boid using the predefined velocity. """
        self.pos = (self.pos[0] + self.vel[0],
                    self.pos[1] + self.vel[1])
        
