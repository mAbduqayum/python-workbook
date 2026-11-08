import pytest

try:
    from wrap import wrap
except ImportError:
    wrap = None

pytestmark = pytest.mark.skipif(wrap is None, reason="wrap function not implemented")


@pytest.mark.parametrize(
    "value, low, high, expected",
    [
        (13, 1, 12, 1),
        (0, 1, 12, 12),
        (25, 1, 12, 1),
        (24, 1, 12, 12),
        (7, 1, 12, 7),
        (1, 1, 12, 1),
        (12, 1, 12, 12),
        (-11, 1, 12, 1),
        (10, 0, 6, 3),
        (-1, 0, 6, 6),
        (-8, 0, 6, 6),
        (360, 0, 359, 0),
        (-90, 0, 359, 270),
    ],
)
def test_wrap(value, low, high, expected):
    assert wrap(value, low, high) == expected
