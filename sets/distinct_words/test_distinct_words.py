import pytest

try:
    from distinct_words import distinct_words
except ImportError:
    distinct_words = None

pytestmark = pytest.mark.skipif(
    distinct_words is None, reason="distinct_words function not implemented"
)


@pytest.mark.parametrize(
    "text, expected",
    [
        ("the cat and the hat", 4),
        ("The the THE", 1),
        ("one two three", 3),
        ("word", 1),
        ("", 0),
        ("a b a b a b", 2),
        ("Go go GO stop Stop", 2),
        ("  extra   spaces  here ", 3),
    ],
)
def test_distinct_words(text, expected):
    assert distinct_words(text) == expected
