from typing import Annotated


class Constants:
    _p5js: object

    # GRAPHICS RENDERER
    P2D: Annotated[str, "The default, two-dimensional renderer."]
    WEBGL: Annotated[
        str,
        "One of the two render modes in p5: P2D (default renderer) and WEBGL.Enables 3D render by introducing the third dimension: Z. ",
    ]

    # TRIGONOMETRY
    HALF_PI: Annotated[
        float,
        """HALF_PI is a mathematical constant with the value 1.57079632679489661923. It is half the ratio of the circumference of a circle to its diameter.
        It is useful in combination with the trigonometric functions sin() and cos().
        """,
    ]
    PI: Annotated[
        float,
        """PI is a mathematical constant with the value 3.14159265358979323846. It is the ratio of the circumference of a circle to its diameter.
        It is useful in combination with the trigonometric functions sin() and cos().
        """,
    ]
    QUARTER_PI: Annotated[
        float,
        """QUARTER_PI is a mathematical constant with the value 0.7853982. It is one quarter the ratio of the circumference of a circle to its diameter.
        It is useful in combination with the trigonometric functions sin() and cos().
        """,
    ]
    TAU: Annotated[
        float,
        """TAU is an alias for TWO_PI, a mathematical constant with the value 6.28318530717958647693. It is twice the ratio of the circumference of a circle to its diameter.
        It is useful in combination with the trigonometric functions sin() and cos().
        """,
    ]
    TWO_PI: Annotated[
        float,
        """TWO_PI is a mathematical constant with the value 6.28318530717958647693. It is twice the ratio of the circumference of a circle to its diameter.
        It is useful in combination with the trigonometric functions sin() and cos().
        """,
    ]
    DEGREES: Annotated[
        str,
        "Constant to be used with the angle_mode() function, to set the mode in which p5 interprets and calculates angles (either DEGREES or RADIANS).",
    ]
    RADIANS: Annotated[
        str,
        "Constant to be used with the angle_mode() function, to set the mode in which p5 interprets and calculates angles (either RADIANS or DEGREES).",
    ]

    # SHAPE
    CORNER: str

    CORNERS: str

    RADIUS: str

    RIGHT: str

    LEFT: str

    CENTER: str

    TOP: str

    BOTTOM: str

    BASELINE: str

    POINTS: float

    LINES: float

    LINE_STRIP: float

    LINE_LOOP: float

    TRIANGLES: float

    TRIANGLE_FAN: float

    TRIANGLE_STRIP: float

    QUADS: str

    QUAD_STRIP: str

    TESS: str

    CLOSE: str

    OPEN: str

    CHORD: str

    PIE: str

    PROJECT: str

    SQUARE: str

    ROUND: str

    BEVEL: str

    MITER: str

    # COLOR
    RGB: str

    HSB: Annotated[
        str,
        """HSB (hue, saturation, brightness) is a type of color model. You can learn more about it at
    https://learnui.design/blog/the-hsb-color-system-practicioners-primer.html
    """,
    ]

    HSL: str

    # DOM EXTENSION
    AUTO: Annotated[
        str,
        """AUTO allows us to automatically set the width or height of an element
    (but not both), based on the current height and width of the element.
    Only one parameter can be passed to size() function as AUTO, at a time.
    """,
    ]

    # INPUT
    ALT: int

    BACKSPACE: int

    CONTROL: int

    DELETE: int

    DOWN_ARROW: int

    ENTER: int

    ESCAPE: int

    LEFT_ARROW: int

    OPTION: int

    RETURN: int

    RIGHT_ARROW: int

    SHIFT: int

    TAB: int

    UP_ARROW: int

    # RENDERING
    BLEND: str

    REMOVE: str

    ADD: str

    DARKEST: str

    LIGHTEST: str

    DIFFERENCE: str

    SUBTRACT: str

    EXCLUSION: str

    MULTIPLY: str

    SCREEN: str

    REPLACE: str

    OVERLAY: str

    HARD_LIGHT: str

    SOFT_LIGHT: str

    DODGE: str

    BURN: str

    # FILTERS
    THRESHOLD: str

    GRAY: str

    OPAQUE: str

    INVERT: str

    POSTERIZE: str

    DILATE: str

    ERODE: str

    BLUR: str

    # TYPOGRAPHY
    NORMAL: str

    ITALIC: str

    BOLD: str

    BOLDITALIC: str

    CHAR: str

    WORD: str

    # VERTICES
    LINEAR: str

    QUADRATIC: str

    BEZIER: str

    CURVE: str

    # WEBGL DRAWMODES

    STROKE: str

    FILL: str

    TEXTURE: str

    IMMEDIATE: str

    # WEBGL TEXTURE MODE
    # NORMAL already exists for typography
    IMAGE: str

    # WEBGL TEXTURE WRAP AND FILTERING
    # LINEAR already exists above
    NEAREST: str

    REPEAT: str

    CLAMP: str

    MIRROR: str

    # DEVICE-ORIENTATION
    LANDSCAPE: str

    PORTRAIT: str

    # ACCESSIBILITY

    GRID: str

    AXES: str

    LABEL: str

    FALLBACK: str

    CONTAIN: str

    COVER: str

    # CAMERA
    VIDEO: str

    AUDIO: str

    def _init_constants(self):
        # GRAPHICS RENDERER
        self.P2D = self._p5js.P2D
        self.WEBGL = self._p5js.WEBGL

        # TRIGONOMETRY
        self.HALF_PI = self._p5js.HALF_PI
        self.PI = self._p5js.PI
        self.QUARTER_PI = self._p5js.QUARTER_PI
        self.TAU = self._p5js.TAU
        self.TWO_PI = self._p5js.TWO_PI
        self.DEGREES = self._p5js.DEGREES
        self.RADIANS = self._p5js.RADIANS

        # SHAPE
        self.CORNER = self._p5js.CORNER

        self.CORNERS = self._p5js.CORNERS

        self.RADIUS = self._p5js.RADIUS

        self.RIGHT = self._p5js.RIGHT

        self.LEFT = self._p5js.LEFT

        self.CENTER = self._p5js.CENTER

        self.TOP = self._p5js.TOP

        self.BOTTOM = self._p5js.BOTTOM

        self.BASELINE = self._p5js.BASELINE

        self.POINTS = self._p5js.POINTS

        self.LINES = self._p5js.LINES

        self.LINE_STRIP = self._p5js.LINE_STRIP

        self.LINE_LOOP = self._p5js.LINE_LOOP

        self.TRIANGLES = self._p5js.TRIANGLES

        self.TRIANGLE_FAN = self._p5js.TRIANGLE_FAN

        self.TRIANGLE_STRIP = self._p5js.TRIANGLE_STRIP

        self.QUADS = self._p5js.QUADS

        self.QUAD_STRIP = self._p5js.QUAD_STRIP

        self.TESS = self._p5js.TESS

        self.CLOSE = self._p5js.CLOSE

        self.OPEN = self._p5js.OPEN

        self.CHORD = self._p5js.CHORD

        self.PIE = self._p5js.PIE

        self.PROJECT = self._p5js.PROJECT  # PEND: careful this is counterintuitive

        self.SQUARE = self._p5js.SQUARE

        self.ROUND = self._p5js.ROUND

        self.BEVEL = self._p5js.BEVEL

        self.MITER = self._p5js.MITER

        # COLOR
        self.RGB = self._p5js.RGB

        self.HSB = self._p5js.HSB

        self.HSL = self._p5js.HSL

        # DOM EXTENSION
        self.AUTO = self._p5js.AUTO

        # INPUT
        self.ALT = self._p5js.ALT

        self.BACKSPACE = self._p5js.BACKSPACE

        self.CONTROL = self._p5js.CONTROL

        self.DELETE = self._p5js.DELETE

        self.DOWN_ARROW = self._p5js.DOWN_ARROW

        self.ENTER = self._p5js.ENTER

        self.ESCAPE = self._p5js.ESCAPE

        self.LEFT_ARROW = self._p5js.LEFT_ARROW

        self.OPTION = self._p5js.OPTION

        self.RETURN = self._p5js.RETURN

        self.RIGHT_ARROW = self._p5js.RIGHT_ARROW

        self.SHIFT = self._p5js.SHIFT

        self.TAB = self._p5js.TAB

        self.UP_ARROW = self._p5js.UP_ARROW

        # RENDERING
        self.BLEND = self._p5js.BLEND

        self.REMOVE = self._p5js.REMOVE

        self.ADD = self._p5js.ADD

        self.DARKEST = self._p5js.DARKEST

        self.LIGHTEST = self._p5js.LIGHTEST

        self.DIFFERENCE = self._p5js.DIFFERENCE

        self.SUBTRACT = self._p5js.SUBTRACT

        self.EXCLUSION = self._p5js.EXCLUSION

        self.MULTIPLY = self._p5js.MULTIPLY

        self.SCREEN = self._p5js.SCREEN

        self.REPLACE = self._p5js.REPLACE

        self.OVERLAY = self._p5js.OVERLAY

        self.HARD_LIGHT = self._p5js.HARD_LIGHT

        self.SOFT_LIGHT = self._p5js.SOFT_LIGHT

        self.DODGE = self._p5js.DODGE

        self.BURN = self._p5js.BURN

        # FILTERS
        self.THRESHOLD = self._p5js.THRESHOLD

        self.GRAY = self._p5js.GRAY

        self.OPAQUE = self._p5js.OPAQUE

        self.INVERT = self._p5js.INVERT

        self.POSTERIZE = self._p5js.POSTERIZE

        self.DILATE = self._p5js.DILATE

        self.ERODE = self._p5js.ERODE

        self.BLUR = self._p5js.BLUR

        # TYPOGRAPHY
        self.NORMAL = self._p5js.NORMAL

        self.ITALIC = self._p5js.ITALIC

        self.BOLD = self._p5js.BOLD

        self.BOLDITALIC = self._p5js.BOLDITALIC

        self.CHAR = self._p5js.CHAR

        self.WORD = self._p5js.WORD

        # VERTICES
        self.LINEAR = self._p5js.LINEAR

        self.QUADRATIC = self._p5js.QUADRATIC

        self.BEZIER = self._p5js.BEZIER

        self.CURVE = self._p5js.CURVE

        # WEBGL DRAWMODES

        self.STROKE = self._p5js.STROKE

        self.FILL = self._p5js.FILL

        self.TEXTURE = self._p5js.TEXTURE

        self.IMMEDIATE = self._p5js.IMMEDIATE

        # WEBGL TEXTURE MODE
        # NORMAL already exists for typography
        self.IMAGE = self._p5js.IMAGE

        # WEBGL TEXTURE WRAP AND FILTERING
        # LINEAR already exists above
        self.NEAREST = self._p5js.NEAREST

        self.REPEAT = self._p5js.REPEAT

        self.CLAMP = self._p5js.CLAMP

        self.MIRROR = self._p5js.MIRROR

        # DEVICE-ORIENTATION
        self.LANDSCAPE = self._p5js.LANDSCAPE

        self.PORTRAIT = self._p5js.PORTRAIT

        # ACCESSIBILITY

        self.GRID = self._p5js.GRID

        self.AXES = self._p5js.AXES

        self.LABEL = self._p5js.LABEL

        self.FALLBACK = self._p5js.FALLBACK

        self.CONTAIN = self._p5js.CONTAIN

        self.COVER = self._p5js.COVER

        # CAMERA
        self.VIDEO = self._p5js.VIDEO

        self.AUDIO = self._p5js.AUDIO
