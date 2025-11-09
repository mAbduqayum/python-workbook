import pytest

try:
    from get_words import get_words
except ImportError:
    get_words = None


@pytest.mark.skipif(get_words is None, reason="get_words function not implemented")
@pytest.mark.parametrize(
    "sentence, expected",
    [
        ("Hello world", ["Hello", "world"]),
        ("Python is fun", ["Python", "is", "fun"]),
        ("", []),
        ("One", ["One"]),
        ("a b c d", ["a", "b", "c", "d"]),
        ("  multiple   spaces  ", ["multiple", "spaces"]),
    ],
)
def test_get_words(sentence, expected):
    assert get_words(sentence) == expected
