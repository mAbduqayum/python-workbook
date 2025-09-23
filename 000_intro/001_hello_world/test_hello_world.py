from pathlib import Path

import pytest


def test_hello_world(script_runner):
    script_path = Path(__file__).parent / "hello_world.py"

    if not script_path.exists():
        pytest.skip("Solution file hello_world.py not found")

    runner = script_runner(script_path)
    runner.run_and_check(expected_output="Hello, World!")
