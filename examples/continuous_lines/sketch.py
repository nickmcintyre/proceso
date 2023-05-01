"""
Continuous Lines
Adapted from https://p5js.org/examples/drawing-continuous-lines.html
CC-BY-NC-SA

Click and drag the mouse to draw a line. 
"""
import proceso as p5


def setup():
    p5.create_canvas(710, 400)
    p5.background("dodgerblue")


def draw():
    p5.stroke(255)
    if p5.mouse_is_pressed == True:
        p5.line(p5.mouse_x, p5.mouse_y, p5.pmouse_x, p5.pmouse_y)


def key_pressed():
    p5.background("dodgerblue")


p5.run(setup=setup, draw=draw, key_pressed=key_pressed)
