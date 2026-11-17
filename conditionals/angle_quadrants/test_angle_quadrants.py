import pytest


@pytest.mark.parametrize(
    "angle, expected_output",
    [
        (-180, "on axis"),
        (-135, "quadrant III"),
        (-90, "on axis"),
        (-45, "quadrant IV"),
        (-30, "quadrant IV"),
        (0, "on axis"),
        (1, "quadrant I"),
        (90, "on axis"),
        (120, "quadrant II"),
        (180, "on axis"),
        (225, "quadrant III"),
        (270, "on axis"),
        (315, "quadrant IV"),
        (359, "quadrant IV"),
        (360, "on axis"),
        (405, "quadrant I"),
        (45, "quadrant I"),
        (450, "on axis"),
        (720, "on axis"),
        (810, "on axis"),
    ],
)
def test_angle_quadrants(solution, angle, expected_output):
    solution.check_output(input_text=f"{angle}\n", expected_output=expected_output)
