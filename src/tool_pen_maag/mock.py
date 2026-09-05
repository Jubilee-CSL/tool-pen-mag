from dataclasses import dataclass
from typing import ClassVar

from tool_pen_maag.tool import PenMaag


@dataclass(slots=True, repr=False)
class PenMaagMock(PenMaag):
    TOOL_KEY: ClassVar[str] = "tool_pen_maag"

    def run(self, nav) -> None:
        pass
