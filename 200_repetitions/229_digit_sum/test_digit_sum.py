from pathlib import Path
import pytest


@pytest.mark.parametrize("input_text, expected", [
    ("12345\n", "15"),
    ("-987\n", "24"),
    ("0\n", "0"),
    ("99\n", "18"),
    ("1000\n", "1"),
])
def test_digit_sum(script_runner, input_text, expected):
    script_path = Path(__file__).parent / "digit_sum.py"
    
    if not script_path.exists():
        pytest.skip("Solution file digit_sum.py not found")
    
    runner = script_runner(script_path)
    result = runner.run(input_text=input_text)
    assert result.stdout == expected
