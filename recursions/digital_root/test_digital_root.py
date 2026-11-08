import pytest

try:
    from digital_root import digital_root
except ImportError:
    digital_root = None

pytestmark = pytest.mark.skipif(
    digital_root is None, reason="digital_root not implemented"
)


@pytest.mark.parametrize(
    "n, expected",
    [
        (7, 7),
        (10, 1),
        (38, 2),
        (99, 9),
        (9875, 2),
        (123456789, 9),
        (999999999999, 9),
    ],
)
def test_digital_root(n, expected):
    assert digital_root(n) == expected
