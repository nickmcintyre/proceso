"""
Morph
Adapted from https://p5js.org/examples/motion-morph.html
CC-BY-NC-SA

Changing one shape into another by interpolating vertices from one to another.
"""
from proceso import Sketch


p5 = Sketch()

# Two lists to store the vertices for two shapes
# This example assumes that each shape will have the same
# number of vertices, i.e. the size of each list will be the same
circle = []
square = []

# A list for a third set of vertices, the ones we will be drawing
# in the window
morph = []

# This boolean variable will control if we are morphing to a circle or square
state = False


def setup():
    p5.create_canvas(720, 400)

    # Create a circle using vectors pointing from center
    for angle in range(0, 360, 9):
        # Note we are not starting from 0 in order to match the
        # path of a circle.
        v = p5.Vector.from_heading(p5.radians(angle - 135))
        v *= 100
        circle.append(v)
        # Let's fill out morph list with blank Vectors while we are at it
        morph.append(p5.Vector(0, 0))

    # A square is a bunch of vertices along straight lines
    # Top of square
    for x in range(-50, 50, 10):
        square.append(p5.Vector(x, -50))
    # Right side
    for y in range(-50, 50, 10):
        square.append(p5.Vector(50, y))

    # Bottom
    for x in range(50, -50, -10):
        square.append(p5.Vector(x, 50))
    # Left side
    for y in range(50, -50, -10):
        square.append(p5.Vector(-50, y))


def draw():
    global state

    p5.background(51)

    # We will keep how far the vertices are from their target
    total_distance = 0

    # Look at each vertex
    for i in range(len(circle)):
        v1: p5.Vector
        # Are we lerping to the circle or square?
        if state:
            v1 = circle[i]
        else:
            v1 = square[i]
        # Get the vertex we will draw
        v2 = morph[i]
        # Lerp to the target
        v2 = v2.lerp(v1, 0.1)
        # Check how far we are from target
        total_distance += p5.Vector.dist(v1, v2)
        # Update vertex in morph list
        morph[i] = v2

    # If all the vertices are close, switch shape
    if total_distance < 0.1:
        state = not state

    # Draw relative to center
    p5.translate(p5.width / 2, p5.height / 2)
    p5.stroke_weight(4)
    # Draw a polygon that makes up all the vertices
    p5.begin_shape()
    p5.no_fill()
    p5.stroke(255)

    for v in morph:
        p5.vertex(v.x, v.y)

    p5.end_shape(p5.CLOSE)


p5.run_sketch(setup=setup, draw=draw)
