from .constants import Constants
from .sysvars import SystemVariables


class BaseSketch(Constants, SystemVariables):
    id: str
    _p5js: object

    def __init__(self, id: str = "default_canvas"):
        import js
        from pyodide.code import run_js

        self.id = id
        try:
            old_sketch = getattr(js.window, self.id)
            old_sketch.remove()
        except AttributeError:
            pass
        finally:
            create_sketch = f"var {self.id} = " + "new p5(() => { });"
            run_js(create_sketch)
            set_canvas_id = f"{self.id}.canvas.setAttribute('id', '{self.id}');"
            run_js(set_canvas_id)
            self._p5js = getattr(js.window, self.id)
            self._init_constants()
