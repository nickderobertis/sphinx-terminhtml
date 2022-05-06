% sphinx-terminhtml documentation master file, created by
%   copier-pypi-sphinx-flexlate.
%   You can adapt this file completely to your liking, but it should at least
%   contain the root `toctree` directive.

# Welcome to Sphinx TerminHTML documentation!

```{include} ../../README.md
```

```{terminhtml}
python -m rich
```

For more information on getting started, take a look at the tutorial and examples.

## Tutorial and Examples

```{toctree}

tutorial
auto_examples/index
```

## API Documentation

```{eval-rst}
.. toctree:: api/modules
   :maxdepth: 3
```

## Indices

- {ref}`genindex`
- {ref}`modindex`
- {ref}`search`