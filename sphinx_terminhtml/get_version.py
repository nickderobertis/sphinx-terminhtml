import pkg_resources


def get_sphinx_terminhtml_version() -> str:
    return pkg_resources.get_distribution("sphinx-terminhtml").version
