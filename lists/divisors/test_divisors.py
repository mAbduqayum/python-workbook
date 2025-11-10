import pytest

try:
    from divisors import divisors
except ImportError:
    list_divisors = None


@pytest.mark.skipif(divisors is None, reason="list_divisors function not implemented")
@pytest.mark.parametrize(
    "n, expected",
    [
        (1, [1]),
        (6, [1, 2, 3, 6]),
        (7, [1, 7]),
        (12, [1, 2, 3, 4, 6, 12]),
        (20, [1, 2, 4, 5, 10, 20]),
        (28, [1, 2, 4, 7, 14, 28]),
    ],
)
def test_list_divisors(n, expected):
    assert divisors(n) == expected
