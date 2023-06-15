import js


def remove_sketch(id: str):
    """Removes an existing sketch from the DOM."""
    try:
        old_sketch = getattr(js.window, id)
        old_sketch.remove()
    except AttributeError:
        pass
