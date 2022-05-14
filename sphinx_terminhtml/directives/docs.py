from enum import Enum
from typing import List, Optional

from docutils.nodes import Node, literal_block

from sphinx_terminhtml.directives.terminal import TerminHTMLDirective


class SourceType(str, Enum):
    MD = "markdown"
    RST = "reStructuredText"


def docs_node(docs_content: str) -> Node:
    """
    Creates a literal block node containing the documentation.
    """
    return literal_block(docs_content, docs_content)


class TerminHTMLDocsDirective(TerminHTMLDirective):
    source_type: Optional[SourceType] = None

    def run(self) -> List[Node]:
        terminhtml_nodes = super().run()
        return [docs_node(self._get_source()), *terminhtml_nodes]

    def _get_source(self) -> str:
        raw_source = self._get_raw_source()

        # Replace terminhtml-docs directive with terminhtml directive
        if self.source_type == SourceType.MD:
            source = raw_source.replace("```{terminhtml-docs}", "```{terminhtml}")
        elif self.source_type == SourceType.RST:
            source = raw_source.replace(".. terminhtml-docs", ".. terminhtml")
        else:
            raise NotImplementedError(
                f"Source type {self.source_type} not implemented."
            )
        return source

    def _get_raw_source(self) -> str:
        file_path_str, line_no = self.get_source_info()
        save_lines = False
        lines: List[str] = []
        with open(file_path_str, "r") as f:
            for i, line in enumerate(f):
                if i == line_no - 1:
                    save_lines = True
                    if line.startswith(".."):
                        self.source_type = SourceType.RST
                    elif line.startswith("```"):
                        self.source_type = SourceType.MD
                    else:
                        raise ValueError(
                            f"Unrecognized source type for directive starting with {line}"
                        )
                if not save_lines:
                    continue

                if self.source_type is None:
                    raise ValueError("should not happen, for type narrowing")
                # Determine when to stop saving lines based on the source type
                if self.source_type == SourceType.RST:
                    if line.strip() == "":
                        # Blank line ends RST source
                        break
                elif self.source_type == SourceType.MD:
                    if line.strip() == "```":
                        # Unlike RST, need to add this line before exiting
                        lines.append(line)
                        break
                lines.append(line)
        return "".join(lines)
