import pytest


@pytest.mark.parametrize(
    "year, month, day, expected_output",
    [
        (1900, 2, 28, "1900 3 1"),  # Non-leap year (divisible by 100, not 400)
        (2000, 2, 29, "2000 3 1"),  # Leap year (divisible by 400)
        (2001, 1, 1, "2001 1 2"),  # Regular day in January
        (2004, 2, 29, "2004 3 1"),  # Leap year (divisible by 4)
        (2019, 11, 18, "2019 11 19"),  # Regular day
        (2019, 11, 30, "2019 12 1"),  # End of month
        (2019, 12, 31, "2020 1 1"),  # End of year
        (2020, 1, 31, "2020 2 1"),  # End of January
        (2020, 10, 31, "2020 11 1"),  # End of October
        (2020, 11, 30, "2020 12 1"),  # End of November (30 days)
        (2020, 12, 31, "2021 1 1"),  # End of December
        (2020, 2, 28, "2020 2 29"),  # Leap year February
        (2020, 2, 29, "2020 3 1"),  # Last day of leap year February
        (2020, 3, 31, "2020 4 1"),  # End of March
        (2020, 4, 30, "2020 5 1"),  # End of April (30 days)
        (2020, 5, 31, "2020 6 1"),  # End of May
        (2020, 6, 30, "2020 7 1"),  # End of June (30 days)
        (2020, 7, 31, "2020 8 1"),  # End of July
        (2020, 8, 31, "2020 9 1"),  # End of August
        (2020, 9, 30, "2020 10 1"),  # End of September (30 days)
        (2021, 2, 28, "2021 3 1"),  # Non-leap year February
    ],
)
def test_next_day(solution, year, month, day, expected_output):
    solution.check_output(
        input_text=f"{year}\n{month}\n{day}\n", expected_output=expected_output
    )
