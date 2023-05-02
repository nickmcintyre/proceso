import math

from .._binding import BaseSketch


class Calculation(BaseSketch):
    def abs(self, n: float) -> float:
        """Calculates the absolute value (magnitude) of a number.
        The absolute value of a number is always positive.
        """
        return self._p5js.abs(n)

    def ceil(self, n: float) -> int:
        """Calculates the closest int value that is greater than or equal to the
        value of the parameter.
        Maps to math.ceil(). For example, ceil(9.03) returns the value 10.
        """
        return math.ceil(n)

    def constrain(self, n: float, low: float, high: float) -> float:
        """Constrains a value between a minimum and maximum value."""
        return self._p5js.constrain(n, low, high)

    def dist(self, x1: float, y1: float, x2: float, y2: float, *args) -> float:
        """Calculates the distance between two points, in either two or three
        dimensions.
        """
        return self._p5js.dist(x1, y2, x2, y2, *args)

    def exp(self, n: float) -> float:
        """Returns Euler's number e (2.71828...) raised to the power of the n
        parameter.
        Maps to math.exp().
        """
        return math.exp(n)

    def floor(self, n: float) -> int:
        """Calculates the closest int value that is less than or equal to the
        value of the parameter.
        Maps to math.floor().
        """
        return math.floor(n)

    def lerp(self, start: float, stop: float, amt: float) -> float:
        """Calculates a number between two numbers at a specific increment.
        The amt parameter is the amount to interpolate between the two values
        where 0.0 is equal to the first point, 0.1 is very near the first point,
        0.5 is half-way in between, and 1.0 is equal to the second point. If the
        value of amt is more than 1.0 or less than 0.0, the number will be
        calculated accordingly in the ratio of the two given numbers. The lerp()
        function is convenient for creating motion along a straight path and for
        drawing dotted lines.
        """
        return self._p5js.lerp(start, stop, amt)

    def log(self, n: float) -> float:
        """Calculates the natural logarithm (the base-e logarithm) of a number.
        This function expects the n parameter to be a value greater than 0.0.
        Maps to math.log().
        """
        return math.log(n)

    def mag(self, a: float, b: float) -> float:
        """Calculates the magnitude (or length) of a vector.
        A vector is a direction in space commonly used in computer graphics and
        linear algebra. Because it has no "start" position, the magnitude of a
        vector can be thought of as the distance from the coordinate 0,0 to its
        x,y value. Therefore, mag() is a shortcut for writing dist(0, 0, x, y).
        """
        return dist(0, 0, a, b)

    def remap(
        self,
        value: float,
        start1: float,
        stop1: float,
        start2: float,
        stop2: float,
        within_bounds: bool | None = None,
    ):
        """Re-maps a number from one range to another.

        In the first example above, the number 25 is converted from a value in
        the range of 0 to 100 into a value that ranges from the left edge of the
        window (0) to the right edge (width).
        """
        return self._p5js.map(value, start1, stop1, start2, stop2, within_bounds)

    def max(self, n: float | list[float], n1: float | None = None) -> float:
        """Determines the largest value in a sequence of numbers, and then
        returns that value.
        max() accepts any number of float parameters, or a list of any length.
        """
        if n1:
            return self._p5js.max(n, n1)
        return self._p5js.max(n)

    def min(self, n: float | list[float], n1: float | None = None) -> float:
        """Determines the smallest value in a sequence of numbers, and then
        returns that value.
        min() accepts any number of float parameters, or a list of any length.
        """
        if n1:
            return self._p5js.min(n, n1)
        return self._p5js.min(n)

    def norm(self, value: float, start: float, stop: float) -> float:
        """Normalizes a number from another range into a value between 0 and 1.
        Identical to map(value, low, high, 0, 1). Numbers outside of the range are
        not clamped to 0 and 1, because out-of-range values are often intentional
        and useful. (See the example above.)
        """
        return self._p5js.norm(value, start, stop)

    def pow(self, n: float, e: float) -> float:
        """Facilitates exponential expressions.
        The pow() function is an efficient way of multiplying numbers by
        themselves (or their reciprocals) in large quantities. For example,
        pow(3, 5) is equivalent to the expression 3 × 3 × 3 × 3 × 3 and pow(3, -5)
        is equivalent to 1 / 3 × 3 × 3 × 3 × 3. Maps to math.pow().
        """
        return math.pow(n, e)

    def round(self, n: float, decimals: int | None = None) -> float:
        """Calculates the integer closest to the n parameter.
        For example, round(133.8) returns the value 134.
        """
        return self._p5js.round(n, decimals)

    def sq(self, n: float) -> float:
        """Squares a number (multiplies a number by itself).
        The result is always a positive number, as multiplying two negative
        numbers always yields a positive result. For example, -1 * -1 = 1.
        """
        return n * n

    def sqrt(self, n: float) -> float:
        """Squares a number (multiplies a number by itself).
        The result is always a positive number, as multiplying two negative
        numbers always yields a positive result. For example, -1 * -1 = 1.
        """
        return math.sqrt(n)

    def fract(self, n: float) -> float:
        """Calculates the fractional part of a number."""
        return self._p5js.fract(n)
