from .constants import Constants
from .sysvars import SystemVariables


class BaseSketch(Constants, SystemVariables):
    _p5js: object

    def __init__(self):
        import js
        from pyodide.code import run_js

        run_js("var _sketch = new p5(() => { });")
        self._p5js = js.window._sketch
        self._init_constants()
