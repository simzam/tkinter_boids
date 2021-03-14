from tkinter import Tk
from boidsgui import BoidsApp
from boid import Boid


class Flock():
    """ class for holding all the boids. """
    def __init__(self, radius, domain):
        self.num_boids = 0
        self.boids = []
        # the distance deciding if two boids are neighbours
        self.radius = radius
        # coordinates of the world of the boids
        self.domain = domain

    def _get_boids(self):
        return [(boid.pos, boid.vel) for boid in self.boids]

    def _add_tuple(self, t1, t2):
        # assert isinstance(t1, tuple)
        # assert isinstance(t2, tuple)

        # assert len(t1) == 2
        # assert len(t2) == 2

        return (t1[0] + t2[0], t1[1] + t2[1])

    def _div_tuple(self, t1, const):
        return (t1[0] / const, t1[1] / const)

    def _find_close_boids(self, curr_boid):
        """find all the boids within the "self.radius" distance from this
        boid."""
        neighs = []
        neighs_pos = (0, 0)
        neighs_vel = (0, 0)

        for boid in self.boids:
            distance = curr_boid.distance_from_point(boid.pos)
            if distance == 0:
                continue
            if curr_boid.distance_from_point(boid.pos) < self.radius:
                neighs.append(boid)
                neighs_pos = self._add_tuple(neighs_pos, boid.pos)
                neighs_vel = self._add_tuple(neighs_vel, boid.vel)

        neighs_pos = self._div_tuple(neighs_pos, len(neighs))
        neighs_vel = self._div_tuple(neighs_vel, len(neighs))

        return neighs, neighs_pos, neighs_vel

    def update(self):
        """ update the velocity of the boids."""
        for boid in self.boids:
            if boid.avoid_neighbours(self.domain):
                continue

            neighs, neighs_pos, neighs_vel = self._find_close_boids(boid)

            boid.separation(neighs)
            boid.alignment(neighs)
            boid.cohesion(neighs)


    def add_boid(self, pos=(0, 0), vel=(0, 0)):
        # should do check whether boid were sucessfully created.
        self.boids.append(Boid(pos, vel))


if __name__ == '__main__':
    RADIUS = 15
    SIZE = 1000

    # TODO: fix nonquadratic canvas
    # HEIGHT = 1000
    # WIDTH  = 1800

    def loop(app, boids):
        if app.running:
            boids.ATTRACT = app.ATTRACT
            boids.update()
            app.render(boids.__get_boids())
        app.parent.after(TIME, loop, app, boids)

    boids = Flock(RADIUS, SIZE)
    root = Tk(className="Flock")
    root.resizable(0, 0)
    app = BoidsApp(root, SIZE)
    loop(app, boids)
    root.mainloop()
