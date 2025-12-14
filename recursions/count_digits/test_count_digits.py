import pytest

try:
    from count_digits import count_digits
except ImportError:
    count_digits = None


@pytest.mark.skipif(count_digits is None, reason="count_digits not implemented")
@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 1),
        (5, 1),
        (9, 1),
        (10, 2),
        (99, 2),
        (100, 3),
        (123, 3),
        (1000, 4),
        (12345, 5),
        (1000000, 7),
        (-123, 3),
    ],
)
def test_count_digits(n, expected):
    assert count_digits(n) == expected
