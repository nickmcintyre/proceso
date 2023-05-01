from typing import Annotated

from ._binding import _p5js


# GRAPHICS RENDERER
P2D: Annotated[
    str,
    "The default, two-dimensional renderer."
] = _p5js.P2D
WEBGL: Annotated[
    str,
    "One of the two render modes in p5: P2D (default renderer) and WEBGL.Enables 3D render by introducing the third dimension: Z. "
] = _p5js.WEBGL

# TRIGONOMETRY
HALF_PI: Annotated[
    float,
    """HALF_PI is a mathematical constant with the value 1.57079632679489661923. It is half the ratio of the circumference of a circle to its diameter.
    It is useful in combination with the trigonometric functions sin() and cos().
    """,
] = _p5js.HALF_PI
PI: Annotated[
    float,
    """PI is a mathematical constant with the value 3.14159265358979323846. It is the ratio of the circumference of a circle to its diameter.
    It is useful in combination with the trigonometric functions sin() and cos().
    """,
] = _p5js.PI
QUARTER_PI: Annotated[
    float,
    """QUARTER_PI is a mathematical constant with the value 0.7853982. It is one quarter the ratio of the circumference of a circle to its diameter.
    It is useful in combination with the trigonometric functions sin() and cos().
    """,
] = _p5js.QUARTER_PI
TAU: Annotated[
    float,
    """TAU is an alias for TWO_PI, a mathematical constant with the value 6.28318530717958647693. It is twice the ratio of the circumference of a circle to its diameter.
    It is useful in combination with the trigonometric functions sin() and cos().
    """,
] = _p5js.TAU
TWO_PI: Annotated[
    float,
    """TWO_PI is a mathematical constant with the value 6.28318530717958647693. It is twice the ratio of the circumference of a circle to its diameter.
    It is useful in combination with the trigonometric functions sin() and cos().
    """,
] = _p5js.TWO_PI
DEGREES: Annotated[
    str,
    "Constant to be used with the angle_mode() function, to set the mode in which p5 interprets and calculates angles (either DEGREES or RADIANS).",
] = _p5js.DEGREES
RADIANS: Annotated[
    str,
    "Constant to be used with the angle_mode() function, to set the mode in which p5 interprets and calculates angles (either RADIANS or DEGREES).",
] = _p5js.RADIANS

# SHAPE
CORNER: str = _p5js.CORNER

CORNERS: str = _p5js.CORNERS

RADIUS: str = _p5js.RADIUS

RIGHT: str = _p5js.RIGHT

LEFT: str = _p5js.LEFT

CENTER: str = _p5js.CENTER

TOP: str = _p5js.TOP

BOTTOM: str = _p5js.BOTTOM

BASELINE: str = _p5js.BASELINE

POINTS: float = _p5js.POINTS

LINES: float = _p5js.LINES

LINE_STRIP: float = _p5js.LINE_STRIP

LINE_LOOP: float = _p5js.LINE_LOOP

TRIANGLES: float = _p5js.TRIANGLES

TRIANGLE_FAN: float = _p5js.TRIANGLE_FAN

TRIANGLE_STRIP: float = _p5js.TRIANGLE_STRIP

QUADS: str = _p5js.QUADS

QUAD_STRIP: str = _p5js.QUAD_STRIP

TESS: str = _p5js.TESS

CLOSE: str = _p5js.CLOSE

OPEN: str = _p5js.OPEN

CHORD: str = _p5js.CHORD

PIE: str = _p5js.PIE

PROJECT: str = _p5js.PROJECT # PEND: careful this is counterintuitive

SQUARE: str = _p5js.SQUARE

ROUND: str = _p5js.ROUND

BEVEL: str = _p5js.BEVEL

MITER: str = _p5js.MITER

# COLOR
RGB: str = _p5js.RGB

HSB: Annotated[
 str,
 """HSB (hue, saturation, brightness) is a type of color model. You can learn more about it at
https://learnui.design/blog/the-hsb-color-system-practicioners-primer.html
 """
] = _p5js.HSB

