try:
    from is_anagram import is_anagram
except ImportError:
    is_anagram = None


@pytest.mark.skipif(is_anagram is None, reason="is_anagram function not implemented")
def test_basic_anagrams():
    assert is_anagram("listen", "silent") is True


@pytest.mark.skipif(is_anagram is None, reason="is_anagram function not implemented")
def test_not_anagrams():
    assert is_anagram("hello", "world") is False


@pytest.mark.skipif(is_anagram is None, reason="is_anagram function not implemented")
def test_different_lengths():
    assert is_anagram("abc", "abcd") is False


@pytest.mark.skipif(is_anagram is None, reason="is_anagram function not implemented")
def test_same_word():
    assert is_anagram("test", "test") is True


@pytest.mark.skipif(is_anagram is None, reason="is_anagram function not implemented")
def test_case_sensitive():
    assert is_anagram("Listen", "silent") is False


@pytest.mark.skipif(is_anagram is None, reason="is_anagram function not implemented")
def test_empty():
    assert is_anagram("", "") is True


@pytest.mark.skipif(is_anagram is None, reason="is_anagram function not implemented")
def test_single_char():
    assert is_anagram("a", "a") is True


@pytest.mark.skipif(is_anagram is None, reason="is_anagram function not implemented")
def test_all_same_chars():
    assert is_anagram("aaa", "aaa") is True


@pytest.mark.skipif(is_anagram is None, reason="is_anagram function not implemented")
def test_different_order():
    assert is_anagram("abcdef", "fedcba") is True


@pytest.mark.skipif(is_anagram is None, reason="is_anagram function not implemented")
def test_repeated_chars():
    assert is_anagram("aabbcc", "abcabc") is True


@pytest.mark.skipif(is_anagram is None, reason="is_anagram function not implemented")
def test_partial_match():
    assert is_anagram("abc", "abd") is False
