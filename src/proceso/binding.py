from .constants import Constants
from .sysvars import SystemVariables
from .utils import remove_sketch


class BaseSketch(Constants, SystemVariables):
    id: str
    _p5js: object

    def __init__(self, id: str = "defaultCanvas0"):
        import js
        from pyodide.code import run_js

        self.id = id
        remove_sketch(self.id)
        create_sketch = f"var {self.id} = " + "new p5(() => { });"
        run_js(create_sketch)
        set_canvas_id = f"{self.id}.canvas.setAttribute('id', '{self.id}');"
        run_js(set_canvas_id)
        self._p5js = getattr(js.window, self.id)
        self._init_constants()
