from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "name",
    [
        "Farid",
        "Gulnora",
        "Davron",
    ],
)
def test_hello_name(script_runner, name):
    script_path = Path(__file__).parent / "hello_name.py"

    if not script_path.exists():
        pytest.skip("Solution file hello_name.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=f"{name}\n", expected_output=f"Hello {name}!"
    )
