from pathlib import Path

import pytest


@pytest.mark.parametrize("name", ["Farid", "Gulnora", "Davron"])
def test_hello_name(script_runner, name):
    script_path = Path(__file__).parent / "hello_name.py"

    if not script_path.exists():
        pytest.skip("Solution file hello_name.py not found")

    runner = script_runner(script_path)
    stdout, stderr, return_code = runner.run(f"{name}\n")

    assert stdout == f"Enter your name: Hello {name}!"
