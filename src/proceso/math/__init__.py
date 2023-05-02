from .calculation import Calculation
from .noise import Noise
from .random import Random
from .trigonometry import Trigonometry
from .vector import (
    Vector,
    Vector2D,
    Vector3D,
    Vector4D,
)


class Math(Calculation, Noise, Random, Trigonometry):
    pass
