import pytest


@pytest.mark.parametrize(
    "year, expected_output",
    [
        (-1, "invalid year"),
        (0, "invalid year"),
        (1, "freshman"),
        (2, "sophomore"),
        (3, "junior"),
        (4, "senior"),
        (5, "invalid year"),
    ],
)
def test_student_year_level(solution, year, expected_output):
    solution.check_output(input_text=f"{year}\n", expected_output=expected_output)
