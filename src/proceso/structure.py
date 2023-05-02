from ._binding import BaseSketch


class Structure(BaseSketch):
    def remove(self):
        """Removes the entire p5 sketch.
        This will remove the canvas and any elements created by p5.js. It will
        also stop the draw loop and unbind any properties or methods from the
        window global scope. It will leave a variable p5 in case you wanted to
        create a new p5 sketch. If you like, you can set p5 = null to erase it.
        While all functions and variables and objects created by the p5 library
        will be removed, any other global variables created by your code will
        remain.
        """
        self._p5js.remove()

    def no_loop(self):
        """Stops p5.js from continuously executing the code within draw().
        If loop() is called, the code in draw() begins to run continuously again.
        If using no_loop() in setup(), it should be the last line inside the
        block.

        When noLoop() is used, it's not possible to manipulate or access the screen
        inside event handling functions such as mouse_pressed() or key_pressed().
        Instead, use those functions to call redraw() or loop(), which will run
        draw(), which can update the screen properly. This means that when
        no_loop() has been called, no drawing can happen, and functions like
        save_frames() or load_pixels() may not be used.

        Note that if the sketch is resized, redraw() will be called to update the
        sketch, even after no_loop() has been specified. Otherwise, the sketch
        would enter an odd state until loop() was called.

        Use is_looping() to check the current state of loop().
        """
        self._p5js.noLoop()

    def loop(self):
        """By default, p5 loops through draw() continuously, executing the code
        within it.
        However, the draw() loop may be stopped by calling no_loop(). In that
        case, the draw() loop can be resumed with loop().

        Avoid calling loop() from inside setup().

        Use is_looping() to check the current state of loop().
        """
        self._p5js.loop()

    def is_looping(self) -> bool:
        """By default, p5 loops through draw() continuously, executing the code
        within it.
        If the sketch is stopped with no_loop() or resumed with loop(),
        is_looping() returns the current state for use within custom event handlers.
        """
        return self._p5js.isLooping()

    def push(self):
        """The push() function saves the current drawing style settings and
        transformations, while pop() restores these settings.
        Note that these functions are always used together. They allow you to
        change the style and transformation settings and later return to what you
        had. When a new state is started with push(), it builds on the current
        style and transform information. The push() and pop() functions can be
        embedded to provide more control. (See the second example for a
        demonstration.)

        push() stores information related to the current transformation state and
        style settings controlled by the following functions: fill(), no_fill(),
        no_stroke(), stroke(), tint(), no_tint(), stroke_weight(), stroke_cap(),
        stroke_join(), image_mode(), rect_mode(), ellipse_mode(), color_mode(),
        text_align(), text_font(), text_size(), text_leading(), apply_matrix(),
        reset_matrix(), rotate(), scale(), shear_x(), shear_y(), translate(),
        noise_seed().

        In WEBGL mode additional style settings are stored. These are controlled
        by the following functions: set_camera(), ambient_light(),
        directional_light(), point_light(), texture(), specular_material(),
        shininess(), normal_material() and shader().
        """
        self._p5js.push()

    def pop(self):
        """The push() function saves the current drawing style settings and
        transformations, while pop() restores these settings.
        Note that these functions are always used together. They allow you to
        change the style and transformation settings and later return to what you
        had. When a new state is started with push(), it builds on the current
        style and transform information. The push() and pop() functions can be
        embedded to provide more control. (See the second example for a
        demonstration.)

        push() stores information related to the current transformation state and
        style settings controlled by the following functions: fill(), no_fill(),
        no_stroke(), stroke(), tint(), no_tint(), stroke_weight(), stroke_cap(),
        stroke_join(), image_mode(), rect_mode(), ellipse_mode(), color_mode(),
        text_align(), text_font(), text_size(), text_leading(), apply_matrix(),
        reset_matrix(), rotate(), scale(), shear_x(), shear_y(), translate(),
        noise_seed().

        In WEBGL mode additional style settings are stored. These are controlled
        by the following functions: set_camera(), ambient_light(),
        directional_light(), point_light(), texture(), specular_material(),
        shininess(), normal_material() and shader().
        """
        self._p5js.pop()

    def redraw(self, n: int | None = None):
        """Executes the code within draw() one time.
        This function allows the program to update the display window only when
        necessary, for example when an event registered by mouse_pressed()
        or key_pressed() occurs.

        In structuring a program, it only makes sense to call redraw() within
        events such as mouse_pressed(). This is because redraw() does not run
        draw() immediately (it only sets a flag that indicates an update is
        needed).

        The redraw() function does not work properly when called inside draw().
        To enable/disable animations, use loop() and no_loop().

        In addition you can set the number of redraws per method call. Just add an
        integer as single parameter for the number of redraws.
        """
        self._p5js.redraw(n)
