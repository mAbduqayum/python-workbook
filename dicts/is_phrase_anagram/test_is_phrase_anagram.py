import pytest
from is_phrase_anagram import is_phrase_anagram


def test_basic():
    assert is_phrase_anagram("listen", "silent") is True


def test_with_spaces():
    assert is_phrase_anagram("conversation", "voices rant on") is True


def test_case_insensitive():
    assert is_phrase_anagram("The Eyes", "They See") is True


def test_not_anagrams():
    assert is_phrase_anagram("hello world", "world peace") is False


def test_different_after_cleaning():
    assert is_phrase_anagram("abc", "a b c") is True


def test_empty():
    assert is_phrase_anagram("", "") is True


def test_spaces_only():
    assert is_phrase_anagram(" ", "") is True


def test_mixed_case_and_spaces():
    assert is_phrase_anagram("A gentleman", "Elegant man") is True


def test_complex_phrase():
    assert is_phrase_anagram("Eleven plus two", "Twelve plus one") is True


def test_partial_match():
    assert is_phrase_anagram("hello", "help") is False
