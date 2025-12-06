from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "name,age",
    [
        ("Farid", "22"),
        ("Gulnora", "35"),
        ("Davron", "18"),
    ],
)
def test_name_age(script_runner, name, age):
    script_path = Path(__file__).parent / "name_age.py"

    if not script_path.exists():
        pytest.skip("Solution file name_age.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=f"{name}\n{age}\n",
        expected_output=f"Hello {name}, you are {age} years old.",
    )
