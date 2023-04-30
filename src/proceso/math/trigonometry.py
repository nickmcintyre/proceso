from .._binding import _p5js


def acos(value: float) -> float:
    """The inverse of cos(), returns the arc cosine of a value.
    This function expects the values in the range of -1 to 1 and values are
    returned in the range 0 to PI (3.1415927) if the angle_mode() is RADIANS
    or 0 to 180 if the angle_mode() is DEGREES.
    """
    return _p5js.acos(value)


def asin(value: float) -> float:
    """The inverse of sin(), returns the arc sine of a value.
    This function expects the values in the range of -1 to 1 and values are
    returned in the range -PI/2 to PI/2 if the angle_mode is RADIANS or -90 to
    90 if the angle mode is DEGREES.
    """
    return _p5js.asin(value)


def atan(value: float) -> float:
    """The inverse of tan(), returns the arc tangent of a value.
    This function expects the values in the range of -Infinity to Infinity
    (exclusive) and values are returned in the range -PI/2 to PI/2 if the
    angle_mode is RADIANS or -90 to 90 if the angle_mode is DEGREES.
    """
    return _p5js.atan(value)


def atan2(y, x) -> float:
    """Calculates the angle (in radians) from a specified point to the
    coordinate origin as measured from the positive x-axis.
    Values are returned as a float in the range from PI to -PI if the
    angle_mode() is RADIANS or 180 to -180 if the angle_mode() is DEGREES.
    The atan2() function is most often used for orienting geometry to the
    position of the cursor.

    Note: The y-coordinate of the point is the first parameter, and the
    x-coordinate is the second parameter, due to the structure of calculating
    the tangent.
    """
    return _p5js.atan2(y, x)


def cos(value: float) -> float:
    """Calculates the cosine of an angle.
    This function takes into account the current angle_mode. Values are
    returned in the range -1 to 1.
    """
    return _p5js.cos(value)


def sin(value: float) -> float:
    """Calculates the sine of an angle.
    This function takes into account the current angle_mode. Values are
    returned in the range -1 to 1.
    """
    return _p5js.sin(value)


def tan(value: float) -> float:
    """Calculates the tangent of an angle.
    This function takes into account the current angle_mode. Values are
    returned in the range of all real numbers.
    """
    return _p5js.tan(value)


def degrees(radians: float) -> float:
    """Converts a radian measurement to its corresponding value in degrees.
    Radians and degrees are two ways of measuring the same thing. There are
    360 degrees in a circle and 2*PI radians in a circle. For example,
    90° = PI/2 = 1.5707964. This function does not take into account the
    current angle_mode.
    """
    return _p5js.degrees(radians)


def radians(degrees: float) -> float:
    """Converts a degree measurement to its corresponding value in radians.
    Radians and degrees are two ways of measuring the same thing. There are
    360 degrees in a circle and 2*PI radians in a circle. For example,
    90° = PI/2 = 1.5707964. This function does not take into account the
    current angle_mode.
    """
    return _p5js.radians(degrees)


def angle_mode(mode: str | None = None) -> None | str:
    """Sets the current mode of p5 to the given mode.
    Default mode is RADIANS.

    Calling angle_mode() with no arguments returns current angle_mode.
    """
    if not mode:
        return _p5js.angleMode()
    _p5js.angleMode(mode)
