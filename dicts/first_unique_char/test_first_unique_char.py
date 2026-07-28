import pytest

try:
    from first_unique_char import first_unique_char
except ImportError:
    first_unique_char = None


@pytest.mark.skipif(
    first_unique_char is None, reason="first_unique_char function not implemented"
)
def test_basic():
    assert first_unique_char("leetcode") == "l"


@pytest.mark.skipif(
    first_unique_char is None, reason="first_unique_char function not implemented"
)
def test_first_is_unique():
    assert first_unique_char("abcab") == "c"


@pytest.mark.skipif(
    first_unique_char is None, reason="first_unique_char function not implemented"
)
def test_last_is_unique():
    assert first_unique_char("aabbcd") == "c"


@pytest.mark.skipif(
    first_unique_char is None, reason="first_unique_char function not implemented"
)
def test_no_unique():
    assert first_unique_char("aabbcc") is None


@pytest.mark.skipif(
    first_unique_char is None, reason="first_unique_char function not implemented"
)
def test_all_unique():
    assert first_unique_char("abc") == "a"


@pytest.mark.skipif(
    first_unique_char is None, reason="first_unique_char function not implemented"
)
def test_single_char():
    assert first_unique_char("a") == "a"


@pytest.mark.skipif(
    first_unique_char is None, reason="first_unique_char function not implemented"
)
def test_empty():
    assert first_unique_char("") is None


@pytest.mark.skipif(
    first_unique_char is None, reason="first_unique_char function not implemented"
)
def test_case_sensitive():
    assert first_unique_char("AaBbCc") == "A"


@pytest.mark.skipif(
    first_unique_char is None, reason="first_unique_char function not implemented"
)
def test_middle_unique():
    assert first_unique_char("loveleetcode") == "v"


@pytest.mark.skipif(
    first_unique_char is None, reason="first_unique_char function not implemented"
)
def test_with_spaces():
    assert first_unique_char("hello world") == "h"
