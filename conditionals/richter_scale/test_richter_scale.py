import pytest


@pytest.mark.parametrize(
    "magnitude, expected_output",
    [
        (0.5, "micro"),
        (1.5, "micro"),
        (2.0, "very minor"),
        (2.5, "very minor"),
        (3.0, "minor"),
        (3.5, "minor"),
        (4.0, "light"),
        (4.5, "light"),
        (5.0, "moderate"),
        (5.5, "moderate"),
        (6.0, "strong"),
        (6.5, "strong"),
        (7.0, "major"),
        (7.2, "major"),
        (8.0, "great"),
        (8.9, "great"),
        (10.0, "meteoric"),
        (10.5, "meteoric"),
        (15.0, "meteoric"),
    ],
)
def test_richter_scale(solution, magnitude, expected_output):
    solution.check_output(input_text=f"{magnitude}\n", expected_output=expected_output)
