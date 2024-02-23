from .binding import BaseSketch


class Events(BaseSketch):
    # ============
    # Acceleration
    # ============
    def set_move_threshold(self, value: float):
        """The set_move_threshold() function is used to set the movement threshold
        for the device_moved() function.
        The default threshold is set to 0.5.
        """
        self._p5js.setMoveThreshold(value)

    def set_shake_threshold(self, value: float):
        """The set_shake_threshold() function is used to set the movement
        threshold for the device_shaken() function.
        The default threshold is set to 30.
        """
        self._p5js.setShakeThreshold(value)

    # =====
    # Mouse
    # =====
    def request_pointer_lock(self):
        """The function request_pointer_lock() locks the pointer to its current
        position and makes it invisible.
        Use moved_x and moved_y to get the difference the mouse was moved since
        the last call of draw. Note that not all browsers support this feature.
        This enables you to create experiences that aren't limited by the mouse
        moving out of the screen even if it is repeatedly moved into one
        direction. For example, a first person perspective experience.
        """
        self._p5js.requestPointerLock()

    def exit_pointer_lock(self):
        """The function exit_pointer_lock() exits a previously triggered
        pointer lock for example to make ui elements usable etc.
        """
        self._p5js.exitPointerLock()

    # =====
    # Keyboard
    # =====
    def key_is_down(self, code: int) -> bool:
        """The key_is_down() function checks if the key is currently down, i.e.
        pressed.
        It can be used if you have an object that moves, and you want
        several keys to be able to affect its behaviour simultaneously, such as
        moving a sprite diagonally. You can put in any number representing the
        key_code of the key, or use any of the variable key_code names listed here:
        http://p5js.org/reference/#p5/keyCode.
        """
        return self._p5js.keyIsDown(code)
