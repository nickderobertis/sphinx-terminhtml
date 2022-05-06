import ast
from typing import List, Sequence, Optional, Type


from docutils.nodes import Node
from docutils.parsers.rst import directives
from docutils.statemachine import StringList
from sphinx.util.docutils import SphinxDirective
from docutils import nodes
from terminhtml.main import TerminHTML

from sphinx_terminhtml.cache import TerminalCache
from sphinx_terminhtml.options import RunTerminalOptions


def html(content: str) -> nodes.raw:
    return nodes.raw(text=content, format="html")


def _get_list(input: str) -> List[str]:
    if not input.startswith("["):
        if input:
            return [input]
        return []
    return ast.literal_eval(input)


cache = TerminalCache()


class TerminHTMLDirective(SphinxDirective):
    required_arguments = 0
    option_spec = {
        "setup": directives.unchanged,
        "input": _get_list,
        "prompt-matchers": _get_list,
        "allow-exceptions": directives.flag,
    }
    has_content = True
    always_setup_commands: List[str] = []
    always_prompt_matchers: List[str] = []

    def run(self) -> List[Node]:
        text = self._run_commands_in_temp_dir_generate_output_html()
        return [html(text)]

    def _run_commands_in_temp_dir_generate_output_html(self) -> str:
        self.options: RunTerminalOptions

        setup_command: str = self.options.get("setup", "")
        if setup_command:
            use_setup_commands = self.always_setup_commands + [setup_command]
        else:
            use_setup_commands = self.always_setup_commands

        prompt_matchers: List[str] = self.options.get("prompt-matchers", [])
        if prompt_matchers:
            use_prompt_matchers = self.always_prompt_matchers + prompt_matchers
        else:
            use_prompt_matchers = self.always_prompt_matchers

        input: List[str] = self.options.get("input", [])
        allow_exceptions: bool = "allow-exceptions" in self.options
        terminhtml = TerminHTML.from_commands(
            list(self.content),
            use_setup_commands,
            input=input,
            allow_exceptions=allow_exceptions,
            prompt_matchers=use_prompt_matchers,
        )
        return terminhtml.to_html(full=False)

    def _load_cache_or_run_commands_in_temp_dir_get_output_list(self) -> List[str]:
        self.content: StringList
        cached_result = cache.get(list(self.content), self.options)
        if cached_result:
            return cached_result.content

        result = self._run_commands_in_temp_dir_generate_output_list()
        cache.set(list(self.content), self.options, result)
        return result


def create_terminhtml_directive_with_setup(
    setup_commands: Optional[Sequence[str]] = None,
    prompt_matchers: Optional[Sequence[str]] = None,
) -> Type[SphinxDirective]:
    use_setup_commands = list(setup_commands or [])
    use_prompt_matchers = list(prompt_matchers or [])

    class RunTerminalDirectiveWithSetup(TerminHTMLDirective):
        always_setup_commands = use_setup_commands
        always_prompt_matchers = use_prompt_matchers

    return RunTerminalDirectiveWithSetup
