import pytest

try:
    from remove_duplicate_letters import remove_duplicate_letters
except ImportError:
    remove_duplicate_letters = None


@pytest.mark.skipif(
    remove_duplicate_letters is None,
    reason="remove_duplicate_letters function not implemented",
)
def test_hello():
    assert remove_duplicate_letters("hello") == "helo"


@pytest.mark.skipif(
    remove_duplicate_letters is None,
    reason="remove_duplicate_letters function not implemented",
)
def test_mississippi():
    assert remove_duplicate_letters("mississippi") == "misp"


@pytest.mark.skipif(
    remove_duplicate_letters is None,
    reason="remove_duplicate_letters function not implemented",
)
def test_abcabc():
    assert remove_duplicate_letters("abcabc") == "abc"


@pytest.mark.skipif(
    remove_duplicate_letters is None,
    reason="remove_duplicate_letters function not implemented",
)
def test_case_sensitive():
    assert remove_duplicate_letters("AaAaBb") == "AaBb"


@pytest.mark.skipif(
    remove_duplicate_letters is None,
    reason="remove_duplicate_letters function not implemented",
)
def test_empty_string():
    assert remove_duplicate_letters("") == ""


@pytest.mark.skipif(
    remove_duplicate_letters is None,
    reason="remove_duplicate_letters function not implemented",
)
def test_no_duplicates():
    assert remove_duplicate_letters("abcdef") == "abcdef"


@pytest.mark.skipif(
    remove_duplicate_letters is None,
    reason="remove_duplicate_letters function not implemented",
)
def test_all_same():
    assert remove_duplicate_letters("aaaa") == "a"


@pytest.mark.skipif(
    remove_duplicate_letters is None,
    reason="remove_duplicate_letters function not implemented",
)
def test_single_char():
    assert remove_duplicate_letters("x") == "x"


@pytest.mark.skipif(
    remove_duplicate_letters is None,
    reason="remove_duplicate_letters function not implemented",
)
def test_with_spaces():
    assert remove_duplicate_letters("a b a b") == "a b"


@pytest.mark.skipif(
    remove_duplicate_letters is None,
    reason="remove_duplicate_letters function not implemented",
)
def test_with_numbers():
    assert remove_duplicate_letters("a1b1c1") == "a1bc"
