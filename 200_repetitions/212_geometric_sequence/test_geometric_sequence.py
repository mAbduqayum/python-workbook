from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("2\n5\n3\n", "2\n6\n18\n54\n162"),
        ("100\n5\n0.5\n", "100\n50\n25\n12.5\n6.25"),
        ("5\n1\n2\n", "5"),
    ],
)
def test_geometric_sequence(script_runner, input_text, expected):
    script_path = Path(__file__).parent / "geometric_sequence.py"

    if not script_path.exists():
        pytest.skip("Solution file geometric_sequence.py not found")

    runner = script_runner(script_path)
    result = runner.run(input_text=input_text)
    assert result.stdout == expected
