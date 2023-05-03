"""
Simple Shapes
Adapted from https://p5js.org/examples/hello-p5-simple-shapes.html
CC-BY-NC-SA

This example includes a circle, square, triangle, and a flower. 
"""
from proceso import Sketch


p5 = Sketch()

# Create the canvas
p5.create_canvas(720, 400)
p5.background(200)

# Set colors
p5.fill(204, 101, 192, 127)
p5.stroke(127, 63, 120)

# A rectangle
p5.rect(40, 120, 120, 40)
# An ellipse
p5.ellipse(240, 240, 80, 80)
# A triangle
p5.triangle(300, 100, 320, 100, 310, 80)

# A design for a simple flower
p5.translate(580, 200)
p5.no_stroke()
for _ in range(10):
    p5.ellipse(0, 30, 20, 80)
    p5.rotate(p5.PI / 5)
