"""
Variables
Adapted from https://p5js.org/examples/data-variables.html
CC-BY-NC-SA

Variables are used for storing values. In this example, change the values of
variables to affect the composition. 
"""
from proceso import Sketch


p5 = Sketch()

p5.create_canvas(720, 400)
p5.background(0)
p5.stroke(153)
p5.stroke_weight(4)
p5.stroke_cap(p5.SQUARE)

a = 50
b = 120
c = 180

p5.line(a, b, a + c, b)
p5.line(a, b + 10, a + c, b + 10)
p5.line(a, b + 20, a + c, b + 20)
p5.line(a, b + 30, a + c, b + 30)

a = a + c
b = p5.height - b

p5.line(a, b, a + c, b)
p5.line(a, b + 10, a + c, b + 10)
p5.line(a, b + 20, a + c, b + 20)
p5.line(a, b + 30, a + c, b + 30)

a = a + c
b = p5.height - b

p5.line(a, b, a + c, b)
p5.line(a, b + 10, a + c, b + 10)
p5.line(a, b + 20, a + c, b + 20)
p5.line(a, b + 30, a + c, b + 30)
