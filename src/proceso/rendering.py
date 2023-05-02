from typing import Any

from ._binding import BaseSketch


class Rendering(BaseSketch):
    def create_canvas(
        self, width: int, height: int, renderer: str | None = None
    ) -> object:
        """Creates a canvas element in the document and sets its dimensions in
        pixels. Alias of size().

        This method should be called only once at the start of setup(). Calling
        create_canvas() more than once in a sketch will result in very unpredictable
        behavior. If you want more than one drawing canvas you could use
        create_graphics() (hidden by default but it can be shown).

        Important note: in 2D mode (i.e. when p5.Renderer is not set) the origin
        (0,0) is positioned at the top left of the screen. In 3D mode (i.e. when
        p5.Renderer is set to WEBGL), the origin is positioned at the center of
        the canvas. See this issue for more information.

        The system variables width and height are set by the parameters passed to
        this function. If create_canvas() is not used, the window will be given a
        default size of 100×100 pixels.
        """
        self.width = width
        self.height = height
        return self._p5js.createCanvas(width, height, renderer)

    def size(self, width: int, height: int, renderer: str | None = None) -> object:
        """Creates a canvas element in the document and sets its dimensions in
        pixels. Alias of create_canvas().

        This method should be called only once at the start of setup(). Calling
        size() more than once in a sketch will result in very unpredictable
        behavior. If you want more than one drawing canvas you could use
        create_graphics() (hidden by default but it can be shown).

        Important note: in 2D mode (i.e. when p5.Renderer is not set) the origin
        (0,0) is positioned at the top left of the screen. In 3D mode (i.e. when
        p5.Renderer is set to WEBGL), the origin is positioned at the center of
        the canvas. See this issue for more information.

        The system variables width and height are set by the parameters passed to
        this function. If size() is not used, the window will be given a
        default size of 100×100 pixels.
        """
        return self._p5js.createCanvas(width, height, renderer)

    def resize_canvas(self, width: int, height: int, no_redraw: bool | None = None):
        """Resizes the canvas to given width and height.
        The canvas will be cleared and draw will be called immediately, allowing
        the sketch to re-render itself in the resized canvas.
        """
        self._p5js.resizeCanvas(width, height, no_redraw)

    def no_canvas(self):
        """Removes the default canvas for a p5 sketch that doesn't require a
        canvas.
        """
        self._p5js.noCanvas()

    def create_graphics(
        self, width: int, height: int, renderer: str | None = None
    ) -> object:
        """Creates and returns a new p5.Renderer object.
        Use this class if you need to draw into an off-screen graphics buffer. The
        two parameters define the width and height in pixels.
        """
        return self._p5js.createGraphics(width, height, renderer)

    def blend_mode(self, mode: str):
        """Blends the pixels in the display window according to the defined mode.
        There is a choice of the following modes to blend the source pixels (A)
        with the ones of pixels already in the display window (B):

        BLEND - linear interpolation of colours: C = A*factor + B. This is the
        default blending mode.
        ADD - sum of A and B
        DARKEST - only the darkest colour succeeds: C = min(A*factor, B).
        LIGHTEST - only the lightest colour succeeds: C = max(A*factor, B).
        DIFFERENCE - subtract colors from underlying image. (2D)
        EXCLUSION - similar to DIFFERENCE, but less extreme.
        MULTIPLY - multiply the colors, result will always be darker.
        SCREEN - opposite multiply, uses inverse values of the colors.
        REPLACE - the pixels entirely replace the others and don't utilize alpha
        (transparency) values.
        REMOVE - removes pixels from B with the alpha strength of A.
        OVERLAY - mix of MULTIPLY and SCREEN . Multiplies dark values, and screens
        light values. (2D)
        HARD_LIGHT - SCREEN when greater than 50% gray, MULTIPLY when lower. (2D)
        SOFT_LIGHT - mix of DARKEST and LIGHTEST. Works like OVERLAY, but not as
        harsh. (2D)
        DODGE - lightens light tones and increases contrast, ignores darks. (2D)
        BURN - darker areas are applied, increasing contrast, ignores lights. (2D)
        SUBTRACT - remainder of A and B (3D)

        (2D) indicates that this blend mode only works in the 2D renderer.
        (3D) indicates that this blend mode only works in the WEBGL renderer.
        """
        self._p5js.blendMode(mode)

    def set_attributes(self, key: str, value: Any):
        """Set attributes for the WebGL Drawing context.
        This is a way of adjusting how the WebGL renderer works to fine-tune the
        display and performance.

        Note that this will reinitialize the drawing context if called after the
        WebGL canvas is made.

        If an object is passed as the parameter, all attributes not declared in
        the object will be set to defaults.

        The available attributes are:
        alpha - indicates if the canvas contains an alpha buffer default is True

        depth - indicates whether the drawing buffer has a depth buffer of at
        least 16 bits - default is True

        stencil - indicates whether the drawing buffer has a stencil buffer of at
        least 8 bits

        antialias - indicates whether or not to perform anti-aliasing default is
        False (True in Safari)

        premultipliedAlpha - indicates that the page compositor will assume the
        drawing buffer contains colors with pre-multiplied alpha default is True

        preserveDrawingBuffer - if true the buffers will not be cleared and and
        will preserve their values until cleared or overwritten by author
        (note that p5 clears automatically on draw loop) default is True

        perPixelLighting - if True, per-pixel lighting will be used in the
        lighting shader otherwise per-vertex lighting is used. default is True.
        """
        self._p5js.setAttributes(key, value)
