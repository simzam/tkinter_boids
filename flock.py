""" class for dealing with a flock of boids. """

import Boid

class Flock():
    def __init__(self, radius, domain):
        self.num_boids = 0
        self.boids = []
        self.radius = radius # the distance deciding if two boids are neighbours
        self.domain = domain # coordinates of the world of the boids

    def __find_close_boids(self, curr_boid):
        
        neighbours = []
        for boid in self.boids:
            distance = curr_boid.distance_from_point(boid.pos)
            if distance == 0:
                continue
            if curr_boid.distance_from_point(boid.pos) < self.radius:
                neighbours.append(boid)
        return neighbours


    def update(self):
        """ update the velocity of the boids."""
        for boid in self.boids:
            if boid.avoid_neighbours(self.domain):
                continue

            neighbours = self.__find_close_boids(boid)
            
            boid.separation(neighbours)
            boid.alignment(neighbours)
            boid.cohesion(neighbours)

            
    def add_boid(self, pos = (0,0), vel = (0,0)):
        self.boids.append(Boid(pos, vel))


if __name__ == '__main__':
    
    def loop(app, boids):
        if app.running:
            boids.ATTRACT = app.ATTRACT
            boids.update()
            app.render(boids.getBList())
        app.parent.after(TIME, loop, app, boids)

    boids = Boids(NUM, SIZE)
    root = Tk(className="Boids")
    root.resizable(0, 0)
    app = BoidsApp(root, SIZE)
    loop(app, boids)
    root.mainloop()

