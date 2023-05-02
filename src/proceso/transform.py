import collections
from pyodide.ffi import to_js

from ._binding import BaseSketch


class Transform(BaseSketch):
    def apply_matrix(
        self,
        a: float | list[float],
        b: float | None = None,
        c: float | None = None,
        d: float | None = None,
        e: float | None = None,
        f: float | None = None,
        g: float | None = None,
        h: float | None = None,
        i: float | None = None,
        j: float | None = None,
        k: float | None = None,
        l: float | None = None,
        m: float | None = None,
        n: float | None = None,
        o: float | None = None,
        p: float | None = None,
    ):
        """Multiplies the current matrix by the one specified through the
        parameters.
        This is a powerful operation that can perform the equivalent of translate,
        scale, shear and rotate all at once. You can learn more about
        transformation matrices online:

        https://en.wikipedia.org/wiki/Transformation_matrix

        https://html.spec.whatwg.org/multipage/canvas.html#dom-context-2d-transform
        """
        if p:
            self._p5js.applyMatrix(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p)
        elif f:
            self._p5js.applyMatrix(a, b, c, d, e, f)
        elif isinstance(a, collections.Sequence):
            self._p5js.applyMatrix(to_js(a))

    def reset_matrix(self):
        """Replaces the current matrix with the identity matrix."""
        self._p5js.resetMatrix()

    def rotate(self, angle: float):
        """Rotates a shape by the amount specified by the angle parameter.
        This function accounts for angle_mode, so angles can be entered in either
        RADIANS or DEGREES.

        Objects are always rotated around their relative position to the origin
        and positive numbers rotate objects in a clockwise direction.
        Transformations apply to everything that happens after and subsequent
        calls to the function accumulate the effect. For example, calling
        rotate(HALF_PI) and then rotate(HALF_PI) is the same as rotate(PI).
        All transformations are reset when draw() begins again.

        Technically, rotate() multiplies the current transformation matrix by a
        rotation matrix. This function can be further controlled by push() and
        pop().
        """
        self._p5js.rotate(angle)

    def rotate_x(self, angle: float):
        """Rotates a shape around X axis by the amount specified in angle
        parameter.
        The angles can be entered in either RADIANS or DEGREES.

        Objects are always rotated around their relative position to the origin
        and positive numbers rotate objects in a clockwise direction. All
        transformations are reset when draw() begins again.
        """
        self._p5js.rotateX(angle)

    def rotate_y(self, angle: float):
        """Rotates a shape around Y axis by the amount specified in angle
        parameter.
        The angles can be entered in either RADIANS or DEGREES.

        Objects are always rotated around their relative position to the origin
        and positive numbers rotate objects in a clockwise direction. All
        transformations are reset when draw() begins again.
        """
        self._p5js.rotateY(angle)

    def rotate_z(self, angle: float):
        """Rotates a shape around Z axis by the amount specified in angle
        parameter.
        The angles can be entered in either RADIANS or DEGREES.

        This method works in WEBGL mode only.

        Objects are always rotated around their relative position to the origin
        and positive numbers rotate objects in a clockwise direction. All
        transformations are reset when draw() begins again.
        """
        self._p5js.rotateZ(angle)

    def scale(self, s: float, y: float | None = None, z: float | None = None):
        """Increases or decreases the size of a shape by expanding or
        contracting vertices.
        Objects always scale from their relative origin to the coordinate system.
        Scale values are specified as decimal percentages. For example, the
        function call scale(2.0) increases the dimension of a shape by 200%.

        Transformations apply to everything that happens after and subsequent
        calls to the function multiply the effect. For example, calling scale(2.0)
        and then scale(1.5) is the same as scale(3.0). If scale() is called within
        draw(), the transformation is reset when the loop begins again.

        Using this function with the z parameter is only available in WEBGL mode.
        This function can be further controlled with push() and pop().

        """
        self._p5js.scale(s, y, z)

    def shear_x(self, angle: float):
        """Shears a shape around the x-axis by the amount specified by the angle
        parameter.
        Angles should be specified in the current angleMode. Objects are always
        sheared around their relative position to the origin and positive numbers
        shear objects in a clockwise direction.

        Transformations apply to everything that happens after and subsequent
        calls to the function accumulates the effect. For example, calling
        shear_x(PI/2) and then shear_x(PI/2) is the same as shear_x(PI). If
        shear_x() is called within the draw(), the transformation is reset when
        the loop begins again.

        Technically, shear_x() multiplies the current transformation matrix by a
        rotation matrix. This function can be further controlled by the push()
        and pop() functions.
        """
        self._p5js.shearX(angle)

    def shear_y(self, angle: float):
        """Shears a shape around the y-axis the amount specified by the angle
        parameter.
        Angles should be specified in the current angleMode. Objects are always
        sheared around their relative position to the origin and positive numbers
        shear objects in a clockwise direction.

        Transformations apply to everything that happens after and subsequent
        calls to the function accumulates the effect. For example, calling
        shear_y(PI/2) and then shear_y(PI/2) is the same as shear_y(PI). If
        shear_y() is called within the draw(), the transformation is reset when
        the loop begins again.

        Technically, shear_y() multiplies the current transformation matrix by a rotation matrix. This function can be further controlled by the push() and pop() functions.
        """
        self._p5js.shearY(angle)

    def translate(self, x: float, y: float, z: float | None = None):
        """Specifies an amount to displace objects within the display window.
        The x parameter specifies left/right translation, the y parameter
        specifies up/down translation.

        Transformations are cumulative and apply to everything that happens after
        and subsequent calls to the function accumulates the effect. For example,
        calling translate(50, 0) and then translate(20, 0) is the same as
        translate(70, 0). If translate() is called within draw(), the
        transformation is reset when the loop begins again. This function can be
        further controlled by using push() and pop().
        """
        self._p5js.translate(x, y, z)
