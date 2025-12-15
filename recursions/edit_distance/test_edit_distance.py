import pytest

try:
    from edit_distance import edit_distance
except ImportError:
    edit_distance = None


@pytest.mark.skipif(edit_distance is None, reason="edit_distance not implemented")
@pytest.mark.parametrize(
    "s1, s2, expected",
    [
        ("", "", 0),
        ("", "abc", 3),
        ("abc", "", 3),
        ("abc", "abc", 0),
        ("kitten", "sitting", 3),
        ("horse", "ros", 3),
        ("intention", "execution", 5),
        ("a", "b", 1),
        ("ab", "ac", 1),
        ("abc", "axc", 1),
        ("sunday", "saturday", 3),
    ],
)
def test_edit_distance(s1, s2, expected):
    assert edit_distance(s1, s2) == expected
