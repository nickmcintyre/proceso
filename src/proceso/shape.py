from pyodide.ffi import to_js

from ._binding import BaseSketch


class Shape(BaseSketch):
    # =============
    # 2D Primitives
    # =============
    def arc(
        self,
        x: float,
        y: float,
        w: float,
        h: float,
        start: float,
        stop: float,
        mode: str | None = None,
        detail: int = 25,
    ):
        """Draw an arc to the screen.
        If called with only x, y, w, h, start and stop, the arc will be drawn and
        filled as an open pie segment. If a mode parameter is provided, the arc
        will be filled like an open semi-circle (OPEN), a closed semi-circle
        (CHORD), or as a closed pie segment (PIE). The origin may be changed with
        the ellipse_mode() function.

        The arc is always drawn clockwise from wherever start falls to wherever
        stop falls on the ellipse. Adding or subtracting TWO_PI to either angle
        does not change where they fall. If both start and stop fall at the same
        place, a full ellipse will be drawn. Be aware that the y-axis increases in
        the downward direction, therefore angles are measured clockwise from the
        positive x-direction ("3 o'clock").
        """
        self._p5js.arc(x, y, w, h, start, stop, to_js(mode), detail)

    def ellipse(
        self, x: float, y: float, w: float, h: float | None = None, detail: int = 25
    ):
        """Draws an ellipse (oval) to the screen.
        By default, the first two parameters set the location of the center of the
        ellipse, and the third and fourth parameters set the shape's width and
        height. If no height is specified, the value of width is used for both the
        width and height. If a negative height or width is specified, the absolute
        value is taken.

        An ellipse with equal width and height is a circle. The origin may be
        changed with the ellipse_mode() function.
        """
        self._p5js.ellipse(x, y, w, h, detail)

    def circle(self, x: float, y: float, d: float):
        """Draws a circle to the screen.
        A circle is a simple closed shape. It is the set of all points in a plane
        that are at a given distance from a given point, the center. This function
        is a special case of the ellipse() function, where the width and height of
        the ellipse are the same. Height and width of the ellipse correspond to
        the diameter of the circle. By default, the first two parameters set the
        location of the center of the circle, the third sets the diameter of the
        circle.
        """
        self._p5js.circle(x, y, d)

    def line(self, x1: float, y1: float, x2: float, y2: float, *args):
        """Draws a line (a direct path between two points) to the screen.
        If called with only 4 parameters, it will draw a line in 2D with a default
        width of 1 pixel. This width can be modified by using the stroke_weight()
        function. A line cannot be filled, therefore the fill() function will not
        affect the color of a line. So to color a line, use the stroke() function.
        """
        self._p5js.line(x1, y1, x2, y2, *args)

    def point(self, x: float, y: float, z: float | None = None):
        """Draws a point, a coordinate in space at the dimension of one pixel.
        The first parameter is the horizontal value for the point, the second
        param is the vertical value for the point. The color of the point is
        changed with the stroke() function. The size of the point can be changed
        with the stroke_weight() function.
        """
        self._p5js.point(x, y, z)

    def quad(
        self,
        x1: float,
        y1: float,
        x2: float,
        y2: float,
        x3: float,
        y3: float,
        x4: float,
        y4: float,
        detail_x: int | None = None,
        detail_y: int | None = None,
        *args,
    ):
        """Draws a quad on the canvas.
        A quad is a quadrilateral, a four-sided polygon. It is similar to a
        rectangle, but the angles between its edges are not constrained to ninety
        degrees. The first pair of parameters (x1,y1) sets the first vertex and
        the subsequent pairs should proceed clockwise or counter-clockwise around
        the defined shape. z-arguments only work when quad() is used in WEBGL
        mode.
        """
        self._p5js.quad(x1, y1, x2, y2, x3, y3, x4, y4, detail_x, detail_y, *args)

    def rect(
        self,
        x: float,
        y: float,
        w: float,
        h: float,
        r: float | None = None,
        tr: float | None = None,
        br: float | None = None,
        bl: float | None = None,
    ):
        """Draws a rectangle on the canvas.
        A rectangle is a four-sided closed shape with every angle at ninety
        degrees. By default, the first two parameters set the location of the
        upper-left corner, the third sets the width, and the fourth sets the
        height. The way these parameters are interpreted may be changed with the
        rect_mode() function.

        The fifth, sixth, seventh and eighth parameters, if specified, determine
        corner radius for the top-left, top-right, lower-right and lower-left
        corners, respectively. An omitted corner radius parameter is set to the
        value of the previously specified radius value in the parameter list.
        """
        self._p5js.rect(x, y, w, h, r, tr, br, bl)

    def square(
        self,
        x: float,
        y: float,
        s: float,
        tl: float | None = None,
        tr: float | None = None,
        br: float | None = None,
        bl: float | None = None,
    ):
        """Draws a square to the screen.
        A square is a four-sided shape with every angle at ninety degrees, and
        equal side size. This function is a special case of the rect() function,
        where the width and height are the same, and the parameter is called "s"
        for side size. By default, the first two parameters set the location of
        the upper-left corner, the third sets the side size of the square. The way
        these parameters are interpreted, may be changed with the rect_mode()
        function.

        The fourth, fifth, sixth and seventh parameters, if specified, determine
        corner radius for the top-left, top-right, lower-right and lower-left
        corners, respectively. An omitted corner radius parameter is set to the
        value of the previously specified radius value in the parameter list.
        """
        self._p5js.square(x, y, s, tl, tr, br, bl)

    def triangle(
        self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float
    ):
        """Draws a triangle to the canvas.
        A triangle is a plane created by connecting three points. The first two
        arguments specify the first point, the middle two arguments specify the
        second point, and the last two arguments specify the third point.
        """
        self._p5js.triangle(x1, y1, x2, y2, x3, y3)

    # ==========
    # Attributes
    # ==========
    def ellipse_mode(self, mode: str):
        """Modifies the location from which ellipses are drawn by changing the way
        in which parameters given to ellipse(), circle() and arc() are
        interpreted.

        The default mode is CENTER, in which the first two parameters are
        interpreted as the shape's center point's x and y coordinates
        respectively, while the third and fourth parameters are its width and
        height.

        ellipse_mode(RADIUS) also uses the first two parameters as the shape's
        center point's x and y coordinates, but uses the third and fourth
        parameters to specify half of the shapes's width and height.

        ellipse_mode(CORNER) interprets the first two parameters as the upper-left
        corner of the shape, while the third and fourth parameters are its width
        and height.

        ellipse_mode(CORNERS) interprets the first two parameters as the location
        of one corner of the ellipse's bounding box, and the third and fourth
        parameters as the location of the opposite corner.

        The parameter to this function must be written in ALL CAPS because they
        are predefined as constants in ALL CAPS and Python is a case-sensitive
        language.
        """
        self._p5js.ellipseMode(mode)

    def no_smooth(self):
        """Draws all geometry with jagged (aliased) edges.

        Note that smooth() is active by default in 2D mode, so it is necessary to
        call no_smooth() to disable smoothing of geometry, images, and fonts.

        In 3D mode, no_smooth() is enabled by default, so it is necessary to call
        smooth() if you would like smooth (antialiased) edges on your geometry.
        """
        self._p5js.noSmooth()

    def rect_mode(self, mode: str):
        """Modifies the location from which rectangles are drawn by changing the
        way in which parameters given to rect() are interpreted.

        The default mode is CORNER, which interprets the first two parameters as
        the upper-left corner of the shape, while the third and fourth parameters
        are its width and height.

        rectMode(CORNERS) interprets the first two parameters as the location of
        one of the corners, and the third and fourth parameters as the location
        of the diagonally opposite corner. Note, the rectangle is drawn between
        the coordinates, so it is not necessary that the first corner be the
        upper left corner.

        rectMode(CENTER) interprets the first two parameters as the shape's center
        point, while the third and fourth parameters are its width and height.

        rectMode(RADIUS) also uses the first two parameters as the shape's center
        point, but uses the third and fourth parameters to specify half of the
        shape's width and height respectively.

        The parameter to this function must be written in ALL CAPS because they
        are predefined as constants in ALL CAPS and Python is a case-sensitive
        language.
        """
        self._p5js.rectMode(mode)

    def smooth(self):
        """Draws all geometry with smooth (anti-aliased) edges.
        smooth() will also improve image quality of resized images.

        Note that smooth() is active by default in 2D mode; no_smooth() can be
        used to disable smoothing of geometry, images, and fonts.

        In 3D mode, no_smooth() is enabled by default, so it is necessary to call
        smooth() if you would like smooth (antialiased) edges on your geometry.
        """
        self._p5js.smooth()

    def stroke_cap(self, cap: str):
        """Sets the style for rendering line endings.
        These ends are either rounded, squared, or extended, each of which
        specified with the corresponding parameters: ROUND, SQUARE, or PROJECT.
        The default cap is ROUND.

        The parameter to this function must be written in ALL CAPS because they
        are predefined as constants in ALL CAPS and Python is a case-sensitive
        language.
        """
        self._p5js.strokeCap(cap)

    def stroke_join(self, join: str):
        """Sets the style of the joints which connect line segments.
        These joints are either mitered, beveled, or rounded and specified with
        the corresponding parameters: MITER, BEVEL, or ROUND. The default joint is
        MITER in 2D mode and ROUND in WebGL mode.

        The parameter to this function must be written in ALL CAPS because they
        are predefined as constants in ALL CAPS and Python is a case-sensitive
        language.
        """
        self._p5js.strokeJoin(join)

    def stroke_weight(self, weight: float):
        """Sets the width of the stroke used for lines, points, and the border
        around shapes.
        All widths are set in units of pixels.

        Note that it is affected by any transformation or scaling that has been
        applied previously.
        """
        self._p5js.strokeWeight(weight)

    # ======
    # Curves
    # ======
    def bezier(
        self,
        x1: float,
        y1: float,
        x2: float,
        y2: float,
        x3: float,
        y3: float,
        x4: float,
        y4: float,
        *args,
    ):
        """Draws a cubic Bezier curve on the screen.
        These curves are defined by a series of anchor and control points. The
        first two parameters specify the first anchor point and the last two
        parameters specify the other anchor point, which become the first and
        last points on the curve. The middle parameters specify the two control
        points which define the shape of the curve. Approximately speaking,
        control points "pull" the curve towards them.

        Bezier curves were developed by French automotive engineer Pierre Bezier,
        and are commonly used in computer graphics to define gently sloping
        curves. See also curve().
        """
        self._p5js.bezier(x1, y1, x2, y2, x3, y3, x4, y4, *args)

    def bezier_detail(self, detail: float):
        """Sets the resolution at which Bezier's curve is displayed.
        The default value is 20.

        Note, This function is only useful when using the WEBGL renderer as the
        default canvas renderer does not use this information.
        """
        self._p5js.bezierDetail(detail)

    def bezier_point(self, a: float, b: float, c: float, d: float, t: float):
        """Given the x or y co-ordinate values of control and anchor points of a
        bezier curve, it evaluates the x or y coordinate of the bezier at position
        t.
        The parameters a and d are the x or y coordinates of first and last points
        on the curve while b and c are of the control points.The final parameter t
        is the position of the resultant point which is given between 0 and 1.
        This can be done once with the x coordinates and a second time with the y
        coordinates to get the location of a bezier curve at t.
        """
        self._p5js.bezierPoint(a, b, c, d, t)

    def bezier_tangent(self, a: float, b: float, c: float, d: float, t: float):
        """Evaluates the tangent to the Bezier at position t for points
        a, b, c, d.
        The parameters a and d are the first and last points on the curve, and b
        and c are the control points. The final parameter t varies between 0
        and 1.
        """
        self._p5js.bezierTangent(a, b, c, d, t)

    def curve(
        self,
        x1: float,
        y1: float,
        x2: float,
        y2: float,
        x3: float,
        y3: float,
        x4: float,
        y4: float,
        *args,
    ):
        """Draws a curved line on the screen between two points, given as the
        middle four parameters. The first two parameters are a control point, as
        if the curve came from this point even though it's not drawn. The last two
        parameters similarly describe the other control point.

        Longer curves can be created by putting a series of curve() functions
        together or using curve_vertex(). An additional function called
        curve_tightness() provides control for the visual quality of the curve.
        The curve() function is an implementation of Catmull-Rom splines.
        """
        self._p5js.curve(x1, y1, x2, y2, x3, y3, x4, y4, *args)

    def curve_detail(self, resolution: float):
        """Sets the resolution at which curves display.
        The default value is 20 while the minimum value is 3.

        This function is only useful when using the WEBGL renderer as the default
        canvas renderer does not use this information.
        """
        self._p5js.curveDetail(resolution)

    def curve_tightness(self, amount: float):
        """Modifies the quality of forms created with curve() and
        curve_vertex().
        The parameter tightness determines how the curve fits to the vertex
        points. The value 0.0 is the default value for tightness (this value
        defines the curves to be Catmull-Rom splines) and the value 1.0 connects
        all the points with straight lines. Values within the range -5.0 and 5.0
        will deform the curves but will leave them recognizable and as values
        increase in magnitude, they will continue to deform.
        """
        self._p5js.curveTightness(amount)

    def curve_point(self, a: float, b: float, c: float, d: float, t: float):
        """Evaluates the curve at position t for points a, b, c, d.
        The parameter t varies between 0 and 1, a and d are control points of the
        curve, and b and c are the start and end points of the curve. This can be
        done once with the x coordinates and a second time with the y coordinates
        to get the location of a curve at t.
        """
        self._p5js.curvePoint(a, b, c, d, t)

    def curve_tangent(self, a: float, b: float, c: float, d: float, t: float):
        """Evaluates the tangent to the curve at position t for points a, b, c, d.
        The parameter t varies between 0 and 1, a and d are points on the curve,
        and b and c are the control points.
        """
        self._p5js.curveTangent(a, b, c, d, t)

    # ======
    # Vertex
    # ======
    def begin_contour(self):
        """Use the begin_contour() and end_contour() functions to create negative
        shapes within shapes such as the center of the letter 'O'.
        begin_contour() begins recording vertices for the shape and end_contour()
        stops recording. The vertices that define a negative shape must "wind" in
        the opposite direction from the exterior shape. First draw vertices for
        the exterior clockwise order, then for internal shapes, draw vertices
        shape in counter-clockwise.

        These functions can only be used within a begin_shape()/end_shape() pair
        and transformations such as translate(), rotate(), and scale() do not
        work within a begin_contour()/end_contour() pair. It is also not possible
        to use other shapes, such as ellipse() or rect() within.
        """
        self._p5js.beginContour()

    def begin_shape(self, kind: str | None = None):
        """Using the begin_shape() and end_shape() functions allow creating more
        complex forms.
        begin_shape() begins recording vertices for a shape and end_shape() stops
        recording. The value of the kind parameter tells it which types of shapes
        to create from the provided vertices. With no mode specified, the shape
        can be any irregular polygon.

        The parameters available for begin_shape() are:

        POINTS Draw a series of points

        LINES Draw a series of unconnected line segments (individual lines)

        TRIANGLES Draw a series of separate triangles

        TRIANGLE_FAN Draw a series of connected triangles sharing the first vertex
        in a fan-like fashion

        TRIANGLE_STRIP Draw a series of connected triangles in strip fashion

        QUADS Draw a series of separate quads

        QUAD_STRIP Draw quad strip using adjacent edges to form the next quad

        TESS (WEBGL only) Handle irregular polygon for filling curve by explicit
        tessellation

        After calling the begin_shape() function, a series of vertex() commands
        must follow. To stop drawing the shape, call end_shape(). Each shape will
        be outlined with the current stroke color and filled with the fill color.

        Transformations such as translate(), rotate(), and scale() do not work
        within begin_shape(). It is also not possible to use other shapes, such as
        ellipse() or rect() within begin_shape().

        """
        self._p5js.beginShape(kind)

    def bezier_vertex(
        self, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, *args
    ):
        """Specifies vertex coordinates for Bezier curves.
        Each call to bezier_vertex() defines the position of two control points
        and one anchor point of a Bezier curve, adding a new segment to a line or
        shape. For WebGL mode bezier_vertex() can be used in 2D as well as 3D
        mode. 2D mode expects 6 parameters, while 3D mode expects 9 parameters
        (including z coordinates).

        The first time bezier_vertex() is used within a begin_shape() call, it
        must be prefaced with a call to vertex() to set the first anchor point.
        This function must be used between begin_shape() and end_shape() and only
        when there is no MODE or POINTS parameter specified to begin_shape().
        """
        self._p5js.bezierVertex(x2, y2, x3, y3, x4, y4, *args)

    def curve_vertex(self, x: float, y: float, z: float | None = None):
        """Specifies vertex coordinates for curves.
        This function may only be used between begin_shape() and end_shape() and
        only when there is no MODE parameter specified to begin_shape().
        For WebGL mode curve_vertex() can be used in 2D as well as 3D mode. 2D
        mode expects 2 parameters, while 3D mode expects 3 parameters.

        The first and last points in a series of curve_vertex() lines will be used
        to guide the beginning and end of the curve. A minimum of four points is
        required to draw a tiny curve between the second and third points. Adding
        a fifth point with curve_vertex() will draw the curve between the second,
        third, and fourth points. The curve_vertex() function is an implementation
        of Catmull-Rom splines.
        """
        self._p5js.curveVertex(x, y, z)

    def end_contour(self):
        """Use the begin_contour() and end_contour() functions to create negative
        shapes within shapes such as the center of the letter 'O'.
        begin_contour() begins recording vertices for the shape and end_contour()
        stops recording. The vertices that define a negative shape must "wind" in
        the opposite direction from the exterior shape. First draw vertices for
        the exterior clockwise order, then for internal shapes, draw vertices
        shape in counter-clockwise.

        These functions can only be used within a begin_shape()/end_shape() pair
        and transformations such as translate(), rotate(), and scale() do not work
        within a begin_contour()/end_contour() pair. It is also not possible to
        use other shapes, such as ellipse() or rect() within.
        """
        self._p5js.endContour()

    def end_shape(self, mode: str | None = None):
        """The end_shape() function is the companion to begin_shape() and may
        only be called after begin_shape().
        When end_shape() is called, all of the image data defined since the
        previous call to begin_shape() is written into the image buffer. The
        constant CLOSE as the value for the mode parameter to close the shape (to
        connect the beginning and the end).
        """
        self._p5js.endShape(mode)

    def quadratic_vertex(self, cx: float, cy: float, x3: float, y3: float, *args):
        """Specifies vertex coordinates for quadratic Bezier curves.
        Each call to quadratic_vertex() defines the position of one control points
        and one anchor point of a Bezier curve, adding a new segment to a line or
        shape. The first time quadratic_vertex() is used within a begin_shape()
        call, it must be prefaced with a call to vertex() to set the first anchor
        point. For WebGL mode quadratic_vertex() can be used in 2D as well as 3D
        mode. 2D mode expects 4 parameters, while 3D mode expects 6 parameters
        (including z coordinates).

        This function must be used between begin_shape() and end_shape() and only
        when there is no MODE or POINTS parameter specified to begin_shape().
        """
        self._p5js.quadraticVertex(cx, cy, x3, y3, *args)

    def vertex(
        self,
        x: float,
        y: float,
        z: float | None = None,
        u: float | None = None,
        v: float | None = None,
    ):
        """All shapes are constructed by connecting a series of vertices.
        vertex() is used to specify the vertex coordinates for points, lines,
        triangles, quads, and polygons. It is used exclusively within the
        begin_shape() and end_shape() functions.
        """
        self._p5js.vertex(x, y, z, u, v)

    def normal(self, x: float, y: float, z: float):
        """Sets the 3d vertex normal to use for subsequent vertices drawn with
        vertex().
        A normal is a vector that is generally nearly perpendicular to a shape's
        surface which controls how much light will be reflected from that part of
        the surface.
        """
        self._p5js.normal(x, y, z)

    # =============
    # 3D Primitives
    # =============
    def plane(
        self,
        width: float | None = None,
        height: float | None = None,
        detail_x: int | None = None,
        detail_y: int | None = None,
    ):
        """Draw a plane with given a width and height."""
        self._p5js.plane(width, height, detail_x, detail_y)

    def box(
        self,
        width: float | None = None,
        height: float | None = None,
        depth: float | None = None,
        detail_x: int | None = None,
        detail_y: int | None = None,
    ):
        """Draw a box with given width, height and depth."""
        self._p5js.box(width, height, depth, detail_x, detail_y)

    def sphere(
        self,
        radius: float | None = None,
        detail_x: int | None = None,
        detail_y: int | None = None,
    ):
        """Draw a sphere with given radius.

        detail_x and detail_y determine the number of subdivisions in the
        x-dimension and the y-dimension of a sphere. More subdivisions make the
        sphere seem smoother. The recommended maximum values are both 24. Using a
        value greater than 24 may cause a warning or slow down the browser.
        """
        self._p5js.sphere(radius, detail_x, detail_y)

    def cylinder(
        self,
        radius: float | None = None,
        height: float | None = None,
        detail_x: int | None = None,
        detail_y: int | None = None,
        bottom_cap: bool | None = None,
        top_cap: bool | None = None,
    ):
        """Draw a cylinder with given radius and height.

        detail_x and detail_y determines the number of subdivisions in the
        x-dimension and the y-dimension of a cylinder. More subdivisions make the
        cylinder seem smoother. The recommended maximum value for detailX is 24.
        Using a value greater than 24 may cause a warning or slow down the
        browser.
        """
        self._p5js.cylinder(radius, height, detail_x, detail_y, bottom_cap, top_cap)

    def cone(
        self,
        radius: float | None = None,
        height: float | None = None,
        detail_x: float | None = None,
        detail_y: float | None = None,
        cap: bool | None = None,
    ):
        """Draw a cone with given radius and height

        detail_x and detail_y determine the number of subdivisions in the
        x-dimension and the y-dimension of a cone. More subdivisions make the
        cone seem smoother. The recommended maximum value for detailX is 24.
        Using a value greater than 24 may cause a warning or slow down the
        browser.
        """
        self._p5js.cone(radius, height, detail_x, detail_y, cap)

    def ellipsoid(
        self,
        radius_x: float | None = None,
        radius_y: float | None = None,
        radius_z: float | None = None,
        detail_x: int | None = None,
        detail_y: int | None = None,
    ):
        """Draw an ellipsoid with given radius.

        detail_x and detail_y determine the number of subdivisions in the
        x-dimension and the y-dimension of a cone. More subdivisions make the
        ellipsoid appear to be smoother. Avoid detail number above 150, it may
        crash the browser.
        """
        self._p5js.ellipsoid(radius_x, radius_y, radius_z, detail_x, detail_y)

    def torus(
        self,
        radius: float | None = None,
        tube_radius: float | None = None,
        detail_x: int | None = None,
        detail_y: int | None = None,
    ):
        """Draw a torus with given radius and tube radius.

        detail_x and detail_y determine the number of subdivisions in the
        x-dimension and the y-dimension of a torus. More subdivisions make the
        torus appear to be smoother. The default and maximum values for detail_x
        and detail_y are 24 and 16, respectively. Setting them to relatively small
        values like 4 and 6 allows you to create new shapes other than a torus.
        """
        self._p5js.torus(radius, tube_radius, detail_x, detail_y)

    # =========
    # 3D Models
    # =========
    def load_model(self, path: str) -> object:
        """Load a 3d model from an OBJ or STL file.

        load_model() should be placed inside of preload(). This allows the model to
        load fully before the rest of your code is run.

        One of the limitations of the OBJ and STL format is that it doesn't have a
        built-in sense of scale. This means that models exported from different
        programs might be very different sizes. If your model isn't displaying,
        try calling load_model() with the normalized parameter set to true. This
        will resize the model to a scale appropriate for p5. You can also make
        additional changes to the final size of your model with the scale()
        function.

        Also, the support for colored STL files is not present. STL files with
        color will be rendered without color properties.
        """
        return self._p5js.loadModel(path)

    def model(self, model: object):
        """Render a 3d model to the screen."""
        self._p5js.model(model)
