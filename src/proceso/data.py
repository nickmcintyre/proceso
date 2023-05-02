from pyodide.ffi import to_js

from ._binding import BaseSketch


class Data(BaseSketch):
    def nf(
        self,
        num: float | list[float],
        left: int | str | None = None,
        right: int | str | None = None,
    ) -> str | list[str]:
        """Utility function for formatting numbers into strings.
        There are two versions: one for formatting floats, and one for
        formatting ints.

        The values for the digits, left, and right parameters should always be
        positive integers.

        (NOTE): Be cautious when using left and right parameters as it prepends
        numbers of 0's if the parameter if greater than the current length of the
        number.

        For example if number is 123.2 and left parameter passed is 4 which is
        greater than length of 123 (integer part) i.e 3 than result will be
        0123.2. Same case for right parameter i.e. if right is 3 than the result
        will be 123.200.
        """
        return self._p5js.nf(to_js(num), left, right)

    def nfc(
        self,
        num: float | list[float],
        right: int | str | None = None,
    ) -> str | list[str]:
        """Utility function for formatting numbers into strings and placing
        appropriate commas to mark units of 1000.
        There are two versions: one for formatting ints, and one for formatting
        an array of ints. The value for the right parameter should always be a
        positive integer.
        """
        return self._p5js.nfc(to_js(num), right)

    def nfp(
        self,
        num: float | list[float],
        left: int | str | None = None,
        right: int | str | None = None,
    ) -> str | list[str]:
        """Utility function for formatting numbers into strings.
        Similar to nf() but puts a "+" in front of positive numbers and a "-"
        in front of negative numbers. There are two versions: one for formatting
        floats, and one for formatting ints. The values for left, and right
        parameters should always be positive integers.
        """
        return self._p5js.nfp(to_js(num), left, right)

    def nfs(
        self,
        num: float | list[float],
        left: int | str | None = None,
        right: int | str | None = None,
    ) -> str | list[str]:
        """Utility function for formatting numbers into strings.
        Similar to nf() but puts an additional "_" (space) in front of positive
        numbers just in case to align it with negative numbers which includes "-"
        (minus) sign.

        The main usecase of nfs() can be seen when one wants to align the digits
        (place values) of a non-negative number with some negative number (See
        the example to get a clear picture). There are two versions: one for
        formatting float, and one for formatting int.

        The values for the digits, left, and right parameters should always be
        positive integers.

        (IMP): The result on the canvas basically the expected alignment can vary
        based on the typeface you are using.

        (NOTE): Be cautious when using left and right parameters as it prepends
        numbers of 0's if the parameter if greater than the current length of the number.

        For example if number is 123.2 and left parameter passed is 4 which is
        greater than length of 123 (integer part) i.e 3 than result will be
        0123.2. Same case for right parameter i.e. if right is 3 than the result
        will be 123.200.

        """
        return self._p5js.nfs(to_js(num), left, right)
