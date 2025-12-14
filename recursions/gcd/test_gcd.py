import pytest

try:
    from gcd import gcd
except ImportError:
    gcd = None


@pytest.mark.skipif(gcd is None, reason="gcd not implemented")
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (48, 18, 6),
        (18, 48, 6),
        (100, 25, 25),
        (17, 13, 1),
        (54, 24, 6),
        (7, 7, 7),
        (12, 8, 4),
        (21, 14, 7),
        (36, 60, 12),
        (5, 0, 5),
        (0, 5, 5),
    ],
)
def test_gcd(a, b, expected):
    assert gcd(a, b) == expected
