from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "magnitude, expected_output",
    [
        (0.5, "Micro"),
        (1.5, "Micro"),
        (2.0, "Very Minor"),
        (2.5, "Very Minor"),
        (3.0, "Minor"),
        (3.5, "Minor"),
        (4.0, "Light"),
        (4.5, "Light"),
        (5.0, "Moderate"),
        (5.5, "Moderate"),
        (6.0, "Strong"),
        (6.5, "Strong"),
        (7.0, "Major"),
        (7.2, "Major"),
        (8.0, "Great"),
        (8.9, "Great"),
        (10.0, "Great"),
        (10.5, "Meteoric"),
        (15.0, "Meteoric"),
    ],
)
def test_richter_scale(script_runner, magnitude, expected_output):
    script_path = Path(__file__).parent / "richter_scale.py"

    if not script_path.exists():
        pytest.skip("Solution file richter_scale.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=f"{magnitude}\n", expected_output=expected_output
    )
