from ._binding import BaseSketch


class Typography(BaseSketch):
    # ==========
    # Attributes
    # ==========
    def text_align(self, horiz_align: str, vert_align: str | None = None):
        """Sets the current alignment for drawing text.
        Accepts two arguments: horiz_align (LEFT, CENTER, or RIGHT) and
        vert_align (TOP, BOTTOM, CENTER, or BASELINE).

        The horiz_align parameter is in reference to the x value of the text()
        function, while the vert_align parameter is in reference to the y value.

        So if you write text_align(LEFT), you are aligning the left edge of your
        text to the x value you give in text(). If you write
        text_align(RIGHT, TOP), you are aligning the right edge of your text to
        the x value and the top edge of the text to the y value.
        """
        self._p5js.textAlign(horiz_align, vert_align)

    def text_leading(self, leading: float):
        """Sets/gets the spacing, in pixels, between lines of text.
        This setting will be used in all subsequent calls to the text() function.
        """
        self._p5js.textAlign(leading)

    def text_size(self, size: float) -> float:
        """Sets/gets the current font size.
        This size will be used in all subsequent calls to the text() function.
        Font size is measured in pixels.
        """
        return self._p5js.textSize(size)

    def text_style(self, style: str):
        """Sets/gets the style of the text for system fonts to NORMAL, ITALIC,
        BOLD or BOLDITALIC.
        Note: this may be is overridden by CSS styling. For non-system fonts
        (opentype, truetype, etc.) please load styled fonts instead.
        """
        self._p5js.textStyle(style)

    def text_width(self, text: str) -> float:
        """Calculates and returns the width of any character or text string."""
        return self._p5js.textWidth(text)

    def text_ascent(self) -> float:
        """Returns the ascent of the current font at its current size.
        The ascent represents the distance, in pixels, of the tallest character
        above the baseline.
        """
        return self._p5js.textAscent()

    def text_descent(self) -> float:
        """Returns the descent of the current font at its current size.
        The descent represents the distance, in pixels, of the character with the
        longest descender below the baseline.
        """
        return self._p5js.textDescent()

    def text_wrap(self, style: str):
        """Specifies how lines of text are wrapped within a text box.
        This requires a max-width set on the text area, specified in text() as
        parameter x2.

        WORD wrap style only breaks lines at spaces. A single string without
        spaces that exceeds the boundaries of the canvas or text area is not
        truncated, and will overflow the desired area, disappearing at the canvas
        edge.

        CHAR wrap style breaks lines wherever needed to stay within the text box.

        WORD is the default wrap style, and both styles will still break lines at
        any line breaks (\n) specified in the original text. The text area
        max-height parameter (y2) also still applies to wrapped text in both
        styles, lines of text that do not fit within the text area will not be
        drawn to the screen.
        """
        self._p5js.textWrap(style)

    # ====================
    # Loading & Displaying
    # ====================
    def load_font(self, path: str) -> object:
        """Loads an opentype font file (.otf, .ttf) from a file or a URL, and
        returns a p5.Font object.
        This function is asynchronous, meaning it may not finish before the next
        line in your sketch is executed.

        The path to the font should be relative to the HTML file that links in
        your sketch. Loading fonts from a URL or other remote location may be
        blocked due to your browser's built-in security.
        """
        return self._p5js.loadFont(path)

    def text(
        self,
        txt: str,
        x: float,
        y: float,
        x2: float | None = None,
        y2: float | None = None,
    ):
        """Draws text to the screen.
        Displays the information specified in the first parameter on the screen in
        the position specified by the additional parameters. A default font will
        be used unless a font is set with the textFont() function and a default
        size will be used unless a font is set with text_size(). Change the color
        of the text with the fill() function. Change the outline of the text with
        the stroke() and strokeWeight() functions.

        The text displays in relation to the text_align() function, which gives
        the option to draw to the left, right, and center of the coordinates.

        The x2 and y2 parameters define a rectangular area to display within and
        may only be used with string data. When these parameters are specified,
        they are interpreted based on the current rect_mode() setting. Text that
        does not fit completely within the rectangle specified will not be drawn
        to the screen. If x2 and y2 are not specified, the baseline alignment is
        the default, which means that the text will be drawn upwards from x and y.

        WEBGL: Only opentype/truetype fonts are supported. You must load a font
        using the loadFont() method (see the example above). stroke() currently
        has no effect in WebGL mode. Learn more about working with text in WebGL
        mode on the wiki.
        """
        self._p5js.text(txt, x, y, x2, y2)

    def text_font(self, font: str | object, size: float | None = None):
        """Sets the current font that will be drawn with the text() function.
        If text_font() is called without any argument, it will return the current
        font if one has been set already. If not, it will return the name of the
        default font as a string. If text_font() is called with a font to use, it
        will return the p5 object.

        WEBGL: Only fonts loaded via load_font() are supported.
        """
        self._p5js.textFont(font, size)
