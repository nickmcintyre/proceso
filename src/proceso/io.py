from .binding import BaseSketch


class IO(BaseSketch):
    def day(self) -> int:
        """The day() function returns the current day as a value from 1 - 31."""
        return self._p5js.day()

    def hour(self) -> int:
        """The hour() function returns the current hour as a value from 0 - 23."""
        return self._p5js.hour()

    def minute(self) -> int:
        """The minute() function returns the current minute as a value from 0 - 59."""
        return self._p5js.minute()

    def millis(self) -> int:
        """Returns the number of milliseconds (thousandths of a second) since
        starting the sketch (when setup() is called).
        This information is often used for timing events and animation sequences.
        """
        return self._p5js.millis()

    def month(self) -> int:
        """The month() function returns the current month as a value from 1 - 12."""
        return self._p5js.month()

    def second(self) -> int:
        """The second() function returns the current second as a value from 0 - 59."""
        return self._p5js.second()

    def year(self) -> int:
        """The year() function returns the current year as an integer (2014, 2015, 2016, etc)."""
        return self._p5js.year()
