import pytest

try:
    from clamp import clamp
except ImportError:
    clamp = None

pytestmark = pytest.mark.skipif(clamp is None, reason="clamp function not implemented")


@pytest.mark.parametrize(
    "value, low, high, expected",
    [
        (13, 1, 12, 12),
        (0, 1, 12, 1),
        (7, 1, 12, 7),
        (1, 1, 12, 1),
        (12, 1, 12, 12),
        (100, 1, 12, 12),
        (-5, -3, 3, -3),
        (5, -3, 3, 3),
        (0, -3, 3, 0),
    ],
)
def test_clamp(value, low, high, expected):
    assert clamp(value, low, high) == expected
