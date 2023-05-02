from pyodide.ffi import to_js

from ._binding import BaseSketch


class Images(BaseSketch):
    def create_image(self, width: int, height: int) -> object:
        """Creates a new p5.Image (the datatype for storing images).
        This provides a fresh buffer of pixels to play with. Set the size of the
        buffer with the width and height parameters.

        .pixels gives access to a list containing the values for all the pixels
        in the display window. These values are numbers. This list is the size
        (including an appropriate factor for the pixel_density) of the display
        window x4, representing the R, G, B, A values in order for each pixel,
        moving from left to right across each row, then down each column. See
        .pixels for more info. It may also be simpler to use set_pixels() or get_pixels().

        Before accessing the pixels of an image, the data must loaded with the
        load_pixels() function. After the list data has been modified, the
        update_pixels() function must be run to update the changes.
        """
        return self._p5js.createImage(width, height)

    def save_canvas(self, filename: str, extension: str):
        """Save the current canvas as an image.
        The browser will either save the file immediately, or prompt the user
        with a dialogue window.
        """
        self._p5js.saveCanvas(filename, extension)

    def save_frames(
        self,
        filename: str,
        extension: str,
        duration: float,
        framerate: float,
    ):
        """Capture a sequence of frames that can be used to create a movie.
        Accepts a callback. For example, you may wish to send the frames to a
        server where they can be stored or converted into a movie. If no
        callback is provided, the browser will pop up save dialogues in an
        attempt to download all of the images that have just been created. With
        the callback provided the image data isn't saved by default but instead
        passed as an argument to the callback function as a list of objects,
        with the size of list equal to the total number of frames.

        The arguments duration and framerate are constrained to be less or equal
        to 15 and 22, respectively, which means you can only download a maximum of
        15 seconds worth of frames at 22 frames per second, adding up to 330
        frames. This is done in order to avoid memory problems since a large
        enough canvas can fill up the memory in your computer very easily and
        crash your program or even your browser.

        To export longer animations, you might look into a library like
        ccapture.js.
        """
        self._p5js.saveFrames(filename, extension, duration, framerate)

    # ====================
    # Loading & Displaying
    # ====================
    def load_image(self, path: str) -> object:
        """Loads an image from a path and creates a p5.Image from it.

        The image may not be immediately available for rendering. If you want to
        ensure that the image is ready before doing anything with it, place the
        loadImage() call in preload(). You may also supply a callback function to
        handle the image when it's ready.

        The path to the image should be relative to the HTML file that links in
        your sketch. Loading an image from a URL or other remote location may be
        blocked due to your browser's built-in security.

        You can also pass in a string of a base64 encoded image as an alternative
        to the file path. Remember to add "data:image/png;base64," in front of the
        string.
        """
        return self._p5js.loadImage(path)

    def save_gif(
        self,
        filename: str,
        duration: int,
        options: dict | None = None,
    ):
        """Generates a gif of your current animation and downloads it to your
        computer!

        The duration argument specifies how many seconds you want to record from
        your animation. This value is then converted to the necessary number of
        frames to generate it, depending on the value of units. More on that on
        the next paragraph.

        An optional object that can contain two more arguments: delay (number) and
        units (string).

        delay, specifying how much time we should wait before recording

        units, a string that can be either 'seconds' or 'frames'. By default it's
        'seconds'.

        units specifies how the duration and delay arguments will behave. If
        'seconds', these arguments will correspond to seconds, meaning that 3
        seconds worth of animation will be created. If 'frames', the arguments
        now correspond to the number of frames you want your animation to be, if
        you are very sure of this number.

        This may be called in setup, or, like in the example below, inside an
        event function, like key_pressed or mouse_pressed.
        """
        self._p5js.saveGif(filename, duration, options)

    def image(
        self,
        img: object,
        x: float,
        y: float,
        width: float | None = None,
        height: float | None = None,
    ):
        """Draw an image to the p5 canvas.

        This function can be used with different numbers of parameters. The
        simplest use requires only three parameters: img, x, and y—where (x, y) is
        the position of the image. Two more parameters can optionally be added to
        specify the width and height of the image.

        This function can also be used with eight Number parameters. To
        differentiate between all these parameters, p5.js uses the language of
        "destination rectangle" (which corresponds to "dx", "dy", etc.) and
        "source image" (which corresponds to "sx", "sy", etc.) below. Specifying
        the "source image" dimensions can be useful when you want to display a
        subsection of the source image instead of the whole thing.
        """
        self._p5js.image(img, x, y, width, height)

    def tint(
        self,
        value: str | int | list[int],
        v2: int | None = None,
        v3: int | None = None,
        v4: int | None = None,
    ):
        """Sets the fill value for displaying images.
        Images can be tinted to specified colors or made transparent by including
        an alpha value.

        To apply transparency to an image without affecting its color, use white
        as the tint color and specify an alpha value. For instance, tint(255, 128)
        will make an image 50% transparent (assuming the default alpha range of
        0-255, which can be changed with color_mode()).

        The value for the gray parameter must be less than or equal to the current
        maximum value as specified by color_mode(). The default maximum value is
        255.
        """
        if v4:
            self._p5js.tint(value, v2, v3, v4)
        elif v3:
            self._p5js.tint(value, v2, v3)
        elif v2:
            self._p5js.tint(value, v2)
        else:
            self._p5js.tint(to_js(value))

    def no_tint(self):
        """Removes the current fill value for displaying images and reverts to
        displaying images with their original hues.
        """
        self._p5js.noTint()

    def image_mode(self, mode: str):
        """Set image mode. Modifies the location from which images are drawn by
        changing the way in which parameters given to image() are interpreted.
        The default mode is image_mode(CORNER), which interprets the second and
        third parameters of image() as the upper-left corner of the image. If two
        additional parameters are specified, they are used to set the image's
        width and height.

        image_mode(CORNERS) interprets the second and third parameters of image()
        as the location of one corner, and the fourth and fifth parameters as the
        opposite corner.

        image_mode(CENTER) interprets the second and third parameters of image() as
        the image's center point. If two additional parameters are specified, they
        are used to set the image's width and height.
        """
        self._p5js.imageMode(mode)

    # ======
    # Pixels
    # ======
    def blend(
        self,
        src_image: object,
        sx: int,
        sy: int,
        sw: int,
        sh: int,
        dx: int,
        dy: int,
        dw: int,
        dh: int,
        blend_mode: str,
    ):
        """Copies a region of pixels from one image to another, using a specified
        blend mode to do the operation.
        """
        self._p5js.blend(src_image, sx, sy, sw, sh, dx, dy, dw, dh, blend_mode)

    def copy(
        self,
        src_image: object,
        sx: int,
        sy: int,
        sw: int,
        sh: int,
        dx: int,
        dy: int,
        dw: int,
        dh: int,
    ):
        """Copies a region of the canvas to another region of the canvas and
        copies a region of pixels from an image used as the srcImg parameter into
        the canvas src_image is specified this is used as the source.
        If the source and destination regions aren't the same size, it will
        automatically resize source pixels to fit the specified target region.
        """
        self._p5js.copy(src_image, sx, sy, sw, sh, dx, dy, dw, dh)

    def apply_filter(self, filter_type: str, filter_param: float | None = None):
        """Applies a filter to the canvas.
        The presets options are:

        THRESHOLD Converts the image to black and white pixels depending if they
        are above or below the threshold defined by the level parameter. The
        parameter must be between 0.0 (black) and 1.0 (white). If no level is
        specified, 0.5 is used.

        GRAY Converts any colors in the image to grayscale equivalents. No
        parameter is used.

        OPAQUE Sets the alpha channel to entirely opaque. No parameter is used.

        INVERT Sets each pixel to its inverse value. No parameter is used.

        POSTERIZE Limits each channel of the image to the number of colors
        specified as the parameter. The parameter can be set to values between 2
        and 255, but results are most noticeable in the lower ranges.

        BLUR Executes a Gaussian blur with the level parameter specifying the
        extent of the blurring. If no parameter is used, the blur is equivalent to
        Gaussian blur of radius 1. Larger values increase the blur.

        ERODE Reduces the light areas. No parameter is used.

        DILATE Increases the light areas. No parameter is used.

        apply_filter() does not work in WEBGL mode. A similar effect can be achieved in
        WEBGL mode using custom shaders. Adam Ferriss has written a selection of
        shader examples that contains many of the effects present in the filter
        examples.
        """
        self._p5js.filter(filter_type, filter_param)

    def get_pixels(
        self, x: int, y: int, width: int | None = None, height: int | None = None
    ) -> list[float] | object:
        """Get a region of pixels, or a single pixel, from the canvas.

        Returns a list of [R,G,B,A] values for any pixel or grabs a section of
        an image. If no parameters are specified, the entire image is returned.
        Use the x and y parameters to get the value of one pixel. Get a section of
        the display window by specifying additional w and h parameters. When
        getting an image, the x and y parameters define the coordinates for the
        upper-left corner of the image, regardless of the current image_mode().

        Getting the color of a single pixel with get_pixels(x, y) is easy, but not as
        fast as grabbing the data directly from pixels[].
        """
        return self._p5js.get(x, y, width, height)

    def load_pixels(self):
        """Loads the pixel data for the display window into the pixels[] list.
        This function must always be called before reading from or writing to
        pixels[]. Note that only changes made with set_pixels() or direct manipulation of
        pixels[] will occur.
        """
        self._p5js.loadPixels()

    def set_pixels(self, x: int, y: int, c: float | list[float] | object):
        """Changes the color of any pixel, or writes an image directly to the
        display window.
        The x and y parameters specify the pixel to change and the c parameter
        specifies the color value. This can be a p5.Color object, or [R, G, B, A]
        pixel list. It can also be a single grayscale value. When setting an
        image, the x and y parameters define the coordinates for the upper-left
        corner of the image, regardless of the current imageMode().

        After using set_pixels(), you must call update_pixels() for your changes to
        appear. This should be called once all pixels have been set, and must be
        called before calling get_pixels() or drawing the image.

        Setting the color of a single pixel with set_pixels(x, y) is easy, but not as
        fast as putting the data directly into pixels[]. Setting the pixels[]
        values directly may be complicated when working with a retina display, but
        will perform better when lots of pixels need to be set directly on every
        loop. See the reference for pixels[] for more information.
        """
        self._p5js.set(x, y, c)

    def update_pixels(self):
        """Updates the display window with the data in the pixels[] list.
        Use in conjunction with loadPixels(). If you're only reading pixels from
        the list, there's no need to call update_pixels() — updating is only
        necessary to apply changes. update_pixels() should be called anytime the
        pixels list is manipulated or set_pixels() is called, and only changes made with
        set_pixels() or direct changes to pixels[] will occur.
        """
        self._p5js.updatePixels()
