import pytest


@pytest.mark.parametrize(
    "wavelength, expected_output",
    [
        (300, "outside visible spectrum"),
        (379, "outside visible spectrum"),  # Just below visible
        (380, "violet"),  # Lower boundary of violet
        (420, "violet"),
        (449, "violet"),  # Just below blue
        (450, "blue"),  # Lower boundary of blue
        (480, "blue"),
        (494, "blue"),  # Just below green
        (495, "green"),  # Lower boundary of green
        (550, "green"),
        (569, "green"),  # Just below yellow
        (570, "yellow"),  # Lower boundary of yellow
        (580, "yellow"),
        (589, "yellow"),  # Just below orange
        (590, "orange"),  # Lower boundary of orange
        (600, "orange"),
        (619, "orange"),  # Just below red
        (620, "red"),  # Lower boundary of red
        (700, "red"),
        (750, "red"),  # Upper boundary of red
        (751, "outside visible spectrum"),  # Just above visible
        (800, "outside visible spectrum"),
    ],
)
def test_visible_light(solution, wavelength, expected_output):
    solution.check_output(input_text=f"{wavelength}\n", expected_output=expected_output)
