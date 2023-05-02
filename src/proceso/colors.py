from typing import Any
from pyodide.ffi import to_js

from ._binding import BaseSketch


class Colors(BaseSketch):
    # ==================
    # Creating & Reading
    # ==================
    def alpha(self, color: list[int] | str) -> int:
        """Extracts the alpha value from a color or pixel array."""
        if isinstance(color, list):
            return self._p5js.alpha(to_js(color))
        return self._p5js.alpha(color)

    def blue(self, color: list[int] | str) -> int:
        """Extracts the blue value from a color or pixel array."""
        if isinstance(color, list):
            return self._p5js.blue(to_js(color))
        return self._p5js.blue(color)

    def brightness(self, color: list[int] | str) -> int:
        """Extracts the HSB brightness value from a color or pixel array."""
        if isinstance(color, list):
            return self._p5js.brightness(to_js(color))
        return self._p5js.brightness(color)

    def color(
        self,
        value: str | int | list[int],
        v2: int | None = None,
        v3: int | None = None,
        v4: int | None = None,
    ) -> str:
        """Creates colors for storing in variables of the color datatype.
        The parameters are interpreted as RGB or HSB values depending on the
        current color_mode(). The default mode is RGB values from 0 to 255 and,
        therefore, the function call color(255, 204, 0) will return a bright
        yellow color.

        Note that if only one value is provided to color(), it will be interpreted
        as a grayscale value. Add a second value, and it will be used for alpha
        transparency. When three values are specified, they are interpreted as
        either RGB or HSB values. Adding a fourth value applies alpha
        transparency.

        If a single string argument is provided, RGB, RGBA and Hex CSS color
        strings and all named color strings are supported. In this case, an alpha
        number value as a second argument is not supported, the RGBA form should
        be used.
        """
        if v4:
            return self._p5js.color(value, v2, v3, v4).toString()
        if v3:
            return self._p5js.color(value, v2, v3).toString()
        if v2:
            return self._p5js.color(value, v2).toString()
        return self._p5js.color(to_js(value)).toString()

    def green(self, color: str | list[int]) -> int:
        """Extracts the green value from a color or pixel array."""
        if isinstance(color, list):
            return self._p5js.green(to_js(color))
        return self._p5js.green(color)

    def hue(self, color: str | list[int]) -> int:
        """Extracts the hue value from a color or pixel array.

        Hue exists in both HSB and HSL. This function will return the
        HSB-normalized hue when supplied with an HSB color object (or when
        supplied with a pixel array while the color mode is HSB),but will
        default to the HSL-normalized hue otherwise.
        (The values will only be different if the maximum hue setting for
        each system is different.)
        """
        if isinstance(color, list):
            return self._p5js.hue(to_js(color))
        return self._p5js.hue(color)

    def lerp_color(self, c1: str | list[int], c2: str | list[int], amt: float) -> str:
        """Blends two colors to find a third color somewhere between them.
        The amt parameter is the amount to interpolate between the two values
        where 0.0 is equal to the first color, 0.1 is very near the first color,
        0.5 is halfway in between, etc. An amount below 0 will be treated as 0.
        Likewise, amounts above 1 will be capped at 1. This is different from the
        behavior of lerp(), but necessary because otherwise numbers outside the
        range will produce strange and unexpected colors.

        The way that colors are interpolated depends on the current color mode.
        """
        _c1 = self._p5js.color(to_js(c1))
        _c2 = self._p5js.color(to_js(c2))
        return self._p5js.lerpColor(_c1, _c2, amt).toString()

    def lightness(self, color: str | list[int]) -> int:
        """Extracts the HSL lightness value from a color or pixel array."""
        if isinstance(color, list):
            return self._p5js.lightness(to_js(color))
        return self._p5js.lightness(color)

    def red(self, color: str | list[int]) -> int:
        """Extracts the red value from a color or pixel array."""
        return self._p5js.red(to_js(color))

    def saturation(self, color: str | list[int]) -> int:
        """Extracts the saturation value from a color or pixel array.

        Saturation is scaled differently in HSB and HSL. This function will return
        the HSB saturation when supplied with an HSB color object (or when
        supplied with a pixel array while the color mode is HSB), but will default
        to the HSL saturation otherwise.
        """
        if isinstance(color, list):
            return self._p5js.saturation(to_js(color))
        return self._p5js.saturation(color)

    # =======
    # Setting
    # =======
    def background(
        self,
        value: str | int | list[int],
        v2: int | None = None,
        v3: int | None = None,
        v4: int | None = None,
    ):
        """The background() function sets the color used for the background of the p5 canvas.
        The default background is transparent. This function is typically used within draw() to
        clear the display window at the beginning of each frame, but it can be used inside setup()
        to set the background on the first frame of animation or if the background need only be set once.

        The color is either specified in terms of the RGB, HSB, or HSL color depending on the current color_mode.
        (The default color space is RGB, with each value in the range from 0 to 255). The alpha range by default
        is also 0 to 255.

        A p5.Color object can also be provided to set the background color.
        """
        if v4:
            self._p5js.background(value, v2, v3, v4)
        elif v3:
            self._p5js.background(value, v2, v3)
        elif v2:
            self._p5js.background(value, v2)
        else:
            self._p5js.background(to_js(value))

    def clear(self):
        """Clears the pixels within a buffer.
        This function only clears the canvas. It will not clear objects created by
        create_x() functions such as createVideo() or createDiv(). Unlike the main
        graphics context, pixels in additional graphics areas created with
        create_graphics() can be entirely or partially transparent. This function
        clears everything to make all of the pixels 100% transparent.

        Note: In WebGL mode, this function can be passed normalized RGBA color
        values in order to clear the screen to a specific color. In addition to
        color, it will also clear the depth buffer. If you are not using the
        WebGL renderer these color values will have no effect.
        """
        self._p5js.clear()

    def color_mode(
        self,
        mode: str,
        max1: int | None = None,
        max2: int | None = None,
        max3: int | None = None,
        max4: int | None = None,
    ):
        """color_mode() changes the way p5 interprets color data. By default,
        the parameters for fill(), stroke(), background(), and color() are
        defined by values between 0 and 255 using the RGB color model.
        This is equivalent to setting color_mode(RGB, 255). Setting color_mode(HSB)
        lets you use the HSB system instead. By default,
        this is color_mode(HSB, 360, 100, 100, 1). You can also use HSL.

        Note: existing color objects remember the mode that they were created in,
        so you can change modes as you like without affecting their appearance.
        """
        if max4:
            self._p5js.colorMode(mode, max1, max2, max3, max4)
        elif max3:
            self._p5js.colorMode(mode, max1, max2, max3)
        elif max2:
            self._p5js.colorMode(mode, max1, max2)
        elif max1:
            self._p5js.colorMode(mode, max1)
        else:
            self._p5js.colorMode(mode)

    def fill(
        self,
        value: str | int | list[int],
        v2: int | None = None,
        v3: int | None = None,
        v4: int | None = None,
    ):
        """Sets the color used to fill shapes.
        For example, if you run fill(204, 102, 0), all shapes drawn after the
        fill() command will be filled with the color orange. This color is either
        specified in terms of the RGB or HSB color depending on the current
        color_mode(). (The default color space is RGB, with each value in the
        range from 0 to 255). The alpha range by default is also 0 to 255.

        If a single string argument is provided, RGB, RGBA and Hex CSS color
        strings and all named color strings are supported. In this case, an alpha
        number value as a second argument is not supported, the RGBA form should
        be used.

        A p5.Color object can also be provided to set the fill color.
        """
        if v4:
            self._p5js.fill(value, v2, v3, v4)
        elif v3:
            self._p5js.fill(value, v2, v3)
        elif v2:
            self._p5js.fill(value, v2)
        else:
            self._p5js.fill(to_js(value))

    def no_fill(self):
        """Disables filling geometry. If both no_stroke() and no_fill() are
        called, nothing will be drawn to the screen.
        """
        self._p5js.noFill()

    def no_stroke(self):
        """Disables drawing the stroke (outline). If both no_stroke() and
        no_fill() are called, nothing will be drawn to the screen.
        """
        self._p5js.noStroke()

    def stroke(
        self,
        value: str | int | list[int],
        v2: int | None = None,
        v3: int | None = None,
        v4: int | None = None,
    ):
        """Sets the color used to draw lines and borders around shapes.
        This color is either specified in terms of the RGB or HSB color depending
        on the current color_mode() (the default color space is RGB, with each
        value in the range from 0 to 255). The alpha range by default is also 0
        to 255.

        If a single string argument is provided, RGB, RGBA and Hex CSS color
        strings and all named color strings are supported. In this case, an alpha
        number value as a second argument is not supported, the RGBA form should
        be used.

        A p5.Color object can also be provided to set the stroke color.
        """
        if v4:
            self._p5js.stroke(value, v2, v3, v4)
        elif v3:
            self._p5js.stroke(value, v2, v3)
        elif v2:
            self._p5js.stroke(value, v2)
        else:
            self._p5js.stroke(to_js(value))

    def erase(self):
        """All drawing that follows erase() will subtract from the canvas.
        Erased areas will reveal the web page underneath the canvas. Erasing can
        be canceled with no_rase().

        Drawing done with image() and background() in between erase() and
        no_erase() will not erase the canvas but works as usual.
        """
        self._p5js.erase()

    def no_erase(self):
        """Ends erasing that was started with erase().
        The fill(), stroke(), and blend_mode() settings will return to what they
        were prior to calling erase().
        """
        self._p5js.noErase()
