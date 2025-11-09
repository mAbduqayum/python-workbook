import pytest

try:
    from sieve_of_eratosthenes import sieve_of_eratosthenes
except ImportError:
    sieve_of_eratosthenes = None


@pytest.mark.skipif(sieve_of_eratosthenes is None, reason="sieve_of_eratosthenes function not implemented")
@pytest.mark.parametrize(
    "n, expected",
    [
        (20, [2, 3, 5, 7, 11, 13, 17, 19]),
        (10, [2, 3, 5, 7]),
        (2, [2]),
        (1, []),
        (30, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]),
        (0, []),
    ],
)
def test_sieve_of_eratosthenes(n, expected):
    assert sieve_of_eratosthenes(n) == expected
