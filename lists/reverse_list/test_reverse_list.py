import pytest

try:
    from reverse_list import reverse_list
except ImportError:
    reverse_list = None


@pytest.mark.skipif(reverse_list is None, reason="reverse_list function not implemented")
@pytest.mark.parametrize(
    "string, expected",
    [
        ("1 2 3 4 5", [5, 4, 3, 2, 1]),
        ("10", [10]),
        ("-5 0 5", [5, 0, -5]),
        ("100 200 300", [300, 200, 100]),
        ("", []),
        ("1 2", [2, 1]),
    ],
)
def test_reverse_list(string, expected):
    assert reverse_list(string) == expected
