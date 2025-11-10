import pytest

try:
    from str_to_ints import str_to_ints
except ImportError:
    str_to_ints = None


@pytest.mark.skipif(str_to_ints is None, reason="str_to_ints function not implemented")
@pytest.mark.parametrize(
    "string, expected",
    [
        ("", []),
        ("1", [1]),
        ("10", [10]),
        ("-5 0 5", [-5, 0, 5]),
        ("-10 -20 -30", [-10, -20, -30]),
        ("100 200 300", [100, 200, 300]),
        ("1 2 3 4 5", [1, 2, 3, 4, 5]),
    ],
)
def test_str_to_ints(string, expected):
    assert str_to_ints(string) == expected
