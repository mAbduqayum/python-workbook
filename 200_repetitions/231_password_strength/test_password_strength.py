from pathlib import Path
import pytest


@pytest.mark.parametrize("input_text, expected", [
    ("Hello123\n", "Strong"),
    ("hello123\n", "Moderate"),
    ("HELLO123\n", "Moderate"),
    ("HelloWorld\n", "Moderate"),
    ("hello\n", "Weak"),
    ("12345\n", "Weak"),
    ("\n", "Weak"),
])
def test_password_strength(script_runner, input_text, expected):
    script_path = Path(__file__).parent / "password_strength.py"
    
    if not script_path.exists():
        pytest.skip("Solution file password_strength.py not found")
    
    runner = script_runner(script_path)
    result = runner.run(input_text=input_text)
    assert result.stdout == expected
