from typing import Callable
from pyodide.ffi import create_proxy, to_js

from ._binding import BaseSketch


class DOM(BaseSketch):
    def select(self, selectors: str, container: str | None = None) -> object:
        """Searches the page for the first element that matches the given CSS
        selector string (can be an ID, class, tag name or a combination) and
        returns it as a p5.Element.
        The DOM node itself can be accessed with .elt. Returns null if none found.
        You can also specify a container to search within.
        """
        return self._p5js.select(selectors, container)

    def select_all(self, selectors: str, container: str | None = None) -> list[object]:
        """Searches the page for elements that match the given CSS selector
        string (can be an ID a class, tag name or a combination) and returns them
        as p5.Elements in an array.
        The DOM node itself can be accessed with .elt. Returns an empty array if
        none found. You can also specify a container to search within.
        """
        return self._p5js.selectAll(selectors, container)

    def remove_elements(self):
        """Removes all elements created by p5, except any canvas / graphics
        elements created by create_canvas or create_graphics.
        Event handlers are removed, and element is removed from the DOM.
        """
        self._p5js.removeElements()

    def create_div(self, html: str | None = None) -> object:
        """Creates a <div></div> element in the DOM with given inner HTML."""
        return self._p5js.createDiv(html)

    def create_p(self, html: str | None = None) -> object:
        """Creates a <p></p> element in the DOM with given inner HTML.
        Used for paragraph length text.
        """
        return self._p5js.createP(html)

    def create_span(self, html: str | None = None) -> object:
        """Creates a <span></span> element in the DOM with given inner HTML."""
        return self._p5js.createSpan(html)

    def create_img(self, src: str, alt: str, cross_origin: str | None = None) -> object:
        """Creates an <img> element in the DOM with given src and alternate text."""
        return self._p5js.createImg(src, alt, cross_origin)

    def create_a(self, html: str | None = None) -> object:
        """Creates an <a></a> element in the DOM for including a hyperlink."""
        return self._p5js.createA(html)

    def create_slider(
        self,
        min: float,
        max: float,
        value: float | None = None,
        step: float | None = None,
    ) -> object:
        """Creates a slider <input></input> element in the DOM.
        Use .size() to set the display length of the slider.
        """
        return self._p5js.createSlider(min, max, value, step)

    def create_button(self, label: str, value: str | None = None) -> object:
        """Creates a <button></button> element in the DOM.
        Use .size() to set the display size of the button. Use .mousePressed() to
        specify behavior on press.
        """
        return self._p5js.createButton(label, value)

    def create_checkbox(
        self, label: str | None = None, value: str | None = None
    ) -> object:
        """Creates a checkbox <input></input> element in the DOM.
        Calling .checked() on a checkbox returns a boolean indicating whether it
        is checked or not.
        """
        return self._p5js.createCheckbox(label, value)

    def create_select(self, multiple: bool | None = None) -> object:
        """Creates a dropdown menu <select></select> element in the DOM.
        It also assigns select-related methods to p5.Element when selecting an
        existing select box. Options in the menu are unique by name (the display
        text).

        .option(name, [value]) can be used to add an option with name (the display
        text) and value to the select element. If an option with name already
        exists within the select element, this method will change its value to
        value.

        .value() will return the currently selected option.

        .selected() will return the current dropdown element which is an instance
        of p5.Element.

        .selected(value) can be used to make given option selected by default
        when the page first loads.

        .disable() marks the whole dropdown element as disabled.

        .disable(value) marks a given option as disabled.
        """
        return self._p5js.createSelect(multiple)

    def create_radio(self) -> object:
        """Creates a radio button element in the DOM.
        It also helps existing radio buttons assign methods of p5.Element.

        .option(value, [label]) can be used to create a new option for the
        element. If an option with a value already exists, it will be returned. It
        is recommended to use string values as input for value. Optionally, a
        label can be provided as second argument for the option.

        .remove(value) can be used to remove an option for the element. String
        values recommended as input for value.

        .value() method will return the currently selected value.

        .selected() method will return the currently selected input element.

        .selected(value) method will select the option and return it. String
        values recommended as input for value.

        .disable(Boolean) method will enable/disable the whole radio button element.
        """
        return self._p5js.createRadio()

    def create_color_picker(self, color: str = None) -> object:
        """Creates a color picker element in the DOM for color input.
        The .value() method will return a hex string (#rrggbb) of the color.
        The .color() method will return a p5.Color object with the current chosen
        color.
        """
        return self._p5js.createColorPicker(color)

    def create_input(self, value: str | None = None, type: str | None = None) -> object:
        """Creates an <input></input> element in the DOM for text input.
        Use .size() to set the display length of the box.
        """
        return self._p5js.createInput(value, type)

    def create_file_input(
        self, callback: Callable, multiple: bool | None = None
    ) -> object:
        """Creates an <input></input> element in the DOM of type 'file'.
        This allows users to select local files for use in a sketch.
        """
        return self._p5js.createFileInput(create_proxy(callback), multiple)

    def create_video(self, src: str, callback: Callable | None = None) -> object:
        """Creates an HTML5 <video> element in the DOM for simple playback of
        audio/video.
        Shown by default, can be hidden with .hide() and drawn into canvas using
        image(). The first parameter can be either a single string path to a video
        file, or an array of string paths to different formats of the same video.
        This is useful for ensuring that your video can play across different
        browsers, as each supports different formats. See this page for further
        information about supported formats.
        """
        if callback:
            return self._p5js.createVideo(src, create_proxy(callback))
        return self._p5js.createCanvas(src)

    def create_audio(
        self, src: str | list[str], callback: Callable | None = None
    ) -> object:
        """Creates a hidden HTML5 <audio> element in the DOM for simple audio
        playback.
        The first parameter can be either a single string path to a audio file,
        or an array of string paths to different formats of the same audio. This
        is useful for ensuring that your audio can play across different browsers,
        as each supports different formats. See this page for further information
        about supported formats.
        """
        if callback:
            return self._p5js.createAudio(to_js(src), create_proxy(callback))
        return self._p5js.createAudio(to_js(src))

    def create_capture(self, type: str, callback: Callable | None = None) -> object:
        """Creates a new HTML5 <video> element that contains the audio/video feed from a webcam. The element is separate from the canvas and is displayed by default. The element can be hidden using .hide(). The feed can be drawn onto the canvas using image(). The loadedmetadata property can be used to detect when the element has fully loaded (see second example).

        More specific properties of the feed can be passing in a Constraints object. See the W3C spec for possible properties. Note that not all of these are supported by all browsers.

        Security note: A new browser security specification requires that getUserMedia, which is behind createCapture(), only works when you're running the code locally, or on HTTPS. Learn more here and here.
        """
        if callback:
            return self._p5js.createCapture(type, create_proxy(callback))
        return self._p5js.createCapture(type)

    def create_element(self, tag: str, content: str | None = None) -> object:
        """Creates element with given tag in the DOM with given content."""
        return self._p5js.createElement(tag, content)
