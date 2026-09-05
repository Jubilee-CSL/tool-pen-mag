from science_jubilee.tools.Tool import Tool
from tool_pen_maag.tool import PenMaag
from tool_pen_maag.mock import PenMaagMock


def test_tool_key():
    assert PenMaag.TOOL_KEY == "tool_pen_maag"


def test_is_tool_subclass():
    assert issubclass(PenMaag, Tool)


def test_mock_key_matches():
    assert PenMaagMock.TOOL_KEY == PenMaag.TOOL_KEY
