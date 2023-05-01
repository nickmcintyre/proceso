"""
Ray Casting
Adapted from https://p5js.org/examples/3d-ray-casting.html
CC-BY-NC-SA

Original example by Jonathan Watson. 
Detecting the position of the mouse in 3D space with ray casting.
"""
import proceso as p5


objects = []
eye_z: float


def setup():
    p5.create_canvas(710, 400, p5.WEBGL)

    global eye_z
    eye_z = (
        p5.height / 2 / p5.tan((30 * p5.PI) / 180)
    )  # The default distance the camera is away from the origin.

    objects.append(IntersectPlane(1, 0, 0, -100, 0, 0))  # Left wall
    objects.append(IntersectPlane(1, 0, 0, 100, 0, 0))  # Right wall
    objects.append(IntersectPlane(0, 1, 0, 0, -100, 0))  # Bottom wall
    objects.append(IntersectPlane(0, 1, 0, 0, 100, 0))  # Top wall
    objects.append(IntersectPlane(0, 0, 1, 0, 0, 0))  # Back wall

    p5.no_stroke()
    # p5.ambient_material(250)


def draw():
    p5.background(0)

    # Lights
    p5.point_light(255, 255, 255, 0, 0, 400)
    p5.ambient_light(244, 122, 158)

    # Left wall
    p5.push()
    p5.translate(-100, 0, 200)
    p5.rotate_y((90 * p5.PI) / 180)
    p5.plane(400, 200)
    p5.pop()

    # Right wall
    p5.push()
    p5.translate(100, 0, 200)
    p5.rotate_y((90 * p5.PI) / 180)
    p5.plane(400, 200)
    p5.pop()

    # Bottom wall
    p5.push()
    p5.translate(0, 100, 200)
    p5.rotate_x((90 * p5.PI) / 180)
    p5.plane(200, 400)
    p5.pop()

    # Top wall
    p5.push()
    p5.translate(0, -100, 200)
    p5.rotate_x((90 * p5.PI) / 180)
    p5.plane(200, 400)
    p5.pop()

    p5.plane(200, 200)  # Back wall

    x = p5.mouse_x - p5.width / 2
    y = p5.mouse_y - p5.height / 2

    Q = p5.Vector(
        0, 0, eye_z
    )  # A point on the ray and the default position of the camera.
    v = p5.Vector(x, y, -eye_z)  # The direction vector of the ray.

    intersect: p5.Vector  # The point of intersection between the ray and a plane.
    closest_lambda = eye_z * 10  # The draw distance.

    for o in objects:
        lam = o.get_lambda(Q, v)
        # The value of lambda where the ray intersects the object

        if (lam < closest_lambda) and (lam > 0):
            # Find the position of the intersection of the ray and the object.
            intersect = Q + v * lam
            closest_lambda = lam

    # Cursor
    p5.push()
    p5.translate(intersect.x, intersect.y, intersect.z)
    p5.fill(237, 34, 93)
    p5.sphere(10)
    p5.pop()


# Class for a plane that extends to infinity.
class IntersectPlane:
    def __init__(
        self, n1: float, n2: float, n3: float, p1: float, p2: float, p3: float
    ):
        self.normal = p5.Vector(n1, n2, n3)
        # The normal vector of the plane
        self.point = p5.Vector(p1, p2, p3)
        # A point on the plane
        self.d = self.point.dot(self.normal)

    def get_lambda(self, Q, v):
        lam = 0
        try:
            lam = (-self.d - self.normal.dot(Q)) / self.normal.dot(v)
        except:
            pass
        finally:
            return lam


p5.run(setup=setup, draw=draw)
