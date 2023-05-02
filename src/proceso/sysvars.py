from typing import Annotated


class SystemVariables:
    # Environment
    frame_count: Annotated[
        int,
        """The system variable frame_count contains the number of frames that
        have been displayed since the program started. Inside setup() the value is
        0, after the first iteration of draw() it is 1, etc.
        """,
    ]
    delta_time: Annotated[
        float,
        """The system variable delta_time contains the time difference between the beginning of the previous frame and the beginning of the current frame in milliseconds.
        This variable is useful for creating time sensitive animation or physics calculation that should stay constant regardless of frame rate.
        """,
    ]
    focused: Annotated[
        bool,
        """Confirms if the window a p5 program is in is "focused," meaning that
        the sketch will accept mouse or keyboard input. This variable is True if
        the window is focused and False if not.
        """,
    ]
    display_width: Annotated[
        int,
        """System variable that stores the width of the screen display according to The default pixel_density. This is used to run a full-screen program on any display size.
        To return actual screen size, multiply this by pixel_density.
        """,
    ]
    display_height: Annotated[
        int,
        """System variable that stores the height of the screen display according to The default pixel_density. This is used to run a full-screen program on any display size.
        To return actual screen size, multiply this by pixel_density.
        """,
    ]
    window_width: Annotated[
        int,
        """System variable that stores the width of the inner window, it maps to
        window.innerWidth.
        """,
    ]
    window_height: Annotated[
        int,
        """System variable that stores the height of the inner window, it maps to
        window.innerHeight.
        """,
    ]
    width: Annotated[
        int,
        """System variable that stores the width of the drawing canvas. This value
        is set by the first parameter of the create_canvas() function. For
        example, the function call create_canvas(320, 240) sets the width variable
        to the value 320. The value of width defaults to 100 if create_canvas() is
        not used in a program.
        """,
    ] = 100
    height: Annotated[
        int,
        """System variable that stores the height of the drawing canvas. This
        value is set by the second parameter of the createCanvas() function. For
        example, the function call create_canvas(320, 240) sets the height
        variable to the value 240. The value of height defaults to 100 if
        create_canvas() is not used in a program.
        """,
    ] = 100

    # Events
    device_orientation: Annotated[
        str,
        """The system variable device_orientation always contains the orientation
        of the device. The value of this variable will either be set 'landscape'
        or 'portrait'. If no data is available it will be set to 'undefined'.
        Either LANDSCAPE or PORTRAIT.
        """,
    ]
    acceleration_x: Annotated[
        float,
        """The system variable acceleration_x always contains the acceleration of
        the device along the x axis. Value is represented as meters per second
        squared.
        """,
    ]
    acceleration_y: Annotated[
        float,
        """The system variable acceleration_y always contains the acceleration of
        the device along the y axis. Value is represented as meters per second
        squared.
        """,
    ]
    acceleration_z: Annotated[
        float,
        """The system variable acceleration_z always contains the acceleration of
        the device along the z axis. Value is represented as meters per second
        squared.
        """,
    ]
    pacceleration_x: Annotated[
        float,
        """The system variable pacceleration_ always contains the acceleration of
        the device along the x axis in the frame previous to the current frame.
        Value is represented as meters per second squared.
        """,
    ]
    pacceleration_y: Annotated[
        float,
        """The system variable pacceleration_y always contains the acceleration of
        the device along the y axis in the frame previous to the current frame.
        Value is represented as meters per second squared.
        """,
    ]
    pacceleration_z: Annotated[
        float,
        """The system variable pacceleration_z always contains the acceleration of
        the device along the z axis in the frame previous to the current frame.
        Value is represented as meters per second squared.
        """,
    ]
    rotation_x: Annotated[
        float,
        """The system variable rotation_x always contains the rotation of the
        device along the x axis. If the sketch angle_mode() is set to DEGREES,
        the value will be -180 to 180. If it is set to RADIANS, the value will be
        -PI to PI.
        
        Note: The order the rotations are called is important, ie. if used
        together, it must be called in the order Z-X-Y or there might be
        unexpected behaviour.
        """,
    ]
    rotation_y: Annotated[
        float,
        """The system variable rotation_y always contains the rotation of the
        device along the y axis. If the sketch angle_mode() is set to DEGREES,
        the value will be -90 to 90. If it is set to RADIANS, the value will be
        -PI/2 to PI/2.

        Note: The order the rotations are called is important, ie. if used
        together, it must be called in the order Z-X-Y or there might be
        unexpected behaviour.
        """,
    ]
    rotation_z: Annotated[
        float,
        """The system variable rotation_z always contains the rotation of the
        device along the z axis. If the sketch angleMode() is set to DEGREES,
        the value will be 0 to 360. If it is set to RADIANS, the value will be 0
        to 2*PI.

        Unlike rotation_x and rotation_y, this variable is available for devices
        with a built-in compass only.

        Note: The order the rotations are called is important, ie. if used
        together, it must be called in the order Z-X-Y or there might be
        unexpected behaviour.
        """,
    ]
    protation_x: Annotated[
        float,
        """The system variable protation_x always contains the rotation of the
        device along the x axis in the frame previous to the current frame.
        If the sketch angle_mode() is set to DEGREES, the value will be -180 to
        180. If it is set to RADIANS, the value will be -PI to PI.

        protation_x can also be used with rotation_x to determine the rotate
        direction of the device along the X-axis.
        """,
    ]
    protation_y: Annotated[
        float,
        """The system variable protation_y always contains the rotation of the
        device along the y axis in the frame previous to the current frame.
        If the sketch angle_mode() is set to DEGREES, the value will be -90 to 90.
        If it is set to RADIANS, the value will be -PI/2 to PI/2.

        protation_y can also be used with rotation_y to determine the rotate
        direction of the device along the Y-axis.
        """,
    ]
    protation_z: Annotated[
        float,
        """The system variable protation_z always contains the rotation of the
        device along the z axis in the frame previous to the current frame.
        If the sketch angle_mode() is set to DEGREES, the value will be 0 to 360.
        If it is set to RADIANS, the value will be 0 to 2*PI.

        protation_z can also be used with rotation_z to determine the rotate
        direction of the device along the Z-axis.
        """,
    ]
    turn_axis: Annotated[
        str,
        """When a device is rotated, the axis that triggers the device_turned()
        function is stored in the turn_axis variable.
        The turn_axis variable is only defined within the scope of
        device_turned().
        """,
    ]
    # device_moved
    # device_turned
    # device_shaken
    is_key_pressed: Annotated[
        bool,
        """The boolean system variable is_key_pressed is True if any key is
        pressed and False if no keys are pressed.
        """,
    ]
    key: Annotated[
        str,
        """The system variable key always contains the value of the most recent
        key on the keyboard that was typed.
        To get the proper capitalization, it is best to use it within key_typed().
        For non-ASCII keys, use the key_code variable.
        """,
    ]
    key_code: Annotated[
        int,
        """The variable key_code is used to detect special keys such as BACKSPACE,
        DELETE, ENTER, RETURN, TAB, ESCAPE, SHIFT, CONTROL, OPTION, ALT, UP_ARROW,
        DOWN_ARROW, LEFT_ARROW, RIGHT_ARROW.

        You can also check for custom keys by looking up the key_code of any key
        on a site like this: keycode.info.
        """,
    ]
    moved_x: Annotated[
        float,
        """The variable moved_x contains the horizontal movement of the mouse
        since the last frame.
        """,
    ]
    moved_y: Annotated[
        float,
        """The variable moved_y contains the vertical movement of the mouse since
        the last frame.
        """,
    ]
    mouse_x: Annotated[
        float,
        """The system variable mouse_x always contains the current horizontal
        position of the mouse, relative to (0, 0) of the canvas.
        The value at the top-left corner is (0, 0) for 2-D and
        (-width/2, -height/2) for WebGL.
        If touch is used instead of mouse input, mouse_x will hold the x value of
        the most recent touch point.
        """,
    ]
    mouse_y: Annotated[
        float,
        """The system variable mouse_y always contains the current vertical
        position of the mouse, relative to (0, 0) of the canvas.
        The value at the top-left corner is (0, 0) for 2-D and
        (-width/2, -height/2) for WebGL.
        If touch is used instead of mouse input, mouse_y will hold the y value of
        the most recent touch point.
        """,
    ]
    pmouse_x: Annotated[
        float,
        """The system variable pmouse_x always contains the horizontal position of
        the mouse or finger in the frame previous to the current frame,
        relative to (0, 0) of the canvas. The value at the top-left corner is
        (0, 0) for 2-D and (-width/2, -height/2) for WebGL.
        Note: pmouse_x will be reset to the current mouseX value at the start of
        each touch event.
        """,
    ]
    pmouse_y: Annotated[
        float,
        """The system variable pmouse_y always contains the vertical position of
        the mouse or finger in the frame previous to the current frame,
        relative to (0, 0) of the canvas. The value at the top-left corner is
        (0, 0) for 2-D and (-width/2, -height/2) for WebGL.
        Note: pmouse_y will be reset to the current mouseY value at the start of
        each touch event.
        """,
    ]
    winmouse_x: Annotated[
        float,
        """The system variable winmouse_x always contains the current horizontal
        position of the mouse, relative to (0, 0) of the window.
        """,
    ]
    winmouse_y: Annotated[
        float,
        """The system variable winmouse_y always contains the current vertical
        position of the mouse, relative to (0, 0) of the window.
        """,
    ]
    pwinmouse_x: Annotated[
        float,
        """The system variable pwinmouse_x always contains the horizontal position
        of the mouse in the frame previous to the current frame, relative to
        (0, 0) of the window. Note: pwinmouse_x will be reset to the current
        winmouse_x value at the start of each touch event.
        """,
    ]
    pwinmouse_y: Annotated[
        float,
        """The system variable pwinmouse_y always contains the vertical position
        of the mouse in the frame previous to the current frame, relative to
        (0, 0) of the window. Note: pwinmouse_y will be reset to the current
        winmouse_y value at the start of each touch event.
        """,
    ]
    mouse_button: Annotated[
        str,
        """p5 automatically tracks if the mouse button is pressed and which button
        is pressed. The value of the system variable mouse_button is either LEFT,
        RIGHT, or CENTER depending on which button was pressed last. Warning:
        different browsers may track mouse_button differently.
        """,
    ]
    is_mouse_pressed: Annotated[
        bool,
        """The boolean system variable is_mouse_pressed is True if the mouse is
        pressed and False if not.
        """,
    ]
    # touch_started
    # touch_moved
    # touch_ended
    touches: Annotated[
        list[object],
        """The system variable touches[] contains an array of the positions of all
        current touch points, relative to (0, 0) of the canvas, and IDs
        identifying a unique touch as it moves. Each element in the array is an
        object with x, y, and id properties.

        The touches[] array is not supported on Safari and IE on touch-based
        desktops (laptops).
        """,
    ]

    pixels: Annotated[
        list[float],
        """List containing the values for all the pixels in the display window.
        These values are numbers. This array is the size (include an appropriate
        factor for pixel_density) of the display window x4, representing the
        R, G, B, A values in order for each pixel, moving from left to right
        across each row, then down each column. Retina and other high density
        displays will have more pixels[] (by a factor of pixel_density^2). For
        example, if the image is 100×100 pixels, there will be 40,000. On a
        retina display, there will be 160,000.

        The first four values (indices 0-3) in the array will be the R, G, B, A
        values of the pixel at (0, 0). The second four values (indices 4-7) will
        contain the R, G, B, A values of the pixel at (1, 0).
        """,
    ]

    def _update_system_variables(self):
        # Environment
        self.frame_count = self._p5js.frameCount
        self.delta_time = self._p5js.deltaTime
        self.focused = self._p5js.focused
        self.display_width = self._p5js.displayWidth
        self.display_height = self._p5js.displayHeight
        self.window_width = self._p5js.windowWidth
        self.window_height = self._p5js.windowHeight
        self.width = self._p5js.width
        self.height = self._p5js.height
        # Events
        self.device_orientation = self._p5js.deviceOrientation
        self.acceleration_x = self._p5js.accelerationX
        self.acceleration_y = self._p5js.accelerationY
        self.acceleration_z = self._p5js.accelerationZ
        self.pacceleration_x = self._p5js.pAccelerationX
        self.pacceleration_y = self._p5js.pAccelerationY
        self.pacceleration_z = self._p5js.pAccelerationZ
        self.rotation_x = self._p5js.rotationX
        self.rotation_y = self._p5js.rotationY
        self.rotation_z = self._p5js.rotationZ
        self.protation_x = self._p5js.pRotationX
        self.protation_y = self._p5js.pRotationY
        self.protation_z = self._p5js.pRotationZ
        self.turn_axis = self._p5js.turnAxis
        self.is_key_pressed = self._p5js.keyIsPressed
        self.key = self._p5js.key
        self.key_code = self._p5js.keyCode
        self.moved_x = self._p5js.movedX
        self.moved_y = self._p5js.movedY
        self.mouse_x = self._p5js.mouseX
        self.mouse_y = self._p5js.mouseY
        self.pmouse_x = self._p5js.pmouseX
        self.pmouse_y = self._p5js.pmouseY
        self.winmouse_x = self._p5js.winMouseX
        self.winmouse_y = self._p5js.winMouseY
        self.pwinmouse_x = self._p5js.pwinMouseX
        self.pwinmouse_y = self._p5js.pwinMouseY
        self.mouse_button = self._p5js.mouseButton
        self.is_mouse_pressed = self._p5js.mouseIsPressed
        self.touches = self._p5js.touches
        self.pixels = self._p5js.pixels
