"""
Flocking
Adapted from https://p5js.org/examples/hello-p5-flocking.html
CC-BY-NC-SA

Demonstration of Craig Reynolds' "Flocking" behavior.
(Rules: Cohesion, Separation, Alignment.)
From natureofcode.com.
"""
import proceso as p5


boids = []


def setup():
    p5.create_canvas(720, 400)

    # Add an initial set of boids into the system
    for _ in range(20):
        boids.append(Boid(p5.random(p5.width), p5.random(p5.height)))


def draw():
    p5.background(51)
    # Run all the boids
    for b in boids:
        b.run(boids)


# Boid class
# Methods for Separation, Cohesion, Alignment added
class Boid:
    def __init__(self, x, y):
        self.acceleration = p5.Vector(0, 0)
        self.velocity = p5.Vector.random(2)
        self.position = p5.Vector(x, y)
        self.r = 3.0
        self.maxspeed = 3  # Maximum speed
        self.maxforce = 0.05  # Maximum steering force

    def run(self, boids):
        self.flock(boids)
        self.update()
        self.borders()
        self.render()

    # Forces go into acceleration
    def apply_force(self, force):
        self.acceleration += force

    # We accumulate a new acceleration each time based on three rules
    def flock(self, boids):
        sep = self.separate(boids)  # Separation
        ali = self.align(boids)  # Alignment
        coh = self.cohesion(boids)  # Cohesion
        # Arbitrarily weight these forces
        sep * 2.5
        ali * 1.0
        coh * 1.0
        # Add the force vectors to acceleration
        self.apply_force(sep)
        self.apply_force(ali)
        self.apply_force(coh)

    # Method to update location
    def update(self):
        # Update velocity
        self.velocity += self.acceleration
        # Limit speed
        self.velocity.set_limit(self.maxspeed)
        self.position += self.velocity
        # Reset acceleration to 0 each cycle
        self.acceleration *= 0

    # A method that calculates and applies a steering force towards a target
    # STEER = DESIRED MINUS VELOCITY
    def seek(self, target):
        desired = (
            target - self.position
        )  # A vector pointing from the location to the target
        # Normalize desired and scale to maximum speed
        desired.normalize()
        desired * self.maxspeed
        # Steering = Desired minus Velocity
        steer = desired - self.velocity
        steer.set_limit(self.maxforce)  # Limit to maximum steering force
        return steer

    # Draw boid as a circle
    def render(self):
        p5.fill(127, 127)
        p5.stroke(200)
        p5.circle(self.position.x, self.position.y, 16)

    # Wraparound
    def borders(self):
        if self.position.x < -self.r:
            self.position.x = p5.width + self.r
        if self.position.y < -self.r:
            self.position.y = p5.height + self.r
        if self.position.x > p5.width + self.r:
            self.position.x = -self.r
        if self.position.y > p5.height + self.r:
            self.position.y = -self.r

    # Separation
    # Method checks for nearby boids and steers away
    def separate(self, boids):
        desiredseparation = 25.0
        steer = p5.Vector(0, 0)
        count = 0
        # For every boid in the system, check if it's too close
        for b in boids:
            d = p5.Vector.dist(self.position, b.position)
            # If the distance is greater than 0 and less than an arbitrary amount (0 when you are yourself)
            if (d > 0) and (d < desiredseparation):
                # Calculate vector pointing away from neighbor
                diff = self.position - b.position
                diff.normalize()
                diff /= d  # Weight by distance
                steer += diff
                count += 1  # Keep track of how many
        # Average -- divide by how many
        if count > 0:
            steer /= count

        # As long as the vector is greater than 0
        if steer.mag > 0:
            # Implement Reynolds: Steering = Desired - Velocity
            steer.normalize()
            steer *= self.maxspeed
            steer -= self.velocity
            steer.set_limit(self.maxforce)
        return steer

    # Alignment
    # For every nearby boid in the system, calculate the average velocity
    def align(self, boids):
        neighbordist = 50
        sum = p5.Vector(0, 0)
        count = 0
        for b in boids:
            d = p5.Vector.dist(self.position, b.position)
            if (d > 0) and (d < neighbordist):
                sum += b.velocity
                count += 1

        if count > 0:
            sum /= count
            sum.normalize()
            sum *= self.maxspeed
            steer = sum - self.velocity
            steer.set_limit(self.maxforce)
            return steer
        else:
            return p5.Vector(0, 0)

    # Cohesion
    # For the average location (i.e. center) of all nearby boids, calculate steering vector towards that location
    def cohesion(self, boids):
        neighbordist = 50
        sum = p5.Vector(0, 0)  # Start with empty vector to accumulate all locations
        count = 0
        for b in boids:
            d = p5.Vector.dist(self.position, b.position)
            if (d > 0) and (d < neighbordist):
                sum += b.position  # Add location
                count += 1

        if count > 0:
            sum /= count
            return self.seek(sum)  # Steer towards the location
        else:
            return p5.Vector(0, 0)


p5.run(setup=setup, draw=draw)
