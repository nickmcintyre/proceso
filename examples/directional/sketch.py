"""
Directional
Adapted from https://p5js.org/examples/lights-directional.html
CC-BY-NC-SA

Move the mouse to change the direction of the light. Directional light comes
from one direction and is stronger when hitting a surface squarely and weaker
if it hits at a a gentle angle. After hitting a surface, a directional light
scatters in all directions. 
"""
from proceso import Sketch


p5 = Sketch()
p5.describe("Two gray spheres are illuminated when someone moves their mouse over them.")

radius = 200


def setup():
    p5.create_canvas(710, 400, p5.WEBGL)
    p5.no_stroke()
    p5.fill(200)


def draw():
    p5.no_stroke()
    p5.background(0)
    dir_y = (p5.mouse_y / p5.height - 0.5) * 4
    dir_x = (p5.mouse_x / p5.width - 0.5) * 4
    p5.directional_light(204, 204, 204, dir_x, dir_y, 1)
    p5.translate(-1.5 * radius, 0, 0)
    p5.sphere(radius)
    p5.translate(3 * radius, 0, 0)
    p5.sphere(radius)


p5.run_sketch(setup=setup, draw=draw)
