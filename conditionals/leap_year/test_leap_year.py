import pytest


@pytest.mark.parametrize(
    "year, expected_output",
    [
        (1600, "leap year"),  # Divisible by 400
        (1700, "not leap year"),  # Divisible by 100 but not 400
        (1800, "not leap year"),  # Divisible by 100 but not 400
        (1900, "not leap year"),  # Divisible by 100 but not 400
        (1996, "leap year"),  # Divisible by 4 but not 100
        (1997, "not leap year"),  # Not divisible by 4
        (1998, "not leap year"),  # Not divisible by 4
        (1999, "not leap year"),  # Not divisible by 4
        (2000, "leap year"),  # Divisible by 400
        (2001, "not leap year"),  # Not divisible by 4
        (2004, "leap year"),  # Divisible by 4 but not 100
        (2012, "leap year"),  # Divisible by 4 but not 100
        (2021, "not leap year"),  # Not divisible by 4
        (2024, "leap year"),  # Divisible by 4 but not 100
        (2100, "not leap year"),  # Divisible by 100 but not 400
        (2400, "leap year"),  # Divisible by 400
    ],
)
def test_leap_year(solution, year, expected_output):
    solution.check_output(input_text=f"{year}\n", expected_output=expected_output)