HSL: str = _p5js.HSL

# DOM EXTENSION
AUTO: Annotated[
  str,
  """AUTO allows us to automatically set the width or height of an element
  (but not both), based on the current height and width of the element.
  Only one parameter can be passed to size() function as AUTO, at a time.
  """
] = _p5js.AUTO

# INPUT
ALT: int = _p5js.ALT

BACKSPACE: int = _p5js.BACKSPACE

CONTROL: int = _p5js.CONTROL

DELETE: int = _p5js.DELETE

DOWN_ARROW: int = _p5js.DOWN_ARROW

ENTER: int = _p5js.ENTER

ESCAPE: int = _p5js.ESCAPE

LEFT_ARROW: int = _p5js.LEFT_ARROW

OPTION: int = _p5js.OPTION

RETURN: int = _p5js.RETURN

RIGHT_ARROW: int = _p5js.RIGHT_ARROW

SHIFT: int = _p5js.SHIFT

TAB: int = _p5js.TAB

UP_ARROW: int = _p5js.UP_ARROW

# RENDERING
BLEND: str = _p5js.BLEND

REMOVE: str = _p5js.REMOVE

ADD: str = _p5js.ADD

DARKEST: str = _p5js.DARKEST

LIGHTEST: str = _p5js.LIGHTEST

DIFFERENCE: str = _p5js.DIFFERENCE

SUBTRACT: str = _p5js.SUBTRACT

EXCLUSION: str = _p5js.EXCLUSION

MULTIPLY: str = _p5js.MULTIPLY

SCREEN: str = _p5js.SCREEN

REPLACE: str = _p5js.REPLACE

OVERLAY: str = _p5js.OVERLAY

HARD_LIGHT: str = _p5js.HARD_LIGHT

SOFT_LIGHT: str = _p5js.SOFT_LIGHT

DODGE: str = _p5js.DODGE

BURN: str = _p5js.BURN

# FILTERS
THRESHOLD: str = _p5js.THRESHOLD

GRAY: str = _p5js.GRAY

OPAQUE: str = _p5js.OPAQUE

INVERT: str = _p5js.INVERT

POSTERIZE: str = _p5js.POSTERIZE

DILATE: str = _p5js.DILATE

ERODE: str = _p5js.ERODE

BLUR: str = _p5js.BLUR

# TYPOGRAPHY
NORMAL: str = _p5js.NORMAL

ITALIC: str = _p5js.ITALIC

BOLD: str = _p5js.BOLD

BOLDITALIC: str = _p5js.BOLDITALIC

CHAR: str = _p5js.CHAR

WORD: str = _p5js.WORD

# VERTICES
LINEAR: str = _p5js.LINEAR

QUADRATIC: str = _p5js.QUADRATIC

BEZIER: str = _p5js.BEZIER

CURVE: str = _p5js.CURVE

# WEBGL DRAWMODES

STROKE: str = _p5js.STROKE

FILL: str = _p5js.FILL

TEXTURE: str = _p5js.TEXTURE

IMMEDIATE: str = _p5js.IMMEDIATE

# WEBGL TEXTURE MODE
# NORMAL already exists for typography
IMAGE: str = _p5js.IMAGE

# WEBGL TEXTURE WRAP AND FILTERING
# LINEAR already exists above
NEAREST: str = _p5js.NEAREST

REPEAT: str = _p5js.REPEAT

CLAMP: str = _p5js.CLAMP

MIRROR: str = _p5js.MIRROR

# DEVICE-ORIENTATION
LANDSCAPE: str = _p5js.LANDSCAPE

PORTRAIT: str = _p5js.PORTRAIT

# ACCESSIBILITY

GRID: str = _p5js.GRID

AXES: str = _p5js.AXES

LABEL: str = _p5js.LABEL

FALLBACK: str = _p5js.FALLBACK

CONTAIN: str = _p5js.CONTAIN

COVER: str = _p5js.COVER

# CAMERA
VIDEO: str = _p5js.VIDEO

AUDIO: str = _p5js.AUDIO
