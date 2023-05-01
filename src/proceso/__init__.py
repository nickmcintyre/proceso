from typing import Annotated, Callable

from ._setup import *
from ._binding import _p5js
from .constants import (
    P2D,
    WEBGL,
    HALF_PI,
    PI,
    QUARTER_PI,
    TAU,
    TWO_PI,
    DEGREES,
    RADIANS,
    CORNER,
    CORNERS,
    RADIUS,
    RIGHT,
    LEFT,
    CENTER,
    TOP,
    BOTTOM,
    BASELINE,
    POINTS,
    LINES,
    LINE_STRIP,
    LINE_LOOP,
    TRIANGLES,
    TRIANGLE_FAN,
    TRIANGLE_STRIP,
    QUADS,
    QUAD_STRIP,
    TESS,
    CLOSE,
    OPEN,
    CHORD,
    PIE,
    PROJECT,
    SQUARE,
    ROUND,
    BEVEL,
    MITER,
    # COLOR
    RGB,
    HSB,
    HSL,
    # DOM EXTENSION
    AUTO,
    # INPUT
    ALT,
    BACKSPACE,
    CONTROL,
    DELETE,
    DOWN_ARROW,
    ENTER,
    ESCAPE,
    LEFT_ARROW,
    OPTION,
    RETURN,
    RIGHT_ARROW,
    SHIFT,
    TAB,
    UP_ARROW,
    # RENDERING
    BLEND,
    REMOVE,
    ADD,
    DARKEST,
    LIGHTEST,
    DIFFERENCE,
    SUBTRACT,
    EXCLUSION,
    MULTIPLY,
    SCREEN,
    REPLACE,
    OVERLAY,
    HARD_LIGHT,
    SOFT_LIGHT,
    DODGE,
    BURN,
    # FILTERS
    THRESHOLD,
    GRAY,
    OPAQUE,
    INVERT,
    POSTERIZE,
    DILATE,
    ERODE,
    BLUR,
    # TYPOGRAPHY
    NORMAL,
    ITALIC,
    BOLD,
    BOLDITALIC,
    CHAR,
    WORD,
    # VERTICES
    LINEAR,
    QUADRATIC,
    BEZIER,
    CURVE,
    # WEBGL DRAWMODES
    STROKE,
    FILL,
    TEXTURE,
    IMMEDIATE,
    # WEBGL TEXTURE MODE
    # NORMAL already exists for typography
    IMAGE,
    # WEBGL TEXTURE WRAP AND FILTERING
    # LINEAR already exists above
    NEAREST,
    REPEAT,
    CLAMP,
    MIRROR,
    # DEVICE-ORIENTATION
    LANDSCAPE,
    PORTRAIT,
    # ACCESSIBILITY
    GRID,
    AXES,
    LABEL,
    FALLBACK,
    CONTAIN,
    COVER,
    # CAMERA
    VIDEO,
    AUDIO,
)
from .colors import (
    # Creating & Reading
    alpha,
    blue,
    brightness,
    color,
    green,
    hue,
    lerp_color,
    lightness,
    red,
    saturation,
    # Setting
    background,
    clear,
    color_mode,
    fill,
    no_fill,
    no_stroke,
    stroke,
    erase,
    no_erase,
)
from .data import (
    # String Functions
    nf,
    nfc,
    nfp,
    nfs,
)
from .dom import (
    select,
    select_all,
    remove_elements,
    create_div,
    create_p,
    create_span,
    create_img,
    create_a,
    create_slider,
    create_button,
    create_checkbox,
    create_select,
    create_radio,
    create_color_picker,
    create_input,
    create_file_input,
    create_video,
    create_audio,
    create_capture,
    create_element,
)
from .environment import (
    describe,
    describe_element,
    text_output,
    grid_output,
    cursor,
    frame_rate,
    get_target_frame_rate,
    hide_cursor,
    fullscreen,
    pixel_density,
    display_density,
    get_url,
    get_url_path,
    get_url_params,
)
from .events import (
    # Acceleration
    set_move_threshold,
    set_shake_threshold,
    # Mouse
    request_pointer_lock,
    exit_pointer_lock,
)
from .images import (
    create_image,
    save_canvas,
    save_frames,
    # Loading & Displaying
    load_image,
    save_gif,
    image,
    tint,
    no_tint,
    image_mode,
    # Pixels
    blend,
    copy,
    filter,
    get,
    load_pixels,
    set,
    update_pixels,
)
from .math import (
    # Calculation
    abs,
    ceil,
    constrain,
    dist,
    exp,
    floor,
    lerp,
    mag,
    remap,
    max,
    min,
    norm,
    pow,
    round,
    sq,
    sqrt,
    fract,
    # Vector
    Vector,
    Vector2D,
    Vector3D,
    Vector4D,
    # Noise
    noise,
    noise_detail,
    noise_seed,
    # Random,
    random_seed,
    random,
    random_gaussian,
    # Trigonometry
    acos,
    asin,
    atan,
    atan2,
    cos,
    sin,
    tan,
    degrees,
    radians,
    angle_mode,
)
from .rendering import (
    create_canvas,
    resize_canvas,
    no_canvas,
    create_graphics,
    blend_mode,
    set_attributes,
)
from .shape import (
    # 2D Primitives
    arc,
    ellipse,
    circle,
    line,
    point,
    quad,
    rect,
    square,
    triangle,
    # Attributes
    ellipse_mode,
    no_smooth,
    rect_mode,
    smooth,
    stroke_cap,
    stroke_join,
    stroke_weight,
    # Curves
    bezier,
    bezier_detail,
    bezier_point,
    bezier_tangent,
    curve,
    curve_detail,
    curve_tightness,
    curve_point,
    curve_tangent,
    # Vertex
    begin_contour,
    begin_shape,
    bezier_vertex,
    curve_vertex,
    end_contour,
    end_shape,
    quadratic_vertex,
    vertex,
    normal,
    # 3D Primitives
    plane,
    box,
    sphere,
    cylinder,
    cone,
    ellipsoid,
    torus,
    # 3D Models
    load_model,
    model,
)
from .structure import (
    remove,
    no_loop,
    loop,
    is_looping,
    push,
    pop,
    redraw,
)
from .three_d import (
    # Interaction
    orbit_control,
    debug_mode,
    no_debug_mode,
    # Lights
    ambient_light,
    specular_color,
    directional_light,
    point_light,
    lights,
    light_falloff,
    spot_light,
    no_lights,
    # Camera
    camera,
    perspective,
    ortho,
    frustum,
    create_camera,
    set_camera,
)
from .transform import (
    apply_matrix,
    reset_matrix,
    rotate,
    rotate_x,
    rotate_y,
    rotate_z,
    scale,
    shear_x,
    shear_y,
    translate,
)
from .typography import (
    # Attributes
    text_align,
    text_leading,
    text_size,
    text_style,
    text_width,
    text_ascent,
    text_descent,
    text_wrap,
    # Loading & Displaying
    load_font,
    text,
    text_font,
)


