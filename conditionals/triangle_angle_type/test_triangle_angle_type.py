import pytest


@pytest.mark.parametrize(
    "angle1, angle2, angle3, expected_output",
    [
        (60, 60, 60, "acute triangle"),
        (90, 45, 45, "right triangle"),
        (120, 30, 30, "obtuse triangle"),
        (30, 60, 90, "right triangle"),
        (45, 45, 90, "right triangle"),
        (100, 40, 40, "obtuse triangle"),
        (70, 70, 40, "acute triangle"),
        (80, 80, 20, "acute triangle"),
        (179, 0.5, 0.5, "obtuse triangle"),
        (1, 1, 178, "obtuse triangle"),
        (30, 30, 120, "obtuse triangle"),
        (45, 60, 75, "acute triangle"),
        (90, 90, 90, "invalid triangle"),
        (50, 60, 80, "invalid triangle"),
    ],
)
def test_triangle_angle_type(solution, angle1, angle2, angle3, expected_output):
    solution.check_output(
        input_text=f"{angle1}\n{angle2}\n{angle3}\n", expected_output=expected_output
    )
