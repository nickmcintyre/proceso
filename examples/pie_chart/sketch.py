"""
Pie Chart
Adapted from https://p5js.org/examples/form-pie-chart.html
CC-BY-NC-SA

Uses the arc() function to generate a pie chart from the data stored in a list. 
"""
from proceso import Sketch


p5 = Sketch()
p5.describe("A grayscale pie chart on a dark gray background.")

angles = [30, 10, 45, 35, 60, 38, 75, 67]

p5.create_canvas(720, 400)
p5.background(100)
p5.no_stroke()


def pie_chart(diameter, data):
    last_angle = 0
    for i in range(len(data)):
        gray = p5.remap(i, 0, len(data), 0, 255)
        p5.fill(gray)
        p5.arc(
            p5.width / 2,
            p5.height / 2,
            diameter,
            diameter,
            last_angle,
            last_angle + p5.radians(angles[i]),
        )
        last_angle += p5.radians(angles[i])


pie_chart(300, angles)
