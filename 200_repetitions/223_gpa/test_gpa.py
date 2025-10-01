from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_values, expected_gpa",
    [
        ("A\nC+\nB\n\n", "3.1"),
        ("A+\nA\nA-\n\n", "3.9"),
        ("B\nB\nB\n\n", "3.0"),
        ("A+\n\n", "4.0"),
        ("F\nF\n\n", "0.0"),
    ],
)
def test_gpa(script_runner, input_values, expected_gpa):
    script_path = Path(__file__).parent / "gpa.py"

    if not script_path.exists():
        pytest.skip("Solution file gpa.py not found")

    runner = script_runner(script_path)
    result = runner.run(input_text=input_values)

    # Check if expected GPA appears in output
    assert (
        expected_gpa in result.stdout
        or str(round(float(expected_gpa), 1)) in result.stdout
    )
