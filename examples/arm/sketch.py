"""
Arm
Adapted from https://p5js.org/examples/transform-arm.html
CC-BY-NC-SA

This example uses transform matrices to create an arm. The angle of each
segment is controlled with the mouseX and mouseY position. The transformations
applied to the first segment are also applied to the second segment because
they are inside the same push() and pop() matrix group. 
"""
import proceso as p5


x: float
y: float
seg_length = 100


def setup():
    p5.create_canvas(720, 400)
    p5.stroke_weight(30)

    # Stroke with a semi-transparent white
    p5.stroke(255, 160)

    # Position the "shoulder" of the arm in the center of the canvas
    global x, y
    x = p5.width * 0.5
    y = p5.height * 0.5


def draw():
    p5.background(0)

    # Change the angle of the segments according to the mouse positions
    angle_1 = (p5.mouse_x / p5.width - 0.5) * -p5.TWO_PI
    angle_2 = (p5.mouse_y / p5.height - 0.5) * p5.PI

    # use push and pop to "contain" the transforms. Note that
    # even though we draw the segments using a custom function,
    # the transforms still accumulate
    p5.push()
    segment(x, y, angle_1)
    segment(seg_length, 0, angle_2)
    p5.pop()


# a custom function for drawing segments
def segment(x, y, a):
    p5.translate(x, y)
    p5.rotate(a)
    p5.line(0, 0, seg_length, 0)


p5.run(setup=setup, draw=draw)
