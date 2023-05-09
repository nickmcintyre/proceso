"""
Relativity
Adapted from https://p5js.org/examples/color-relativity.html

Each color is perceived in relation to other colors. The top and bottom bars
each contain the same component colors, but a different display order causes
individual colors to appear differently.
"""
from proceso import Sketch


p5 = Sketch()
p5.describe("Two rows of vertical lines drawn in different five different colors.")

p5.create_canvas(710, 400)
p5.no_stroke()
a = p5.color(165, 167, 20)
b = p5.color(77, 86, 59)
c = p5.color(42, 106, 105)
d = p5.color(165, 89, 20)
e = p5.color(146, 150, 127)


def draw_band(v, w, x, y, z, ypos, bar_width):
    num = 5
    color_order = [v, w, x, y, z]
    for i in range(0, p5.width, int(bar_width * num)):
        for j in range(num):
            p5.fill(color_order[j])
            p5.rect(i + j * bar_width, ypos, bar_width, p5.height * 0.5)


draw_band(a, b, c, d, e, 0, p5.width / 128)
draw_band(c, a, d, b, e, p5.height / 2, p5.width / 128)
