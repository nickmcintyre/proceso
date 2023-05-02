# proceso
> A Python package for creative coding on the web.

proceso provides a Pythonic interface to the [p5.js](https://p5js.org) library. The package is designed for [Pyodide](https://pyodide.org)-based environments including [PyScript](https://pyscript.net) and (soonish) [JupyterLite](https://jupyterlite.readthedocs.io/en/latest/). Similar to [py5](https://py5coding.org/), proceso's goal is to integrate p5.js into the Python ecosystem with thoughtful choices about how to do so in the browser.

Here is an example of how to create a proceso sketch with PyScript:
```html
<!DOCTYPE html>
<html lang="en-us">

<head>
    <title>Bouncing Ball</title>
    <meta charset="utf-8" />

    <link rel="stylesheet" href="https://pyscript.net/releases/2023.03.1/pyscript.css" />
    <script defer src="https://pyscript.net/releases/2023.03.1/pyscript.js"></script>
    <link rel="stylesheet" href="style.css" />
    <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.6.0/p5.min.js"></script>
    <py-config>
        packages = ["numpy", "proceso"]
    </py-config>
</head>

<body>
    <main></main>
    <py-script src="sketch.py"></py-script>
</body>

</html>
```

```python
from proceso import Sketch


p5 = Sketch()


pos = p5.Vector(200, 200)
vel = p5.Vector.random(2)
r = 25


def setup():
    p5.create_canvas(400, 400)
    p5.background("#1e90ff")
    p5.fill("orchid")
    p5.stroke(255)


def draw():
    global pos, vel
    pos += vel

    p5.circle(pos.x, pos.y, 2 * r)

    if pos.x < r or pos.x > p5.width - r:
        vel.x *= -1
    if pos.y < r or pos.y > p5.height - r:
        vel.y *= -1

    if p5.is_mouse_pressed == True:
        p5.background("dodgerblue")


p5.run_sketch(setup=setup, draw=draw)
```

# Roadmap
- Improve documentation
- Fix known bugs
- Finish API
- Support JupyterLite
- Translate p5.js test suite?
- Add CLI with hot reload
- Add bindings for p5.js addon libraries

# Acknowledgements
- proceso is, first and foremost, an interface to the p5.js library. Nearly all of the package's documentation and examples are adapted from their p5.js counterparts. Portions of the source code are also adapted from the original JavaScript implementation.
- The `Vector` class is lovingly borrowed from py5 as are most of py5's naming conventions.
- [Basthon](https://framagit.org/basthon/), [Py5.js](https://github.com/Luxapodular/Py5.js), and [pyp5js](https://github.com/berinhard/pyp5js/) all pointed the way. 
