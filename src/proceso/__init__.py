from typing import Callable


from .colors import Colors
from .data import Data
from .dom import DOM
from .environment import Environment
from .events import Events
from .images import Images
from .math import (
    Math,
    Vector as _Vector,
    Vector2D as _Vector2D,
    Vector3D as _Vector3D,
    Vector4D as _Vector4D,
)
from .rendering import Rendering
from .shape import Shape
from .structure import Structure
from .three_d import ThreeD
from .transform import Transform
from .typography import Typography


class Sketch(
    Colors,
    Data,
    DOM,
    Environment,
    Events,
    Images,
    Math,
    Rendering,
    Shape,
    Structure,
    ThreeD,
    Transform,
    Typography,
):
    Vector = _Vector
    Vector2D = _Vector2D
    Vector3D = _Vector3D
    Vector4D = _Vector4D

    def run_sketch(
        self,
        preload: Callable | None = None,
        setup: Callable | None = None,
        draw: Callable | None = None,
        key_pressed: Callable | None = None,
        key_released: Callable | None = None,
        key_typed: Callable | None = None,
        key_is_down: Callable | None = None,
        mouse_moved: Callable | None = None,
        mouse_dragged: Callable | None = None,
        mouse_pressed: Callable | None = None,
        mouse_released: Callable | None = None,
        mouse_clicked: Callable | None = None,
        double_clicked: Callable | None = None,
        mouse_wheel: Callable | None = None,
        request_pointer_lock: Callable | None = None,
        exit_pointer_lock: Callable | None = None,
    ):
        import inspect
        from pyodide.ffi import create_proxy

        self._p5js._setupDone = False
        self._p5js._preloadDone = False
        self._p5js._millisStart = -1
        if callable(preload):
            self._p5js.preload = create_proxy(preload)
        if callable(setup):
            self._p5js.setup = create_proxy(setup)

        if callable(draw):

            def _draw(*args):
                self._update_system_variables()
                draw()

            self._p5js.draw = create_proxy(_draw)

        def wrap_event_func(func: Callable):
            args = inspect.signature(func).parameters
            if len(args) == 0:

                def wrapped_func(event):
                    func()

                return create_proxy(wrapped_func)
            else:
                return create_proxy(func)

        if callable(key_pressed):
            self._p5js.keyPressed = wrap_event_func(key_pressed)
        if callable(key_released):
            self._p5js.keyReleased = wrap_event_func(key_released)
        if callable(key_typed):
            self._p5js.keyTyped = wrap_event_func(key_typed)
        if callable(key_is_down):
            self._p5js.keyIsDown = create_proxy(key_is_down)
        if callable(mouse_moved):
            self._p5js.mouseMoved = wrap_event_func(mouse_moved)
        if callable(mouse_dragged):
            self._p5js.mouseDragged = wrap_event_func(mouse_dragged)
        if callable(mouse_pressed):
            self._p5js.mousePressed = wrap_event_func(mouse_pressed)
        if callable(mouse_released):
            self._p5js.mouseReleased = wrap_event_func(mouse_released)
        if callable(mouse_clicked):
            self._p5js.mouseClicked = wrap_event_func(mouse_clicked)
        if callable(double_clicked):
            self._p5js.doubleClicked = wrap_event_func(double_clicked)
        if callable(mouse_wheel):
            self._p5js.mouseWheel = create_proxy(mouse_wheel)
        if callable(request_pointer_lock):
            self._p5js.requestPointerLock = create_proxy(request_pointer_lock)
        if callable(exit_pointer_lock):
            self._p5js.exitPointerLock = create_proxy(exit_pointer_lock)

        self._p5js._start()
