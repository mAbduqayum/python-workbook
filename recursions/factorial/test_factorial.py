import pytest

try:
    from factorial import factorial
except ImportError:
    factorial = None


@pytest.mark.skipif(factorial is None, reason="factorial not implemented")
@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24),
        (5, 120),
        (6, 720),
        (7, 5040),
        (10, 3628800),
    ],
)
def test_factorial(n, expected):
    assert factorial(n) == expected