# ================
# System variables
# ================

# Environment
frame_count: Annotated[
    int,
    """The system variable frame_count contains the number of frames that
    have been displayed since the program started. Inside setup() the value is
    0, after the first iteration of draw() it is 1, etc.
    """,
] = _p5js.frameCount
delta_time: Annotated[
    float,
    """The system variable delta_time contains the time difference between the beginning of the previous frame and the beginning of the current frame in milliseconds.
    This variable is useful for creating time sensitive animation or physics calculation that should stay constant regardless of frame rate.
    """,
] = _p5js.deltaTime
focused: Annotated[
    bool,
    """Confirms if the window a p5 program is in is "focused," meaning that
    the sketch will accept mouse or keyboard input. This variable is True if
    the window is focused and False if not.
    """,
] = _p5js.focused
display_width: Annotated[
    int,
    """System variable that stores the width of the screen display according to The default pixel_density. This is used to run a full-screen program on any display size.
    To return actual screen size, multiply this by pixel_density.
    """,
] = _p5js.displayWidth
display_height: Annotated[
    int,
    """System variable that stores the height of the screen display according to The default pixel_density. This is used to run a full-screen program on any display size.
    To return actual screen size, multiply this by pixel_density.
    """,
] = _p5js.displayHeight
window_width: Annotated[
    int,
    """System variable that stores the width of the inner window, it maps to
    window.innerWidth.
    """,
] = _p5js.windowWidth
window_height: Annotated[
    int,
    """System variable that stores the height of the inner window, it maps to
    window.innerHeight.
    """,
] = _p5js.windowHeight
width: Annotated[
    int,
    """System variable that stores the width of the drawing canvas. This value
    is set by the first parameter of the create_canvas() function. For
    example, the function call create_canvas(320, 240) sets the width variable
    to the value 320. The value of width defaults to 100 if create_canvas() is
    not used in a program.
    """,
] = _p5js.width
height: Annotated[
    int,
    """System variable that stores the height of the drawing canvas. This
    value is set by the second parameter of the createCanvas() function. For
    example, the function call create_canvas(320, 240) sets the height
    variable to the value 240. The value of height defaults to 100 if
    create_canvas() is not used in a program.
    """,
] = _p5js.height

