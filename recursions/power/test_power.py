import pytest

try:
    from power import power
except ImportError:
    power = None


@pytest.mark.skipif(power is None, reason="power not implemented")
@pytest.mark.parametrize(
    "base, exp, expected",
    [
        (2, 0, 1),
        (2, 1, 2),
        (2, 3, 8),
        (2, 10, 1024),
        (3, 0, 1),
        (3, 2, 9),
        (3, 4, 81),
        (5, 3, 125),
        (10, 3, 1000),
        (1, 100, 1),
        (0, 5, 0),
    ],
)
def test_power(base, exp, expected):
    assert power(base, exp) == expected
