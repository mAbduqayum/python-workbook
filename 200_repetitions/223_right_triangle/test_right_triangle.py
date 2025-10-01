from pathlib import Path
import pytest


@pytest.mark.parametrize("input_text, expected", [
    ("5\n", "*\n**\n***\n****\n*****"),
    ("3\n", "*\n**\n***"),
    ("1\n", "*"),
    ("0\n", "Error"),
])
def test_right_triangle(script_runner, input_text, expected):
    script_path = Path(__file__).parent / "right_triangle.py"
    
    if not script_path.exists():
        pytest.skip("Solution file right_triangle.py not found")
    
    runner = script_runner(script_path)
    result = runner.run(input_text=input_text)
    assert result.stdout == expected
