import pytest

try:
    from is_valid_date import days_in_month, is_valid_date
except ImportError:
    days_in_month = None
    is_valid_date = None

pytestmark = pytest.mark.skipif(
    days_in_month is None or is_valid_date is None,
    reason="days_in_month or is_valid_date not implemented",
)


@pytest.mark.parametrize(
    "month, expected",
    [
        (1, 31),
        (2, 28),
        (3, 31),
        (4, 30),
        (5, 31),
        (6, 30),
        (7, 31),
        (8, 31),
        (9, 30),
        (10, 31),
        (11, 30),
        (12, 31),
    ],
)
def test_days_in_month_common_year(month, expected):
    assert days_in_month(2023, month) == expected


@pytest.mark.parametrize(
    "year, expected",
    [
        (2024, 29),
        (2023, 28),
        (2000, 29),
        (1900, 28),
    ],
)
def test_days_in_february(year, expected):
    assert days_in_month(year, 2) == expected


@pytest.mark.parametrize(
    "year, month, day, expected",
    [
        (2024, 2, 29, True),
        (2023, 2, 29, False),
        (1900, 2, 29, False),
        (2000, 2, 29, True),
        (2023, 4, 30, True),
        (2023, 4, 31, False),
        (2023, 1, 31, True),
        (2023, 12, 31, True),
        (2023, 13, 1, False),
        (2023, 0, 1, False),
        (2023, 12, 0, False),
        (2023, 6, -1, False),
    ],
)
def test_is_valid_date(year, month, day, expected):
    assert is_valid_date(year, month, day) is expected
