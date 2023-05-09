"""
Letters
Adapted from https://p5js.org/examples/typography-letters.html
CC-BY-NC-SA

Letters can be drawn to the screen by loading a font, setting its
characteristics and then drawing the letters. This example uses a for loop and
unicode reference numbers to automatically fill the canvas with characters in
a grid. Vowels are selected and given a specific fill color. 
"""
from proceso import Sketch


p5 = Sketch()
p5.describe("Letters, numbers, and symbols are displayed in white on a gray background. Vowels are highlighted in pink.")

font: object
font_size = 32


def preload():
    global font
    # Ensure the .ttf or .otf font stored in the assets directory
    # is loaded before setup() and draw() are called
    font = p5.load_font("assets/SourceSansPro-Regular.otf")


def setup():
    p5.create_canvas(710, 400)

    # Set text characteristics
    p5.text_font(font)
    p5.text_size(font_size)
    p5.text_align(p5.CENTER, p5.CENTER)


def draw():
    p5.background(160)

    # Set the gap between letters and the left and top margin
    gap = 52
    margin = 10
    p5.translate(margin * 4, margin * 4)

    # Set the counter to start at the character you want
    # in this case 35, which is the # symbol
    counter = 35

    # Loop as long as there is space on the canvas
    for y in range(0, p5.height - gap, gap):
        for x in range(0, p5.width - gap, gap):
            # Use the counter to retrieve individual letters by their Unicode number
            letter = chr(counter)

            # Add different color to the vowels and other characters
            if (
                letter == "A"
                or letter == "E"
                or letter == "I"
                or letter == "O"
                or letter == "U"
            ):
                p5.fill("#ed225d")
            else:
                p5.fill(255)

            # Draw the letter to the screen
            p5.text(letter, x, y)

            # Increment the counter
            counter += 1


p5.run_sketch(preload=preload, setup=setup, draw=draw)
