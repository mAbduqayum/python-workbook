import pytest

try:
    from first_repeat import first_repeat
except ImportError:
    first_repeat = None

pytestmark = pytest.mark.skipif(
    first_repeat is None, reason="first_repeat function not implemented"
)


@pytest.mark.parametrize(
    "words, expected",
    [
        (["the", "cat", "saw", "the", "dog"], "the"),
        (["red", "blue", "green", "blue", "red"], "blue"),
        (["go", "go"], "go"),
        (["a", "b", "c", "a"], "a"),
        (["one", "two", "three"], ""),
        (["solo"], ""),
        ([], ""),
    ],
)
def test_first_repeat(words, expected):
    assert first_repeat(words) == expected


@pytest.mark.parametrize(
    "words, expected",
    [
        (["The", "cat", "saw", "the", "dog"], "the"),
        (["Cat", "cat"], "cat"),
        (["cat", "CAT"], "cat"),
        (["Red", "BLUE", "green", "blue"], "blue"),
    ],
)
def test_case_does_not_matter(words, expected):
    assert first_repeat(words) == expected
