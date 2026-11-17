import pytest


@pytest.mark.parametrize(
    "age, expected_output",
    [
        (0, "infant"),
        (1, "infant"),
        (2, "toddler"),
        (3, "toddler"),
        (4, "toddler"),
        (5, "child"),
        (8, "child"),
        (10, "child"),
        (11, "adolescent"),
        (15, "adolescent"),
        (17, "adolescent"),
        (18, "young adult"),
        (25, "young adult"),
        (39, "young adult"),
        (40, "middle-aged"),
        (50, "middle-aged"),
        (64, "middle-aged"),
        (65, "senior"),
        (70, "senior"),
        (100, "senior"),
        (-5, "invalid age"),
        (-1, "invalid age"),
    ],
)
def test_life_phases(solution, age, expected_output):
    solution.check_output(input_text=f"{age}\n", expected_output=expected_output)
