import pytest

try:
    from average import average
except ImportError:
    average = None


@pytest.mark.skipif(average is None, reason="average function not implemented")
@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([1, 2, 3, 4, 5], 3.0),
        ([10, 20, 30], 20.0),
        ([5], 5.0),
        ([0, 0, 0], 0.0),
        ([-5, 5], 0.0),
        ([100, 200], 150.0),
    ],
)
def test_average(numbers, expected):
    assert average(numbers) == pytest.approx(expected)
