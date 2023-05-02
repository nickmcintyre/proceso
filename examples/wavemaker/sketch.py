"""
Wavemaker
Adapted from https://p5js.org/examples/interaction-wavemaker.html
CC-BY-NC-SA

This illustrates how waves (like water waves) emerge from particles
oscillating in place. Move your mouse to direct the wave. Contributed by
Aatish Bhatia, inspired by Orbiters by Dave Whyte. 
"""
from proceso import Sketch


p5 = Sketch()


def setup():
    p5.create_canvas(600, 600)
    p5.no_stroke()
    p5.fill(40, 200, 40)


def draw():
    p5.background(10, 10)  # translucent background (creates trails)

    # make a x and y grid of ellipses
    for x in range(0, p5.width, 30):
        for y in range(0, p5.height, 30):
            # starting point of each circle depends on mouse position
            x_angle = p5.remap(p5.mouse_x, 0, p5.width, -4 * p5.PI, 4 * p5.PI, True)
            y_angle = p5.remap(p5.mouse_x, 0, p5.height, -4 * p5.PI, 4 * p5.PI, True)
            # and also varies based on the particle's location
            angle = x_angle * (x / p5.width) + y_angle * (y / p5.height)

            # each particle moves in a circle
            t = p5.frame_count * 0.01
            my_x = x + 20 * p5.cos(2 * p5.PI * t + angle)
            my_y = y + 20 * p5.sin(2 * p5.PI * t + angle)

            p5.circle(my_x, my_y, 10)  # draw particle


p5.run_sketch(setup=setup, draw=draw)
