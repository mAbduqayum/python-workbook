import pytest

try:
    from fibonacci import fibonacci
except ImportError:
    fibonacci = None


@pytest.mark.skipif(fibonacci is None, reason="fibonacci not implemented")
@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (8, 21),
        (10, 55),
        (15, 610),
    ],
)
def test_fibonacci(n, expected):
    assert fibonacci(n) == expected
