from pyodide.ffi import to_js

from ._binding import BaseSketch


class ThreeD(BaseSketch):
    # ===========
    # Interaction
    # ===========
    def orbit_control(
        self,
        sensitivity_x: float | None = None,
        sensitivity_y: float | None = None,
        sensitivity_z: float | None = None,
    ):
        """Allows movement around a 3D sketch using a mouse or trackpad.
        Left-clicking and dragging will rotate the camera position about the
        center of the sketch, right-clicking and dragging will pan the camera
        position without rotation, and using the mouse wheel (scrolling) will
        move the camera closer or further from the center of the sketch. This
        function can be called with parameters dictating sensitivity to mouse
        movement along the X and Y axes. Calling this function without parameters
        is equivalent to calling orbit_control(1,1). To reverse direction of
        movement in either axis, enter a negative number for sensitivity.
        """
        self._p5js.orbitControl(sensitivity_x, sensitivity_y, sensitivity_z)

    def debug_mode(self, mode: str | None = None):
        """debug_mode() helps visualize 3D space by adding a grid to indicate
        where the ‘ground’ is in a sketch and an axes icon which indicates the +X,
        +Y, and +Z directions. This function can be called without parameters to
        create a default grid and axes icon. The grid is drawn using the most
        recently set stroke color and weight. To specify these parameters, add a
        call to stroke() and stroke_weight() just before the end of the draw()
        loop.

        By default, the grid will run through the origin (0,0,0) of the sketch
        along the XZ plane and the axes icon will be offset from the origin. Both
        the grid and axes icon will be sized according to the current canvas size.
        Note that because the grid runs parallel to the default camera view, it is
        often helpful to use debug_mode along with orbit_control to allow full
        view of the grid.
        """
        self._p5js.debugMode(mode)

    def no_debug_mode(self):
        """Turns off debug_mode() in a 3D sketch."""
        self._p5js.noDebugMode()

    # ======
    # Lights
    # ======
    def ambient_light(
        self,
        value: str | int | list[int],
        v2: int | None = None,
        v3: int | None = None,
        v4: int | None = None,
    ):
        """Creates an ambient light with the given color.

        Ambient light does not come from a specific direction. Objects are evenly
        lit from all sides. Ambient lights are almost always used in combination
        with other types of lights.

        Note: lights need to be called (whether directly or indirectly) within
        draw() to remain persistent in a looping program. Placing them in setup()
        will cause them to only have an effect the first time through the loop.
        """
        if v4:
            self._p5js.ambientLight(value, v2, v3, v4)
        elif v3:
            self._p5js.ambientLight(value, v2, v3)
        elif v2:
            self._p5js.ambientLight(value, v2)
        else:
            self._p5js.ambientLight(to_js(value))

    def specular_color(
        self,
        value: str | int | list[int],
        v2: int | None = None,
        v3: int | None = None,
    ):
        """Sets the color of the specular highlight of a non-ambient light
        (i.e. all lights except ambient_light()).

        specularColor() affects only the lights which are created after it in the
        code.

        This function is used in combination with specular_material(). If a
        geometry does not use specular_material(), this function will have no
        effect.

        The default color is white (255, 255, 255), which is used if
        specular_color() is not explicitly called.

        Note: specular_color is equivalent to the Processing function
        lightSpecular.
        """
        if v3:
            self._p5js.specularColor(value, v2, v3)
        elif v2:
            self._p5js.specularColor(value, v2)
        else:
            self._p5js.specularColor(to_js(value))

    def directional_light(
        self,
        v1: float,
        v2: float,
        v3: float,
        x: float,
        y: float,
        z: float,
    ):
        """Creates a directional light with the given color and direction.

        Directional light comes from one direction. The direction is specified as
        numbers inclusively between -1 and 1. For example, setting the direction
        as (0, -1, 0) will cause the geometry to be lit from below (since the
        light will be facing directly upwards). Similarly, setting the direction
        as (1, 0, 0) will cause the geometry to be lit from the left (since the
        light will be facing directly rightwards).

        Directional lights do not have a specific point of origin, and therefore
        cannot be positioned closer or farther away from a geometry.

        A maximum of 5 directional lights can be active at once.

        Note: lights need to be called (whether directly or indirectly) within
        draw() to remain persistent in a looping program. Placing them in setup()
        will cause them to only have an effect the first time through the loop.
        """
        self._p5js.directionalLight(v1, v2, v3, x, y, z)

    def point_light(
        self,
        v1: float,
        v2: float,
        v3: float,
        x: float,
        y: float,
        z: float,
    ):
        """Creates a point light with the given color and position.

        A point light emits light from a single point in all directions. Because
        the light is emitted from a specific point (position), it has a different
        effect when it is positioned farther vs. nearer an object.

        A maximum of 5 point lights can be active at once.

        Note: lights need to be called (whether directly or indirectly) within
        draw() to remain persistent in a looping program. Placing them in setup()
        will cause them to only have an effect the first time through the loop.
        """
        self._p5js.pointLight(v1, v2, v3, x, y, z)

    def lights(self):
        """Places an ambient and directional light in the scene.
        The lights are set to ambient_light(128, 128, 128) and
        directional_light(128, 128, 128, 0, 0, -1).

        Note: lights need to be called (whether directly or indirectly) within
        draw() to remain persistent in a looping program. Placing them in setup()
        will cause them to only have an effect the first time through the loop.
        """
        self._p5js.lights()

    def light_falloff(self, constant: float, linear: float, quadratic: float):
        """Sets the falloff rate for point_light() and spot_light().

        light_falloff() affects only the lights which are created after it in the
        code.

        The constant, linear, an quadratic parameters are used to calculate
        falloff as follows:

        d = distance from light position to vertex position

        falloff = 1 / (CONSTANT + d * LINEAR + (d * d) * QUADRATIC)
        """
        self._p5js.lightFalloff(constant, linear, quadratic)

    def spot_light(
        self,
        v1: float,
        v2: float,
        v3: float,
        x: float,
        y: float,
        z: float,
        rx: float,
        ry: float,
        rz: float,
        angle: float | None = None,
        concentration: float | None = None,
    ):
        """Creates a spot light with the given color, position, light direction,
        angle, and concentration.

        Like a point_light(), a spot_light() emits light from a specific point
        (position). It has a different effect when it is positioned farther vs.
        nearer an object.

        However, unlike a point_light(), the light is emitted in one direction
        along a conical shape. The shape of the cone can be controlled using the
        angle and concentration parameters.

        The angle parameter is used to determine the radius of the cone. And the
        concentration parameter is used to focus the light towards the center of
        the cone. Both parameters are optional, however if you want to specify
        concentration, you must also specify angle. The minimum concentration
        value is 1.

        A maximum of 5 spot lights can be active at once.

        Note: lights need to be called (whether directly or indirectly) within
        draw() to remain persistent in a looping program. Placing them in setup()
        will cause them to only have an effect the first time through the loop.
        """
        if concentration:
            self._p5js.spotLight(v1, v2, v3, x, y, z, rx, ry, rz, angle, concentration)
        elif angle:
            self._p5js.spotLight(v1, v2, v3, x, y, z, rx, ry, rz, angle)
        else:
            self._p5js.spotLight(v1, v2, v3, x, y, z, rx, ry, rz)

    def no_lights(self):
        """Removes all lights present in a sketch.

        All subsequent geometry is rendered without lighting (until a new light
        is created with a call to one of the lighting functions (lights(),
        ambient_light(), directional_light(), point_light(), spot_light()).
        """
        self._p5js.noLights()

    # ======
    # Camera
    # ======
    def camera(
        self,
        x: float | None = None,
        y: float | None = None,
        z: float | None = None,
        center_x: float | None = None,
        center_y: float | None = None,
        center_z: float | None = None,
        up_x: float | None = None,
        up_y: float | None = None,
        up_z: float | None = None,
    ):
        """Sets the position of the current camera in a 3D sketch.
        Parameters for this function define the camera's position, the center of
        the sketch (where the camera is pointing), and an up direction (the
        orientation of the camera).

        This function simulates the movements of the camera, allowing objects to
        be viewed from various angles. Remember, it does not move the objects
        themselves but the camera instead. For example when the centerX value is
        positive, and the camera is rotating to the right side of the sketch, the
        object will seem like it's moving to the left.

        See this example to view the position of your camera.

        If no parameters are given, the following default is used:
        camera(0, 0, (height/2) / tan(PI/6), 0, 0, 0, 0, 1, 0)
        """
        if not up_z:
            self._p5js.camera(
                0, 0, (self._p5js.height * 0.5) / 0.5773502691896256, 0, 0, 0, 0, 1, 0
            )
        else:
            self._p5js.camera(x, y, z, center_x, center_y, center_z, up_x, up_y, up_z)

    def perspective(
        self,
        fovy: float | None = None,
        aspect: float | None = None,
        near: float | None = None,
        far: float | None = None,
    ):
        """Sets a perspective projection for the current camera in a 3D sketch.
        This projection represents depth through foreshortening: objects that are
        close to the camera appear their actual size while those that are further
        away from the camera appear smaller.

        The parameters to this function define the viewing frustum (the truncated
        pyramid within which objects are seen by the camera) through vertical
        field of view, aspect ratio (usually width/height), and near and far
        clipping planes.

        If no parameters are given, the following default is used:
        perspective(PI/3, width/height, eyeZ/10, eyeZ*10), where eyeZ is equal to
        ((height/2) / tan(PI/6)).
        """
        if not far:
            eye_z = self._p5js.height * 0.5 / 0.5773502691896256
            self._p5js.perspective(
                1.0471975511965976,
                self._p5js.width / self._p5js.height,
                eye_z * 0.1,
                eye_z * 10,
            )
        else:
            self._p5js.perspective(fovy, aspect, near, far)

    def ortho(
        self,
        left: float | None = None,
        right: float | None = None,
        bottom: float | None = None,
        top: float | None = None,
        near: float | None = None,
        far: float | None = None,
    ):
        """Sets an orthographic projection for the current camera in a 3D sketch
        and defines a box-shaped viewing frustum within which objects are seen.
        In this projection, all objects with the same dimension appear the same
        size, regardless of whether they are near or far from the camera.

        The parameters to this function specify the viewing frustum where left and
        right are the minimum and maximum x values, top and bottom are the minimum
        and maximum y values, and near and far are the minimum and maximum z
        values.

        If no parameters are given, the following default is used:
        ortho(-width/2, width/2, -height/2, height/2).
        """
        if not far:
            self._p5js.ortho(
                -self._p5js.width * 0.5,
                self._p5js.width * 0.5,
                -self._p5js.height * 0.5,
                self._p5js.height * 0.5,
                self._p5js.height * 0.5,
                0,
            )
        else:
            self._p5js.ortho(left, right, bottom, top, near, far)

    def frustum(
        self,
        left: float | None = None,
        right: float | None = None,
        bottom: float | None = None,
        top: float | None = None,
        near: float | None = None,
        far: float | None = None,
    ):
        """Sets the frustum of the current camera as defined by the parameters.

        A frustum is a geometric form: a pyramid with its top cut off. With the
        viewer's eye at the imaginary top of the pyramid, the six planes of the
        frustum act as clipping planes when rendering a 3D view. Thus, any form
        inside the clipping planes is visible; anything outside those planes is
        not visible.

        Setting the frustum changes the perspective of the scene being rendered.
        This can be achieved more simply in many cases by using perspective().

        If no parameters are given, the following default is used:
        frustum(-width/2, width/2, -height/2, height/2, 0, max(width, height)).
        """
        if not far:
            self._p5js.frustum(
                -self._p5js.width * 0.5,
                self._p5js.width * 0.5,
                -self._p5js.height * 0.5,
                self._p5js.height * 0.5,
                0,
                self._p5js.max(self._p5js.width, self._p5js.height),
            )
        else:
            self._p5js.frustum(left, right, bottom, top, near, far)

    def create_camera(self) -> object:
        """Creates a new p5.Camera object and sets it as the current (active)
        camera.

        The new camera is initialized with a default position (see camera()) and
        a default perspective projection (see perspective()). Its properties can
        be controlled with the p5.Camera methods.

        Note: Every 3D sketch starts with a default camera initialized. This
        camera can be controlled with the global methods camera(),
        perspective(), ortho(), and frustum() if it is the only camera in the
        scene.
        """
        return self._p5js.createCamera()

    def set_camera(self, cam: object):
        """Sets the current (active) camera of a 3D sketch.
        Allows for switching between multiple cameras.
        """
        self._p5js.setCamera(cam)
