def _init_global_mode():
    """Initialize p5.js in global mode."""
    from pyodide.code import run_js

    run_js("new p5();")


_init_global_mode()
