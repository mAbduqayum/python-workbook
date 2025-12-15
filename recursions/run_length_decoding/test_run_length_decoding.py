import pytest

try:
    from run_length_decoding import run_length_decode
except ImportError:
    run_length_decode = None


@pytest.mark.skipif(
    run_length_decode is None, reason="run_length_decode not implemented"
)
@pytest.mark.parametrize(
    "encoded, expected",
    [
        ("", ""),
        ("1A", "A"),
        ("3A", "AAA"),
        ("3A2B1C", "AAABBC"),
        ("1H1e1l1l1o", "Hello"),
        ("5X", "XXXXX"),
        ("2A3B4C", "AABBBCCCC"),
        ("12A3B", "AAAAAAAAAAAABBB"),
    ],
)
def test_run_length_decode(encoded, expected):
    assert run_length_decode(encoded) == expected
