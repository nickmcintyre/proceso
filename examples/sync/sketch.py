"""
Sync
CC-BY-NC-SA

Demonstration of the Kuramoto model for synchronization.
https://synchrony.cc
"""
from proceso import Sketch


p5 = Sketch()
p5.describe("Ten white circles moving like fireflies on a dark blue background.")

bugs = []
num_bugs = 10
coupling: object
KN: float


def setup():
    p5.create_canvas(720, 400)
    global coupling
    coupling = p5.create_slider(0, 10, 5)
    for _ in range(num_bugs):
        bugs.append(Bug())


def draw():
    p5.background("midnightblue")

    global KN
    KN = coupling.value() / num_bugs

    for bug in bugs:
        bug.sync()

    for bug in bugs:
        bug.draw()
        bug.update()
        bug.check_edges()


class Bug:
    def __init__(self):
        self.x = p5.width * 0.5
        self.y = p5.height * 0.5
        self.r = 5
        self.angle = p5.random(p5.TWO_PI)
        self.da_dt = 1
        self.dt = 0.01
        self.freq = p5.random(5, 10)

    def draw(self):
        a = p5.remap(self.angle % p5.TWO_PI, 0, p5.TWO_PI, 0, 255)
        p5.fill(255, a)
        p5.stroke(255, a)
        p5.circle(self.x, self.y, 2 * self.r)

    def update(self):
        self.x += p5.cos(self.angle)
        self.y += p5.sin(self.angle)
        self.angle += self.da_dt * self.dt

    def check_edges(self):
        if self.x > p5.width + self.r:
            self.x = -self.r
        if self.x < -self.r:
            self.x = p5.width + self.r
        if self.y > p5.height + self.r:
            self.y = -self.r
        if self.y < -self.r:
            self.y = p5.height + self.r

    def sync(self):
        self.da_dt = self.freq
        for bug in bugs:
            self.da_dt += KN * p5.sin(bug.angle - self.angle)


p5.run_sketch(setup=setup, draw=draw)
