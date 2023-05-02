"""
Video Capture
Adapted from https://p5js.org/examples/dom-video-capture.html
CC-BY-NC-SA

Capture video from the webcam and display on the canvas as well with invert
filter. Note that by default the capture feed shows up, too. You can hide the
feed by uncommenting the capture.hide() line. 
"""
from proceso import Sketch


p5 = Sketch()

capture = None


def setup():
    p5.create_canvas(320, 240)
    global capture
    capture = p5.create_capture(p5.VIDEO)
    capture.size(320, 240)
    capture.hide()


def draw():
    p5.background(255)
    p5.image(capture, 0, 0, 320, 240)
    p5.apply_filter(p5.INVERT)


p5.run_sketch(setup=setup, draw=draw)
