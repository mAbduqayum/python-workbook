from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("Hello123!@#\n", "Very Strong"),
        ("Hello123\n", "Strong"),
        ("hello123\n", "Medium"),
        ("HELLO123\n", "Medium"),
        ("HelloWorld\n", "Medium"),
        ("Hel!23\n", "Strong"),
        ("hello\n", "Very Weak"),
        ("12345\n", "Very Weak"),
    ],
)
def test_password_strength(script_runner, input_text, expected):
    script_path = Path(__file__).parent / "password_strength.py"

    if not script_path.exists():
        pytest.skip("Solution file password_strength.py not found")

    runner = script_runner(script_path)
    result = runner.run(input_text=input_text)
    assert result.stdout == expected
