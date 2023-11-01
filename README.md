# proceso
> A Python package for creative coding on the web

proceso is a Python package for creative coding on the web, with a focus on making coding accessible and inclusive for artists, designers, educators, beginners, and anyone else! The package provides a Pythonic interface to the [p5.js](https://p5js.org) library and is heavily inspired by [py5](https://py5coding.org). proceso is designed for [Pyodide](https://pyodide.org)-based environments with a focus on [PyScript](https://pyscript.net).

Here is an example of how to create a proceso sketch with PyScript using Python, HTML, and CSS:

**sketch.py**

```python
from proceso import Sketch


p5 = Sketch()
p5.describe("A screen reader accessible description for the canvas.")
```

**index.html**

```html
<!DOCTYPE html>
<html lang="en-us">

<head>
    <title>My Sketch</title>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    
    <!-- Load PyScript -->
    <link rel="stylesheet" href="https://pyscript.net/snapshots/2023.09.1.RC2/core.css">
    <script type="module" src="https://pyscript.net/snapshots/2023.09.1.RC2/core.js"></script>
    <!-- Load p5.js -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.8.0/p5.min.js"></script>
    <!-- Load custom styles -->
    <link rel="stylesheet" href="style.css" />
</head>

<body>
    <!-- Load sketch -->
    <script type="py" src="sketch.py" config="pyscript.json"></script>
</body>

</html>
```

**style.css**

```css
html,
body {
    margin: 0;
    padding: 0;
}

canvas {
    display: block;
}
```

**pyscript.json**

```json
{
    "packages": ["proceso"]
}
```

## Static Sketches

Similar to [Processing](https://processing.org), proceso enables beginners to start programming with "static sketches" before introducing animation and interaction. The following example draws a few shapes and a flower on the screen.

```python
from proceso import Sketch


p5 = Sketch()
p5.describe("A rectangle, circle, triangle, and flower drawn in pink on a gray background.")

# Create the canvas
p5.create_canvas(720, 400)
p5.background(200)

# Set colors
p5.fill(204, 101, 192, 127)
p5.stroke(127, 63, 120)

# A rectangle
p5.rect(40, 120, 120, 40)
# A circle
p5.circle(240, 240, 80)
# A triangle
p5.triangle(300, 100, 320, 100, 310, 80)

# A design for a simple flower
p5.translate(580, 200)
p5.no_stroke()
for _ in range(10):
    p5.ellipse(0, 30, 20, 80)
    p5.rotate(p5.PI / 5)
```

[View sketch](https://4b2d42a1-0e0c-430f-8b20-4b2c7ff0dc3e.pyscriptapps.com/98a781e8-5e31-4f82-a2e5-881f9fed7b13/latest/)

## Active Sketches

proceso's "active sketches" provide the `run_sketch()` method to handle initialization, looping, and events. The sketch below simulates the synchronization behavior observed in some species of fireflies.

```python
from proceso import Sketch


p5 = Sketch()
p5.describe("Ten white circles moving like fireflies on a dark blue background.")

bugs = []
num_bugs = 10
coupling: object


def setup():
    p5.create_canvas(720, 400)
    global coupling
    coupling = p5.create_slider(0, 10, 5)
    for _ in range(num_bugs):
        bug = Bug()
        bugs.append(bug)


def draw():
    p5.background("midnightblue")

    for bug in bugs:
        bug.sync()

    for bug in bugs:
        bug.update()
        bug.check_edges()
        bug.draw()


class Bug:
    def __init__(self):
        self.x = p5.width * 0.5
        self.y = p5.height * 0.5
        self.r = 5
        self.angle = p5.random(p5.TWO_PI)
        self.da_dt = 1
        self.dt = 0.01
        self.freq = p5.random(5, 10)

    def draw(self):
        a = p5.remap(self.angle % p5.TWO_PI, 0, p5.TWO_PI, 0, 255)
        p5.fill(255, a)
        p5.stroke(255, a)
        p5.circle(self.x, self.y, 2 * self.r)

    def update(self):
        self.x += p5.cos(self.angle)
        self.y += p5.sin(self.angle)
        self.angle += self.da_dt * self.dt
        self.da_dt = 0

    def check_edges(self):
        if self.x > p5.width + self.r:
            self.x = -self.r
        if self.x < -self.r:
            self.x = p5.width + self.r
        if self.y > p5.height + self.r:
            self.y = -self.r
        if self.y < -self.r:
            self.y = p5.height + self.r

    def sync(self):
        K_N = coupling.value() / num_bugs
        self.da_dt = self.freq
        for bug in bugs:
            self.da_dt += K_N * p5.sin(bug.angle - self.angle)


p5.run_sketch(setup=setup, draw=draw)
```

[View sketch](https://4b2d42a1-0e0c-430f-8b20-4b2c7ff0dc3e.pyscriptapps.com/2db32203-cd60-416f-999c-f730253358e8/latest/)

## Getting Started

**Cloud: PyScript (account required)**

[PyScript](https://pyscript.com) is a great way to run proceso sketches with PyScript. Here's a [project template](https://pyscript.com/view/4b2d42a1-0e0c-430f-8b20-4b2c7ff0dc3e/58197361-1c5f-4d47-93a9-91570255fe85/latest/).

**Local: VS Code**

Here's one possible setup for running sketches on your local machine:

1. Install [Visual Studio Code](https://code.visualstudio.com/).
2. Install the [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) extension.
3. Add your HTML, CSS, JSON, and Python files.
4. Open `index.html` with Live Server and start coding.

## Roadmap

- Improve documentation
- Finish IO API
- Translate p5.js test suite?
- Add CLI with hot reload
- Add bindings for p5.js addon libraries

## Acknowledgements

- proceso is, first and foremost, an interface to the p5.js library. Nearly all of the package's documentation and examples are adapted from their p5.js counterparts. Portions of the source code are also adapted from the original JavaScript implementation.
- The `Vector` class is lovingly borrowed from py5 as are most of py5's naming conventions.
- [Basthon](https://framagit.org/basthon/), [Py5.js](https://github.com/Luxapodular/Py5.js), and [pyp5js](https://github.com/berinhard/pyp5js/) all pointed the way. 
