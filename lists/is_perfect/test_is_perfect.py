import pytest

try:
    from is_perfect import is_perfect
except ImportError:
    is_perfect = None


@pytest.mark.skipif(is_perfect is None, reason="is_perfect function not implemented")
@pytest.mark.parametrize(
    "n, expected",
    [
        (6, True),
        (28, True),
        (12, False),
        (1, False),
        (496, True),
        (100, False),
        (8128, True),
    ],
)
def test_is_perfect(n, expected):
    assert is_perfect(n) == expected
