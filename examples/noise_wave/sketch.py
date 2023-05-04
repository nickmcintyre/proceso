"""
Noise Wave
Adapted from https://p5js.org/examples/math-noise-wave.html
CC-BY-NC-SA

Using Perlin Noise to generate a wave-like pattern. Original by Daniel Shiffman.
"""
from proceso import Sketch


p5 = Sketch()

yoff = 0.0  # 2nd dimension of perlin noise


def setup():
    p5.create_canvas(710, 400)


def draw():
    global yoff

    p5.background(51)

    p5.fill(255)
    # We are going to draw a polygon out of the wave points
    p5.begin_shape()

    xoff = 0  # Option #1: 2D Noise
    # xoff = yoff # Option #2: 1D Noise

    # Iterate over horizontal pixels
    for x in range(0, p5.width + 10, 10):
        # Calculate a y value according to noise, map to

        # Option #1: 2D Noise
        y = p5.remap(p5.noise(xoff, yoff), 0, 1, 200, 300)

        # Option #2: 1D Noise
        # y = p5.remap(p5.noise(xoff), 0, 1, 200,300)

        # Set the vertex
        p5.vertex(x, y)
        # Increment x dimension for noise
        xoff += 0.05
    # increment y dimension for noise
    yoff += 0.01
    p5.vertex(p5.width, p5.height)
    p5.vertex(0, p5.height)
    p5.end_shape(p5.CLOSE)


p5.run_sketch(setup=setup, draw=draw)
