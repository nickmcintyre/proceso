"""
Recursion
Adapted from https://p5js.org/examples/structure-recursion.html
CC-BY-NC-SA

A demonstration of recursion, which means functions call themselves. A
recursive function must have a terminating condition, without which it will go
into an infinite loop. Notice how the drawCircle() function calls itself at
the end of its block. It continues to do this until the variable "level" is
equal to 1.
"""
from proceso import Sketch


p5 = Sketch()
p5.describe("A large circle is inscribed with smaller and smaller circles that shrink by half at each stage.")

p5.create_canvas(720, 560)
p5.no_stroke()


def draw_circle(x, radius, level):
    # 'level' is the variable that terminates the recursion once it reaches
    # a certain value (here, 1). If a terminating condition is not
    # specified, a recursive function keeps calling itself again and again
    # until it runs out of stack space - not a favourable outcome!
    tt = (126 * level) / 4.0
    p5.fill(tt)
    p5.circle(x, p5.height / 2, radius * 2)
    if level > 1:
        # 'level' decreases by 1 at every step and thus makes the terminating condition
        # attainable
        level = level - 1
        draw_circle(x - radius / 2, radius / 2, level)
        draw_circle(x + radius / 2, radius / 2, level)


draw_circle(p5.width / 2, 280, 6)
