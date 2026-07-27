try:
    from group_anagrams import group_anagrams
except ImportError:
    group_anagrams = None


@pytest.mark.skipif(
    group_anagrams is None, reason="group_anagrams function not implemented"
)
def test_basic():
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    # Sort each group and the list of groups for comparison
    result_sorted = [sorted(group) for group in result]
    result_sorted.sort()
    expected = [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
    assert result_sorted == expected


@pytest.mark.skipif(
    group_anagrams is None, reason="group_anagrams function not implemented"
)
def test_no_anagrams():
    result = group_anagrams(["abc", "def"])
    assert len(result) == 2
    assert ["abc"] in result
    assert ["def"] in result


@pytest.mark.skipif(
    group_anagrams is None, reason="group_anagrams function not implemented"
)
def test_all_anagrams():
    result = group_anagrams(["abc", "bca", "cab"])
    assert len(result) == 1
    assert sorted(result[0]) == ["abc", "bca", "cab"]


@pytest.mark.skipif(
    group_anagrams is None, reason="group_anagrams function not implemented"
)
def test_empty_list():
    assert group_anagrams([]) == []


@pytest.mark.skipif(
    group_anagrams is None, reason="group_anagrams function not implemented"
)
def test_single_word():
    assert group_anagrams(["hello"]) == [["hello"]]


@pytest.mark.skipif(
    group_anagrams is None, reason="group_anagrams function not implemented"
)
def test_empty_strings():
    result = group_anagrams(["", ""])
    assert result == [["", ""]]


@pytest.mark.skipif(
    group_anagrams is None, reason="group_anagrams function not implemented"
)
def test_single_char_words():
    result = group_anagrams(["a", "b", "a"])
    result_sorted = [sorted(group) for group in result]
    result_sorted.sort()
    expected = [["a", "a"], ["b"]]
    assert result_sorted == expected
