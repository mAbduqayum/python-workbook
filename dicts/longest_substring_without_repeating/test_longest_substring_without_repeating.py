import pytest

try:
    from longest_substring_without_repeating import longest_substring_without_repeating
except ImportError:
    longest_substring_without_repeating = None


@pytest.mark.skipif(
    longest_substring_without_repeating is None,
    reason="longest_substring_without_repeating function not implemented",
)
def test_abcabcbb():
    assert longest_substring_without_repeating("abcabcbb") == 3


@pytest.mark.skipif(
    longest_substring_without_repeating is None,
    reason="longest_substring_without_repeating function not implemented",
)
def test_all_same():
    assert longest_substring_without_repeating("bbbbb") == 1


@pytest.mark.skipif(
    longest_substring_without_repeating is None,
    reason="longest_substring_without_repeating function not implemented",
)
def test_no_repeats():
    assert longest_substring_without_repeating("abcdef") == 6


@pytest.mark.skipif(
    longest_substring_without_repeating is None,
    reason="longest_substring_without_repeating function not implemented",
)
def test_empty():
    assert longest_substring_without_repeating("") == 0


@pytest.mark.skipif(
    longest_substring_without_repeating is None,
    reason="longest_substring_without_repeating function not implemented",
)
def test_single_char():
    assert longest_substring_without_repeating("a") == 1


@pytest.mark.skipif(
    longest_substring_without_repeating is None,
    reason="longest_substring_without_repeating function not implemented",
)
def test_middle_repeat():
    assert longest_substring_without_repeating("pwwkew") == 3


@pytest.mark.skipif(
    longest_substring_without_repeating is None,
    reason="longest_substring_without_repeating function not implemented",
)
def test_complex():
    assert longest_substring_without_repeating("dvdf") == 3


@pytest.mark.skipif(
    longest_substring_without_repeating is None,
    reason="longest_substring_without_repeating function not implemented",
)
def test_long():
    assert longest_substring_without_repeating("abcdefghijklmnop") == 16


@pytest.mark.skipif(
    longest_substring_without_repeating is None,
    reason="longest_substring_without_repeating function not implemented",
)
def test_two_chars():
    assert longest_substring_without_repeating("ab") == 2


@pytest.mark.skipif(
    longest_substring_without_repeating is None,
    reason="longest_substring_without_repeating function not implemented",
)
def test_pattern():
    assert longest_substring_without_repeating("abba") == 2


@pytest.mark.skipif(
    longest_substring_without_repeating is None,
    reason="longest_substring_without_repeating function not implemented",
)
def test_space():
    assert longest_substring_without_repeating("a b c a") == 3


@pytest.mark.skipif(
    longest_substring_without_repeating is None,
    reason="longest_substring_without_repeating function not implemented",
)
def test_numbers():
    assert longest_substring_without_repeating("12345123") == 5
