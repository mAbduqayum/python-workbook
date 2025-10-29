import pytest

try:
    from quadratic_roots import quadratic_roots
except ImportError:
    quadratic_roots = None


@pytest.mark.skipif(
    quadratic_roots is None, reason="quadratic_roots function not implemented"
)
@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (1, 0, 1, None),
        (1, -2, 1, (1.0, 1.0)),
        (1, 0, -4, (2.0, -2.0)),
        (1, -3, 2, (2.0, 1.0)),
        (1, 5, 6, (-2.0, -3.0)),
        (2, 4, 2, (-1.0, -1.0)),
    ],
)
def test_quadratic_roots(a, b, c, expected):
    result = quadratic_roots(a, b, c)
    if expected is None:
        assert result is None
    else:
        assert result is not None
        assert abs(result[0] - expected[0]) < 1e-9
        assert abs(result[1] - expected[1]) < 1e-9
