import pytest


@pytest.mark.parametrize(
    "month, day, expected_output",
    [
        (1, 1, "New Year's Day"),
        (1, 2, "not a national holiday"),
        (2, 14, "not a national holiday"),
        (3, 8, "International Women's Day"),
        (3, 19, "not a national holiday"),
        (3, 20, "not a national holiday"),
        (3, 21, "Navruz (Persian New Year)"),
        (3, 22, "Navruz (Persian New Year)"),
        (3, 23, "Navruz (Persian New Year)"),
        (3, 24, "Navruz (Persian New Year)"),
        (3, 25, "not a national holiday"),
        (5, 1, "Labor Day"),
        (5, 9, "Victory Day"),
        (6, 27, "National Unity Day"),
        (7, 4, "not a national holiday"),
        (9, 9, "Independence Day"),
        (10, 31, "not a national holiday"),
        (11, 6, "Constitution Day"),
        (12, 25, "not a national holiday"),
        (12, 31, "not a national holiday"),
    ],
)
def test_tajikistan_holidays(solution, month, day, expected_output):
    solution.check_output(
        input_text=f"{month}\n{day}\n", expected_output=expected_output
    )
