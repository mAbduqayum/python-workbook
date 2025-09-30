from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "message, shift, expected_output",
    [
        ("HELLO", "3", "KHOOR"),
        ("xyz", "3", "abc"),
        ("ABC", "1", "BCD"),
        ("XYZ", "3", "ABC"),
        ("Hello World", "5", "Mjqqt Btwqi"),
        ("abc", "-3", "xyz"),
    ],
)
def test_caesar_cipher(script_runner, message, shift, expected_output):
    script_path = Path(__file__).parent / "caesar_cipher.py"

    if not script_path.exists():
        pytest.skip("Solution file caesar_cipher.py not found")

    runner = script_runner(script_path)
    result = runner.run(input_text=f"{message}\n{shift}\n")
    
    assert expected_output in result.stdout
