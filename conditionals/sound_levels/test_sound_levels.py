import pytest


@pytest.mark.parametrize(
    "decibel_level, expected_output",
    [
        (0, "quieter than quiet room"),
        (25, "quieter than quiet room"),
        (35, "quieter than quiet room"),
        (40, "quiet room"),
        (50, "between quiet room and alarm clock"),
        (55, "between quiet room and alarm clock"),
        (70, "alarm clock"),
        (80, "between alarm clock and gas lawnmower"),
        (90, "between alarm clock and gas lawnmower"),
        (106, "gas lawnmower"),
        (115, "between gas lawnmower and jackhammer"),
        (120, "between gas lawnmower and jackhammer"),
        (130, "jackhammer"),
        (140, "louder than jackhammer"),
        (145, "louder than jackhammer"),
        (200, "louder than jackhammer"),
    ],
)
def test_sound_levels(solution, decibel_level, expected_output):
    solution.check_output(
        input_text=f"{decibel_level}\n", expected_output=expected_output
    )
