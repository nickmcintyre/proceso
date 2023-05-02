from ._binding import BaseSketch


class Environment(BaseSketch):
    def describe(self, text: str, display: str | None = None):
        """Creates a screen reader accessible description for the canvas.
        The first parameter should be a string with a description of the canvas.
        The second parameter is optional. If specified, it determines how the
        description is displayed.

        describe(text, LABEL) displays the description to all users as a tombstone
        or exhibit label/caption in a div adjacent to the canvas. You can style it
        as you wish in your CSS.

        describe(text, FALLBACK) makes the description accessible to screen-reader
        users only, in a sub DOM inside the canvas element. If a second parameter
        is not specified, by default, the description will only be available to
        screen-reader users.
        """
        self._p5js.describe(text, display)

    def describe_element(self, name: str, text: str, display: str | None = None):
        """This function creates a screen-reader accessible description for
        elements —shapes or groups of shapes that create meaning together— in
        the canvas.
        The first paramater should be the name of the element. The second
        parameter should be a string with a description of the element. The third
        parameter is optional. If specified, it determines how the element
        description is displayed.

        describe_element(name, text, LABEL) displays the element description to
        all users as a tombstone or exhibit label/caption in a div adjacent to
        the canvas. You can style it as you wish in your CSS.

        describe_element(name, text, FALLBACK) makes the element description
        accessible to screen-reader users only, in a sub DOM inside the canvas
        element. If a second parameter is not specified, by default, the element
        description will only be available to screen-reader users.
        """
        self._p5js.describeElement(name, text, display)

    def text_output(self, display: str | None = None):
        """text_output() creates a screenreader accessible output that describes
        the shapes present on the canvas. The general description of the canvas
        includes canvas size, canvas color, and number of elements in the canvas
        (example: 'Your output is a, 400 by 400 pixels, lavender blue canvas
        containing the following 4 shapes:'). This description is followed by a
        list of shapes where the color, position, and area of each shape are
        described (example: "orange ellipse at top left covering 1% of the
        canvas"). Each element can be selected to get more details. A table of
        elements is also provided. In this table, shape, color, location,
        coordinates and area are described (example: "orange ellipse
        location=top left area=2").

        text_output() and text_output(FALLBACK) make the output available in a
        sub DOM inside the canvas element which is accessible to screen readers.
        text_output(LABEL) creates an additional div with the output adjacent to
        the canvas, this is useful for non-screen reader users that might want to
        display the output outside of the canvas' sub DOM as they code. However,
        using LABEL will create unnecessary redundancy for screen reader users.
        We recommend using LABEL only as part of the development process of a
        sketch and removing it before publishing or sharing with screen reader
        users.
        """
        self._p5js.textOutput(display)

    def grid_output(self, display: str | None = None):
        """grid_output() lays out the content of the canvas in the form of a grid
        (html table) based on the spatial location of each shape.
        A brief description of the canvas is available before the table output.
        This description includes: color of the background, size of the canvas,
        number of objects, and object types (example: "lavender blue canvas is
        200 by 200 and contains 4 objects - 3 ellipses 1 rectangle"). The grid
        describes the content spatially, each element is placed on a cell of the
        table depending on its position. Within each cell an element the color
        and type of shape of that element are available (example:
        "orange ellipse"). These descriptions can be selected individually to
        get more details. A list of elements where shape, color, location, and
        area are described (example: "orange ellipse location=top left area=1%")
        is also available.

        grid_output() and grid_output(FALLBACK) make the output available in a
        sub DOM inside the canvas element which is accessible to screen readers.
        grid_output(LABEL) creates an additional div with the output adjacent to
        the canvas, this is useful for non-screen reader users that might want to
        display the output outside of the canvas' sub DOM as they code. However,
        using LABEL will create unnecessary redundancy for screen reader users.
        We recommend using LABEL only as part of the development process of a
        sketch and removing it before publishing or sharing with screen reader
        users.
        """
        self._p5js.gridOutput(display)

    def cursor(self, type: str, x: float | None = None, y: float | None = None):
        """Sets the cursor to a predefined symbol or an image, or makes it
        visible if already hidden.
        If you are trying to set an image as the cursor, the recommended size is
        16×16 or 32×32 pixels. The values for parameters x and y must be less than
        the dimensions of the image.
        """
        self._p5js.cursor(type, x, y)

    def frame_rate(self, fps: float | None = None) -> float | None:
        """Specifies the number of frames to be displayed every second.
        For example, the function call frame_rate(30) will attempt to refresh 30
        times a second. If the processor is not fast enough to maintain the
        specified rate, the frame rate will not be achieved. Setting the frame
        rate within setup() is recommended. The default frame rate is based on the
        frame rate of the display (here also called "refresh rate"), which is set
        to 60 frames per second on most computers. A frame rate of 24 frames per
        second (usual for movies) or above will be enough for smooth animations.

        Calling frame_rate() with no arguments returns the current framerate. The
        draw function must run at least once before it will return a value. This
        is the same as get_frame_rate().

        Calling frame_rate() with arguments that are not of the type Number or are
        non-positive also returns current framerate.
        """
        return self._p5js.frameRate(fps)

    def get_target_frame_rate(self) -> float:
        """Returns _targetFrameRate variable.
        The default _targetFrameRate is set to 60. This could be changed by
        calling frame_rate() and setting it to the desired value. When
        get_target_frame_rate() is called, it should return the value that was set.
        """
        return self._p5js.getTargetFrameRate()

    def hide_cursor(self):
        """Hides the cursor from view."""
        self._p5js.hideCursor()

    def fullscreen(self, val: bool | None = None) -> bool:
        """If argument is given, sets the sketch to fullscreen or not based on the
        value of the argument.
        If no argument is given, returns the current fullscreen state. Note that
        due to browser restrictions this can only be called on user input, for
        example, on mouse press like the example below.
        """
        return self._p5js.fullscreen(val)

    def pixel_density(self, val: float) -> float | None:
        """Sets the pixel scaling for high pixel density displays.
        By default pixel density is set to match display density, call
        pixel_density(1) to turn this off. Calling pixel_density() with no
        arguments returns the current pixel density of the sketch.
        """
        return self._p5js.pixelDensity(val)

    def display_density(self) -> float:
        """Returns the pixel density of the current display the sketch is running
        on.
        """
        return self._p5js.displayDensity()

    def get_url(self) -> str:
        """Gets the current URL."""
        return self._p5js.getURL()

    def get_url_path(self) -> list[str]:
        """Gets the current URL path as an array."""
        return self._p5js.getURLPath()

    def get_url_params(self) -> dict:
        """Gets the current URL params as a dictionary."""
        return self._p5js.getURLParams()
