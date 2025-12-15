import pytest

try:
    from run_length_encoding import run_length_encode
except ImportError:
    run_length_encode = None


@pytest.mark.skipif(
    run_length_encode is None, reason="run_length_encode not implemented"
)
@pytest.mark.parametrize(
    "text, expected",
    [
        ("", ""),
        ("A", "1A"),
        ("AAA", "3A"),
        ("AAABBC", "3A2B1C"),
        ("Hello", "1H1e2l1o"),
        ("XXXXX", "5X"),
        ("AABBBCCCC", "2A3B4C"),
        ("abcd", "1a1b1c1d"),
        ("aaaaaaaaaaaa", "12a"),
    ],
)
def test_run_length_encode(text, expected):
    assert run_length_encode(text) == expected
