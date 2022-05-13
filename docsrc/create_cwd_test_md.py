from pathlib import Path

from jinja2 import Environment, Template

jinja_template_str = """
# CWD Tests

```{terminhtml}
---
cwd: .
disable-cache:
---
echo 'cwd .'
ls -l
```

```{terminhtml}
---
cwd: .
cwd-relative-to: cwd
---
echo 'cwd ., cwd-relative-to: cwd'
ls -l
```

```{terminhtml}
---
cwd: .
cwd-relative-to: current_source
---
echo 'cwd ., cwd-relative-to: current_source'
ls -l
```

```{terminhtml}
---
cwd: .
cwd-relative-to: sources_root
---
echo 'cwd ., cwd-relative-to: sources_root'
ls -l
```

```{terminhtml}
---
cwd: {{ absolute_cwd }}
cwd-relative-to: sources_root
---
echo 'cwd absolute, cwd-relative-to: sources_root'
ls -l
```
"""

template = Template(jinja_template_str)

DIRECTIVES_PATH = Path(__file__).parent / "directives"
SOURCE_PATH = Path(__file__).parent / "source"
CWD_MD_TESTS_PATH = SOURCE_PATH / "tests" / "cwd.md"

def create_cwd_test_md() -> str:
    """Create the CWD tests Markdown file."""
    # Use Jinja2 to create the Markdown file by loading the template from string
    # and replacing the variables.

    return template.render(absolute_cwd=str(DIRECTIVES_PATH.resolve()))

def main():
    md_str = create_cwd_test_md()
    CWD_MD_TESTS_PATH.write_text(md_str)

if __name__ == '__main__':
    main()