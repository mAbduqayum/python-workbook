import pytest


@pytest.mark.parametrize(
    "sides, expected_output",
    [
        (3, "triangle"),
        (4, "quadrilateral"),
        (5, "pentagon"),
        (6, "hexagon"),
        (7, "heptagon"),
        (8, "octagon"),
        (9, "nonagon"),
        (10, "decagon"),
        (2, "invalid number of sides"),
        (11, "invalid number of sides"),
        (15, "invalid number of sides"),
        (0, "invalid number of sides"),
        (-1, "invalid number of sides"),
    ],
)
def test_name_shape(solution, sides, expected_output):
    solution.check_output(input_text=f"{sides}\n", expected_output=expected_output)
