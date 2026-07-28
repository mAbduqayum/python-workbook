import pytest

try:
    from roman_to_int import roman_to_int
except ImportError:
    roman_to_int = None


@pytest.mark.skipif(
    roman_to_int is None, reason="roman_to_int function not implemented"
)
def test_basic_iii():
    assert roman_to_int("III") == 3


@pytest.mark.skipif(
    roman_to_int is None, reason="roman_to_int function not implemented"
)
def test_subtraction_iv():
    assert roman_to_int("IV") == 4


@pytest.mark.skipif(
    roman_to_int is None, reason="roman_to_int function not implemented"
)
def test_subtraction_ix():
    assert roman_to_int("IX") == 9


@pytest.mark.skipif(
    roman_to_int is None, reason="roman_to_int function not implemented"
)
def test_complex_mcmxciv():
    assert roman_to_int("MCMXCIV") == 1994


@pytest.mark.skipif(
    roman_to_int is None, reason="roman_to_int function not implemented"
)
def test_lviii():
    assert roman_to_int("LVIII") == 58


@pytest.mark.skipif(
    roman_to_int is None, reason="roman_to_int function not implemented"
)
def test_single_i():
    assert roman_to_int("I") == 1


@pytest.mark.skipif(
    roman_to_int is None, reason="roman_to_int function not implemented"
)
def test_xiv():
    assert roman_to_int("XIV") == 14


@pytest.mark.skipif(
    roman_to_int is None, reason="roman_to_int function not implemented"
)
def test_xl():
    assert roman_to_int("XL") == 40


@pytest.mark.skipif(
    roman_to_int is None, reason="roman_to_int function not implemented"
)
def test_cd():
    assert roman_to_int("CD") == 400


@pytest.mark.skipif(
    roman_to_int is None, reason="roman_to_int function not implemented"
)
def test_cm():
    assert roman_to_int("CM") == 900


@pytest.mark.skipif(
    roman_to_int is None, reason="roman_to_int function not implemented"
)
def test_large_mmmcmxcix():
    assert roman_to_int("MMMCMXCIX") == 3999


@pytest.mark.skipif(
    roman_to_int is None, reason="roman_to_int function not implemented"
)
def test_xcix():
    assert roman_to_int("XCIX") == 99
