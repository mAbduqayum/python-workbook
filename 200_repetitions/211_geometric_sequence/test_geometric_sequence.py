from pathlib import Path
import pytest


@pytest.mark.parametrize("input_text, expected", [
    ("2\n5\n3\n", "2.0\n6.0\n18.0\n54.0\n162.0"),
    ("100\n4\n0.5\n", "100.0\n50.0\n25.0\n12.5"),
    ("5\n1\n2\n", "5.0"),
    ("5\n0\n2\n", "Error"),
])
def test_geometric_sequence(script_runner, input_text, expected):
    script_path = Path(__file__).parent / "geometric_sequence.py"
    
    if not script_path.exists():
        pytest.skip("Solution file geometric_sequence.py not found")
    
    runner = script_runner(script_path)
    result = runner.run(input_text=input_text)
    assert result.stdout == expected
