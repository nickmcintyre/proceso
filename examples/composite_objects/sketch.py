"""
Composite Objects
Adapted from https://p5js.org/examples/objects-composite-objects.html

An object can include several other objects. Creating such composite objects
is a good way to use the principles of modularity and build higher levels of
abstraction within a program. 
"""
from proceso import Sketch


p5 = Sketch()
p5.describe("Two white eggs rock back and forth as rings propagate from their centers.")


class Egg:
    def __init__(self, xpos, ypos, t, s):
        self.x = xpos
        self.y = ypos
        self.tilt = t
        self.scalar = s / 100.0
        self.angle = 0.0

    def wobble(self):
        self.tilt = p5.cos(self.angle) / 8
        self.angle += 0.1

    def display(self):
        p5.no_stroke()
        p5.fill(255)
        p5.push()
        p5.translate(self.x, self.y)
        p5.rotate(self.tilt)
        p5.scale(self.scalar)
        p5.begin_shape()
        p5.vertex(0, -100)
        p5.bezier_vertex(25, -100, 40, -65, 40, -40)
        p5.bezier_vertex(40, -15, 25, 0, 0, 0)
        p5.bezier_vertex(-25, 0, -40, -15, -40, -40)
        p5.bezier_vertex(-40, -65, -25, -100, 0, -100)
        p5.end_shape()
        p5.pop()


class Ring:
    def start(self, xpos, ypos):
        self.x = xpos
        self.y = ypos
        self.on = True
        self.diameter = 1

    def grow(self):
        if self.on == True:
            self.diameter += 0.5
            if self.diameter > p5.width * 2:
                self.diameter = 0.0

    def display(self):
        if self.on == True:
            p5.no_fill()
            p5.stroke_weight(4)
            p5.stroke(155, 153)
            p5.circle(self.x, self.y, self.diameter)


class EggRing:
    def __init__(self, x, y, t, sp):
        self.x = x
        self.y = y
        self.t = t
        self.sp = sp
        self.circle = Ring()
        self.ovoid = Egg(self.x, self.y, self.t, self.sp)
        self.circle.start(self.x, self.y - self.sp / 2)

    def transmit(self):
        self.ovoid.wobble()
        self.ovoid.display()
        self.circle.grow()
        self.circle.display()
        if self.circle.on == False:
            self.circle.on = True


er1: EggRing
er2: EggRing


def setup():
    global er1, er2
    p5.create_canvas(640, 360)
    er1 = EggRing(p5.width * 0.45, p5.height * 0.5, 0.1, 120)
    er2 = EggRing(p5.width * 0.65, p5.height * 0.8, 0.05, 180)


def draw():
    p5.background(0)
    er1.transmit()
    er2.transmit()


p5.run_sketch(setup=setup, draw=draw)
