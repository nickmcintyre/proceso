from .color import Color
from .data import Data
from .dom import DOM
from .environment import Environment
from .events import Events
from .images import Images
from .io import IO
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
    Color,
    Data,
    DOM,
    Environment,
    Events,
    Images,
    IO,
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
