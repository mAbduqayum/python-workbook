import pytest


@pytest.mark.parametrize(
    "angle, expected_output",
    [
        (-30, "invalid angle"),
        (-1, "invalid angle"),
        (0, "invalid angle"),
        (1, "acute angle"),
        (30, "acute angle"),
        (45, "acute angle"),
        (60, "acute angle"),
        (89, "acute angle"),
        (90, "right angle"),
        (91, "obtuse angle"),
        (120, "obtuse angle"),
        (150, "obtuse angle"),
        (179, "obtuse angle"),
        (180, "straight angle"),
        (181, "reflex angle"),
        (200, "reflex angle"),
        (270, "reflex angle"),
        (300, "reflex angle"),
        (359, "reflex angle"),
        (360, "full rotation"),
        (361, "invalid angle"),
        (450, "invalid angle"),
        (720, "invalid angle"),
    ],
)
def test_angle_type(solution, angle, expected_output):
    solution.check_output(input_text=f"{angle}\n", expected_output=expected_output)
