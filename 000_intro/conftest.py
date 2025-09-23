import subprocess
import sys
from pathlib import Path

import pytest


class ScriptRunner:
    """Helper class to run Python scripts and capture output."""

    def __init__(self, script_path) -> None:
        self.script_path = Path(script_path)

    def run(self, input_text=""):
        """Run the script with optional input and return stdout."""
        try:
            result = subprocess.run(
                [sys.executable, str(self.script_path)],
                input=input_text,
                text=True,
                capture_output=True,
                timeout=3,
            )
            return result.stdout.strip(), result.stderr.strip(), result.returncode
        except subprocess.TimeoutExpired:
            return "", "Script timed out", 1

    def run_and_check(self, input_text="", expected_output=""):
        """Run script and assert expected output."""
        stdout, stderr, return_code = self.run(input_text)

        if return_code != 0:
            pytest.fail(f"Script failed with error: {stderr}")

        # Normalize whitespace for comparison
        actual = stdout.strip()
        expected = expected_output.strip()

        assert actual == expected, f"Expected: {expected!r}, Got: {actual!r}"
        return stdout

    def run_and_check_output_only(self, input_text="", expected_output=""):
        """Run script and assert expected output, filtering out input prompts."""
        stdout, stderr, return_code = self.run(input_text)

        if return_code != 0:
            pytest.fail(f"Script failed with error: {stderr}")

        # Extract only the output lines (filter out input prompts)
        import re

        # Remove all "Enter [something]: " prompts
        cleaned_output = re.sub(r"Enter [^:]+:\s*", "", stdout.strip())

        # Clean up any extra whitespace
        actual_output = "\n".join(
            line.strip() for line in cleaned_output.split("\n") if line.strip()
        )

        assert actual_output == expected_output, (
            f"Expected: {expected_output!r}, Got: {actual_output!r}"
        )
        return stdout


@pytest.fixture
def script_runner():
    """Fixture to provide ScriptRunner functionality."""
    return ScriptRunner
