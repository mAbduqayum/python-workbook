from pathlib import Path
import pytest


@pytest.mark.parametrize("input_text, expected", [
    ("5\n", "*\n   ***\n  *****\n *******\n*********"),
    ("3\n", "*\n ***\n*****"),
    ("1\n", "*"),
    ("0\n", "Error"),
])
def test_pyramid(script_runner, input_text, expected):
    script_path = Path(__file__).parent / "pyramid.py"
    
    if not script_path.exists():
        pytest.skip("Solution file pyramid.py not found")
    
    runner = script_runner(script_path)
    result = runner.run(input_text=input_text)
    assert result.stdout == expected
