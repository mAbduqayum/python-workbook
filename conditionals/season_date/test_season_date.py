import pytest


@pytest.mark.parametrize(
    "month, day, expected_output",
    [
        ("January", 15, "winter"),
        ("January", 1, "winter"),
        ("February", 14, "winter"),
        ("February", 28, "winter"),
        ("March", 19, "winter"),
        ("March", 20, "spring"),
        ("MARCH", 21, "spring"),
        ("March", 25, "spring"),
        ("April", 1, "spring"),
        ("april", 10, "spring"),
        ("May", 15, "spring"),
        ("june", 15, "spring"),
        ("June", 20, "spring"),
        ("June", 21, "summer"),
        ("July", 4, "summer"),
        ("August", 15, "summer"),
        ("September", 21, "summer"),
        ("September", 22, "fall"),
        ("October", 31, "fall"),
        ("November", 15, "fall"),
        ("December", 20, "fall"),
        ("December", 21, "winter"),
        ("December", 25, "winter"),
    ],
)
def test_season_date(solution, month, day, expected_output):
    solution.check_output(
        input_text=f"{month}\n{day}\n", expected_output=expected_output
    )