# Events
device_orientation: Annotated[
    str,
    """The system variable device_orientation always contains the orientation
    of the device. The value of this variable will either be set 'landscape'
    or 'portrait'. If no data is available it will be set to 'undefined'.
    Either LANDSCAPE or PORTRAIT.
    """,
] = _p5js.deviceOrientation
acceleration_x: Annotated[
    float,
    """The system variable acceleration_x always contains the acceleration of
    the device along the x axis. Value is represented as meters per second
    squared.
    """,
] = _p5js.accelerationX
acceleration_y: Annotated[
    float,
    """The system variable acceleration_y always contains the acceleration of
    the device along the y axis. Value is represented as meters per second
    squared.
    """,
] = _p5js.accelerationY
acceleration_z: Annotated[
    float,
    """The system variable acceleration_z always contains the acceleration of
    the device along the z axis. Value is represented as meters per second
    squared.
    """,
] = _p5js.accelerationZ
pacceleration_x: Annotated[
    float,
    """The system variable pacceleration_ always contains the acceleration of
    the device along the x axis in the frame previous to the current frame.
    Value is represented as meters per second squared.
    """,
] = _p5js.pAccelerationX
pacceleration_y: Annotated[
    float,
    """The system variable pacceleration_y always contains the acceleration of
    the device along the y axis in the frame previous to the current frame.
    Value is represented as meters per second squared.
    """,
] = _p5js.pAccelerationY
pacceleration_z: Annotated[
    float,
    """The system variable pacceleration_z always contains the acceleration of
    the device along the z axis in the frame previous to the current frame.
    Value is represented as meters per second squared.
    """,
] = _p5js.pAccelerationZ
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
] = _p5js.rotationX
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
] = _p5js.rotationY
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
] = _p5js.rotationZ
protation_x: Annotated[
    float,
    """The system variable protation_x always contains the rotation of the
    device along the x axis in the frame previous to the current frame.
    If the sketch angle_mode() is set to DEGREES, the value will be -180 to
    180. If it is set to RADIANS, the value will be -PI to PI.

    protation_x can also be used with rotation_x to determine the rotate
    direction of the device along the X-axis.
    """,
] = _p5js.pRotationX
protation_y: Annotated[
    float,
    """The system variable protation_y always contains the rotation of the
    device along the y axis in the frame previous to the current frame.
    If the sketch angle_mode() is set to DEGREES, the value will be -90 to 90.
    If it is set to RADIANS, the value will be -PI/2 to PI/2.

    protation_y can also be used with rotation_y to determine the rotate
    direction of the device along the Y-axis.
    """,
] = _p5js.pRotationY
protation_z: Annotated[
    float,
    """The system variable protation_z always contains the rotation of the
    device along the z axis in the frame previous to the current frame.
    If the sketch angle_mode() is set to DEGREES, the value will be 0 to 360.
    If it is set to RADIANS, the value will be 0 to 2*PI.

    protation_z can also be used with rotation_z to determine the rotate
    direction of the device along the Z-axis.
    """,
] = _p5js.pRotationZ
turn_axis: Annotated[
    str,
    """When a device is rotated, the axis that triggers the device_turned()
    function is stored in the turn_axis variable.
    The turn_axis variable is only defined within the scope of
    device_turned().
    """,
] = _p5js.turnAxis
# device_moved = _p5js.deviceMoved
# device_turned = _p5js.deviceTurned
# device_shaken = _p5js.deviceShaken
key_is_pressed: Annotated[
    bool,
    """The boolean system variable key_is_pressed is True if any key is
    pressed and False if no keys are pressed.
    """,
] = _p5js.keyIsPressed
key: Annotated[
    str,
    """The system variable key always contains the value of the most recent
    key on the keyboard that was typed.
    To get the proper capitalization, it is best to use it within key_typed().
    For non-ASCII keys, use the key_code variable.
    """,
] = _p5js.key
key_code: Annotated[
    int,
    """The variable key_code is used to detect special keys such as BACKSPACE,
    DELETE, ENTER, RETURN, TAB, ESCAPE, SHIFT, CONTROL, OPTION, ALT, UP_ARROW,
    DOWN_ARROW, LEFT_ARROW, RIGHT_ARROW.

    You can also check for custom keys by looking up the key_code of any key
    on a site like this: keycode.info.
    """,
] = _p5js.keyCode
moved_x: Annotated[
    float,
    """The variable moved_x contains the horizontal movement of the mouse
    since the last frame.
    """,
] = _p5js.movedX
moved_y: Annotated[
    float,
    """The variable moved_y contains the vertical movement of the mouse since
    the last frame.
    """,
] = _p5js.movedY
mouse_x: Annotated[
    float,
    """The system variable mouse_x always contains the current horizontal
    position of the mouse, relative to (0, 0) of the canvas.
    The value at the top-left corner is (0, 0) for 2-D and
    (-width/2, -height/2) for WebGL.
    If touch is used instead of mouse input, mouse_x will hold the x value of
    the most recent touch point.
    """,
] = _p5js.mouseX
mouse_y: Annotated[
    float,
    """The system variable mouse_y always contains the current vertical
    position of the mouse, relative to (0, 0) of the canvas.
    The value at the top-left corner is (0, 0) for 2-D and
    (-width/2, -height/2) for WebGL.
    If touch is used instead of mouse input, mouse_y will hold the y value of
    the most recent touch point.
    """,
] = _p5js.mouseY
pmouse_x: Annotated[
    float,
    """The system variable pmouse_x always contains the horizontal position of
    the mouse or finger in the frame previous to the current frame,
    relative to (0, 0) of the canvas. The value at the top-left corner is
    (0, 0) for 2-D and (-width/2, -height/2) for WebGL.
    Note: pmouse_x will be reset to the current mouseX value at the start of
    each touch event.
    """,
] = _p5js.pmouseX
pmouse_y: Annotated[
    float,
    """The system variable pmouse_y always contains the vertical position of
    the mouse or finger in the frame previous to the current frame,
    relative to (0, 0) of the canvas. The value at the top-left corner is
    (0, 0) for 2-D and (-width/2, -height/2) for WebGL.
    Note: pmouse_y will be reset to the current mouseY value at the start of
    each touch event.
    """,
] = _p5js.pmouseY
winmouse_x: Annotated[
    float,
    """The system variable winmouse_x always contains the current horizontal
    position of the mouse, relative to (0, 0) of the window.
    """,
] = _p5js.winMouseX
winmouse_y: Annotated[
    float,
    """The system variable winmouse_y always contains the current vertical
    position of the mouse, relative to (0, 0) of the window.
    """,
] = _p5js.winMouseY
pwinmouse_x: Annotated[
    float,
    """The system variable pwinmouse_x always contains the horizontal position
    of the mouse in the frame previous to the current frame, relative to
    (0, 0) of the window. Note: pwinmouse_x will be reset to the current
    winmouse_x value at the start of each touch event.
    """,
] = _p5js.pwinMouseX
pwinmouse_y: Annotated[
    float,
    """The system variable pwinmouse_y always contains the vertical position
    of the mouse in the frame previous to the current frame, relative to
    (0, 0) of the window. Note: pwinmouse_y will be reset to the current
    winmouse_y value at the start of each touch event.
    """,
] = _p5js.pwinMouseY
mouse_button: Annotated[
    str,
    """p5 automatically tracks if the mouse button is pressed and which button
    is pressed. The value of the system variable mouse_button is either LEFT,
    RIGHT, or CENTER depending on which button was pressed last. Warning:
    different browsers may track mouse_button differently.
    """,
] = _p5js.mouseButton
mouse_is_pressed: Annotated[
    bool,
    """The boolean system variable mouse_is_pressed is True if the mouse is
    pressed and False if not.
    """,
] = _p5js.mouseIsPressed
# touch_started = _p5js.touchStarted
# touch_moved = _p5js.touchMoved
# touch_ended = _p5js.touchEnded
touches: Annotated[
    list[object],
    """The system variable touches[] contains an array of the positions of all
    current touch points, relative to (0, 0) of the canvas, and IDs
    identifying a unique touch as it moves. Each element in the array is an
    object with x, y, and id properties.

    The touches[] array is not supported on Safari and IE on touch-based
    desktops (laptops).
    """,
] = _p5js.touches

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
] = _p5js.pixels


