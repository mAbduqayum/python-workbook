import pytest

try:
    from isogram import is_isogram
except ImportError:
    is_isogram = None


@pytest.mark.skipif(is_isogram is None, reason="is_isogram function not implemented")
def test_simple_isogram():
    assert is_isogram("lumberjacks") is True


@pytest.mark.skipif(is_isogram is None, reason="is_isogram function not implemented")
def test_repeated_letter():
    assert is_isogram("isograms") is False


@pytest.mark.skipif(is_isogram is None, reason="is_isogram function not implemented")
def test_case_insensitive():
    assert is_isogram("Alphabet") is False


@pytest.mark.skipif(is_isogram is None, reason="is_isogram function not implemented")
def test_hyphen_ignored():
    assert is_isogram("thumbscrew-japingly") is True


@pytest.mark.skipif(is_isogram is None, reason="is_isogram function not implemented")
def test_spaces_ignored():
    assert is_isogram("Emily Jung Schwartzkopf") is True


@pytest.mark.skipif(is_isogram is None, reason="is_isogram function not implemented")
def test_empty_string():
    assert is_isogram("") is True


@pytest.mark.skipif(is_isogram is None, reason="is_isogram function not implemented")
def test_single_letter():
    assert is_isogram("a") is True


@pytest.mark.skipif(is_isogram is None, reason="is_isogram function not implemented")
def test_long_isogram():
    assert is_isogram("subdermatoglyphic") is True


@pytest.mark.skipif(is_isogram is None, reason="is_isogram function not implemented")
def test_adjacent_repeat():
    assert is_isogram("eleven") is False


@pytest.mark.skipif(is_isogram is None, reason="is_isogram function not implemented")
def test_all_same_letter():
    assert is_isogram("aaa") is False


@pytest.mark.skipif(is_isogram is None, reason="is_isogram function not implemented")
def test_case_insensitive_repeat():
    assert is_isogram("abcABC") is False
