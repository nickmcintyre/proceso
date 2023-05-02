"""
Load and Display Image
Adapted from https://p5js.org/examples/image-load-and-display-image.html
CC-BY-NC-SA

Images can be loaded and displayed to the screen at their actual size or any other size.
To run this example locally, you will need an image file, and a running local server.
"""
from proceso import Sketch


p5 = Sketch()

img: object  # Declare variable 'img'


def preload():
    global img
    img = p5.load_image("assets/moonwalk.jpg")  # Load the image


def setup():
    p5.create_canvas(720, 400)


def draw():
    # Displays the image at its actual size at point (0,0)
    p5.image(img, 0, 0)
    # Displays the image at point (0, height/2) at half size
    p5.image(img, 0, p5.height / 2, img.width / 2, img.height / 2)


p5.run_sketch(preload=preload, setup=setup, draw=draw)
