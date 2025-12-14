import pytest

try:
    from sum_digits import sum_digits
except ImportError:
    sum_digits = None


@pytest.mark.skipif(sum_digits is None, reason="sum_digits not implemented")
@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 0),
        (5, 5),
        (10, 1),
        (123, 6),
        (999, 27),
        (9999, 36),
        (12345, 15),
        (100, 1),
        (-456, 15),
    ],
)
def test_sum_digits(n, expected):
    assert sum_digits(n) == expected
