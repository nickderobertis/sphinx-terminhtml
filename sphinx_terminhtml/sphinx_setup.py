from sphinx.application import Sphinx

from sphinx_terminhtml.assets import register_assets
from sphinx_terminhtml.directives.terminal import TerminHTMLDirective
from sphinx_terminhtml.get_version import get_sphinx_terminhtml_version

version = get_sphinx_terminhtml_version()


def setup(app: Sphinx):
    register_assets(app)
    app.add_config_value("terminhtml_cache", True, "html")
    app.add_config_value("terminhtml_echo", False, "html")
    app.add_config_value("terminhtml_force_color", True, "html")
    app.add_directive("terminhtml", TerminHTMLDirective)
    return {
        "version": version,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
