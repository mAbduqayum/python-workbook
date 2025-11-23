import pytest
from first_recurring_char import first_recurring


def test_first_char_recurs():
    assert first_recurring("ABCA") == "A"


def test_middle_char_recurs():
    assert first_recurring("ABCBA") == "B"


def test_no_recurring():
    assert first_recurring("ABC") is None


def test_adjacent_recurring():
    assert first_recurring("ABBA") == "B"


def test_case_sensitive():
    assert first_recurring("aAbBaA") == "a"


def test_empty_string():
    assert first_recurring("") is None


def test_all_same():
    assert first_recurring("aaaa") == "a"


def test_last_char_recurs():
    assert first_recurring("abcda") == "a"


def test_single_char():
    assert first_recurring("a") is None


def test_two_same_chars():
    assert first_recurring("aa") == "a"


def test_with_spaces():
    assert first_recurring("a b a") == " "


def test_numbers_in_string():
    assert first_recurring("a1b1") == "1"
