import pytest

try:
    from sum_to_n import sum_to_n
except ImportError:
    sum_to_n = None


@pytest.mark.skipif(sum_to_n is None, reason="sum_to_n not implemented")
@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 1),
        (2, 3),
        (3, 6),
        (4, 10),
        (5, 15),
        (10, 55),
        (100, 5050),
    ],
)
def test_sum_to_n(n, expected):
    assert sum_to_n(n) == expected
