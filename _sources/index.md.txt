% sphinx-terminhtml documentation master file, created by
%   copier-pypi-sphinx-flexlate.
%   You can adapt this file completely to your liking, but it should at least
%   contain the root `toctree` directive.

# Welcome to Sphinx TerminHTML documentation!

```{terminhtml-docs}
---
prompt-matchers: "['\\[0m: ']"
input: "Nick DeRobertis"
cwd: ..
---
python -m terminhtml.demo_output
```

```{include} ../../README.md
```

```{terminhtml-docs}
python -m rich
```

For more information on getting started, take a look at the tutorial and examples.

## Tutorial and Examples

```{toctree}
tutorial
tests/index
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