def _update_system_variables():
    # Environment
    global frame_count, delta_time, focused, display_width, display_height
    global window_width, window_height, width, height
    # Events
    global device_orientation, acceleration_x, acceleration_y, acceleration_z
    global pacceleration_x, pacceleration_y, pacceleration_z
    global rotation_x, rotation_y, rotation_z
    global protation_x, protation_y, protation_z
    global turn_axis, key_is_pressed, key, key_code
    global moved_x, moved_y, mouse_x, mouse_y, pmouse_x, pmouse_y
    global winmouse_x, winmouse_y, pwinmouse_x, pwinmouse_y
    global mouse_button, mouse_is_pressed
    global touches
    global pixels

    # Environment
    frame_count = _p5js.frameCount
    delta_time = _p5js.deltaTime
    focused = _p5js.focused
    display_width = _p5js.displayWidth
    display_height = _p5js.displayHeight
    window_width = _p5js.windowWidth
    window_height = _p5js.windowHeight
    width = _p5js.width
    height = _p5js.height
    # Events
    device_orientation = _p5js.deviceOrientation
    acceleration_x = _p5js.accelerationX
    acceleration_y = _p5js.accelerationY
    acceleration_z = _p5js.accelerationZ
    pacceleration_x = _p5js.pAccelerationX
    pacceleration_y = _p5js.pAccelerationY
    pacceleration_z = _p5js.pAccelerationZ
    rotation_x = _p5js.rotationX
    rotation_y = _p5js.rotationY
    rotation_z = _p5js.rotationZ
    protation_x = _p5js.pRotationX
    protation_y = _p5js.pRotationY
    protation_z = _p5js.pRotationZ
    turn_axis = _p5js.turnAxis
    key_is_pressed = _p5js.keyIsPressed
    key = _p5js.key
    key_code = _p5js.keyCode
    moved_x = _p5js.movedX
    moved_y = _p5js.movedY
    mouse_x = _p5js.mouseX
    mouse_y = _p5js.mouseY
    pmouse_x = _p5js.pmouseX
    pmouse_y = _p5js.pmouseY
    winmouse_x = _p5js.winMouseX
    winmouse_y = _p5js.winMouseY
    pwinmouse_x = _p5js.pwinMouseX
    pwinmouse_y = _p5js.pwinMouseY
    mouse_button = _p5js.mouseButton
    mouse_is_pressed = _p5js.mouseIsPressed
    touches = _p5js.touches
    pixels = _p5js.pixels


