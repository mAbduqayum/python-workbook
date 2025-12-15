import pytest

try:
    from coin_sum import coin_sum
except ImportError:
    coin_sum = None


@pytest.mark.skipif(coin_sum is None, reason="coin_sum not implemented")
@pytest.mark.parametrize(
    "amount, coins, expected",
    [
        (0, [1, 2], 1),
        (1, [1], 1),
        (2, [1], 1),
        (2, [1, 2], 2),
        (3, [2], 0),
        (5, [1, 2, 5], 4),
        (10, [1, 5, 10], 4),
        (10, [2, 5, 3, 6], 5),
        (4, [1, 2, 3], 4),
    ],
)
def test_coin_sum(amount, coins, expected):
    assert coin_sum(amount, coins) == expected
