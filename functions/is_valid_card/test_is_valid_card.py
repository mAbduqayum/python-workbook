import pytest

try:
    from is_valid_card import digits_only, is_valid_card, luhn_sum
except ImportError:
    digits_only = None
    luhn_sum = None
    is_valid_card = None

pytestmark = pytest.mark.skipif(
    digits_only is None or luhn_sum is None or is_valid_card is None,
    reason="digits_only, luhn_sum or is_valid_card not implemented",
)


@pytest.mark.parametrize(
    "number, expected",
    [
        ("4539 1488 0343 6467", "4539148803436467"),
        ("79927398713", "79927398713"),
        ("1 2 3", "123"),
        ("", ""),
    ],
)
def test_digits_only(number, expected):
    assert digits_only(number) == expected


@pytest.mark.parametrize(
    "digits, expected",
    [
        ("0", 0),
        ("7", 7),
        ("18", 10),
        ("59", 10),
        ("4321", 16),
        ("8763", 20),
        ("79927398713", 70),
    ],
)
def test_luhn_sum(digits, expected):
    assert luhn_sum(digits) == expected


@pytest.mark.parametrize(
    "number, expected",
    [
        ("79927398713", True),
        ("79927398710", False),
        ("4539 1488 0343 6467", True),
        ("4539 1488 0343 6468", False),
        ("18", True),
        ("12", False),
    ],
)
def test_is_valid_card(number, expected):
    assert is_valid_card(number) is expected
