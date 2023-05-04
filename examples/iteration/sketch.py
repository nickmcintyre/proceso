"""
Iteration
Adapted from https://p5js.org/examples/control-iteration.html
CC-BY-NC-SA

Iteration with a "for" structure to construct repetitive forms. 
"""
from proceso import Sketch


p5 = Sketch()

num = 14

p5.create_canvas(720, 360)
p5.background(102)
p5.no_stroke()

# Draw white bars
p5.fill(255)
y = 60
for _ in range(int(num / 3)):
    p5.rect(50, y, 475, 10)
    y += 20

# Gray bars
p5.fill(51)
y = 40
for _ in range(num):
    p5.rect(405, y, 30, 10)
    y += 20

y = 50
for _ in range(num):
    p5.rect(425, y, 30, 10)
    y += 20

# Thin lines
y = 45
p5.fill(0)
for _ in range(num - 1):
    p5.rect(120, y, 40, 1)
    y += 20