def run(
    preload: Callable | None = None,
    setup: Callable | None = None,
    draw: Callable | None = None,
    key_pressed: Callable | None = None,
    key_released: Callable | None = None,
    key_typed: Callable | None = None,
    key_is_down: Callable | None = None,
    mouse_moved: Callable | None = None,
    mouse_dragged: Callable | None = None,
    mouse_pressed: Callable | None = None,
    mouse_released: Callable | None = None,
    mouse_clicked: Callable | None = None,
    double_clicked: Callable | None = None,
    mouse_wheel: Callable | None = None,
    request_pointer_lock: Callable | None = None,
    exit_pointer_lock: Callable | None = None,
):
    """Runs a sketch in dynamic mode and executes any event functions."""

    import inspect
    from pyodide.ffi import create_proxy

    from ._setup import _init_global_mode

    # =========
    # Structure
    # =========
    if callable(preload):
        _p5js.preload = create_proxy(preload)
    if callable(setup):
        _p5js.setup = create_proxy(setup)
    if callable(draw):

        def _draw(*args):
            draw()
            _update_system_variables()

        _p5js.draw = create_proxy(_draw)

    # ======
    # Events
    # ======
    def wrap_event_func(func: Callable):
        args = inspect.signature(func).parameters
        if len(args) == 0:

            def wrapped_func(event):
                func()

            return create_proxy(wrapped_func)
        else:
            return create_proxy(func)

    if callable(key_pressed):
        _p5js.keyPressed = wrap_event_func(key_pressed)
    if callable(key_released):
        _p5js.keyReleased = wrap_event_func(key_released)
    if callable(key_typed):
        _p5js.keyTyped = wrap_event_func(key_typed)
    if callable(key_is_down):
        _p5js.keyIsDown = create_proxy(key_is_down)
    if callable(mouse_moved):
        _p5js.mouseMoved = wrap_event_func(mouse_moved)
    if callable(mouse_dragged):
        _p5js.mouseDragged = wrap_event_func(mouse_dragged)
    if callable(mouse_pressed):
        _p5js.mousePressed = wrap_event_func(mouse_pressed)
    if callable(mouse_released):
        _p5js.mouseReleased = wrap_event_func(mouse_released)
    if callable(mouse_clicked):
        _p5js.mouseClicked = wrap_event_func(mouse_clicked)
    if callable(double_clicked):
        _p5js.doubleClicked = wrap_event_func(double_clicked)
    if callable(mouse_wheel):
        _p5js.mouseWheel = create_proxy(mouse_wheel)
    if callable(request_pointer_lock):
        _p5js.requestPointerLock = create_proxy(request_pointer_lock)
    if callable(exit_pointer_lock):
        _p5js.exitPointerLock = create_proxy(exit_pointer_lock)

    # FIXME: This is a hack to make preload work
    _p5js.remove()
    _init_global_mode()
