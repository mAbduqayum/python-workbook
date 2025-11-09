import pytest

try:
    from sublists import sublists
except ImportError:
    sublists = None


@pytest.mark.skipif(sublists is None, reason="sublists function not implemented")
@pytest.mark.parametrize(
    "lst, expected_count",
    [
        ([1, 2, 3], 7),  # [], [1], [1,2], [1,2,3], [2], [2,3], [3]
        ([1, 2], 4),  # [], [1], [1,2], [2]
        ([1], 2),  # [], [1]
        ([], 1),  # []
    ],
)
def test_sublists_count(lst, expected_count):
    result = sublists(lst)
    assert len(result) == expected_count


@pytest.mark.skipif(sublists is None, reason="sublists function not implemented")
def test_sublists_content():
    result = sublists([1, 2, 3])
    assert [] in result
    assert [1] in result
    assert [2] in result
    assert [3] in result
    assert [1, 2] in result
    assert [2, 3] in result
    assert [1, 2, 3] in result
