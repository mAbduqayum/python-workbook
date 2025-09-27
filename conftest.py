import re
import subprocess
import sys
from pathlib import Path
from typing import Tuple

import pytest

from tests.grading import GradeReporter


class ScriptRunner:
    """Helper class to run Python scripts and capture output."""

    DEFAULT_TIMEOUT = 3

    def __init__(self, script_path: str | Path) -> None:
        self.script_path = Path(script_path)

    def run(self, input_text: str = "") -> Tuple[str, str, int]:
        """Run the script with optional input and return (stdout, stderr, returncode)."""
        try:
            result = subprocess.run(
                [sys.executable, str(self.script_path)],
                input=input_text,
                text=True,
                capture_output=True,
                timeout=self.DEFAULT_TIMEOUT,
            )
            return result.stdout.strip(), result.stderr.strip(), result.returncode
        except subprocess.TimeoutExpired:
            return "", "Script timed out", 1

    @staticmethod
    def _validate_execution(stderr: str, return_code: int) -> None:
        """Validate that script execution was successful."""
        if return_code != 0:
            pytest.fail(f"Script failed with error: {stderr}")

    def run_and_check(self, input_text: str = "", expected_output: str = "") -> str:
        """Run script and assert expected output."""
        stdout, stderr, return_code = self.run(input_text)
        self._validate_execution(stderr, return_code)

        actual = stdout.strip()
        expected = expected_output.strip()

        assert actual == expected, f"Expected: {expected!r}, Got: {actual!r}"
        return stdout

    @staticmethod
    def _clean_output(stdout: str) -> str:
        """Remove input prompts and clean up whitespace from output."""
        cleaned_output = re.sub(r"Enter [^:]+:\s*", "", stdout.strip())
        return "\n".join(
            line.strip() for line in cleaned_output.split("\n") if line.strip()
        )

    def run_and_check_output_only(
        self, input_text: str = "", expected_output: str = ""
    ) -> str:
        """Run script and assert expected output, filtering out input prompts."""
        stdout, stderr, return_code = self.run(input_text)
        self._validate_execution(stderr, return_code)

        actual_output = self._clean_output(stdout)

        assert actual_output == expected_output, (
            f"Expected: {expected_output!r}, Got: {actual_output!r}"
        )
        return stdout


@pytest.fixture
def script_runner():
    """Fixture to provide ScriptRunner functionality."""
    return ScriptRunner


def pytest_addoption(parser):
    """Add custom command line options."""
    parser.addoption(
        "--no-grade",
        action="store_true",
        default=False,
        help="Disable grade report after running tests",
    )


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """Add grade report to terminal summary unless disabled."""
    if not config.getoption("no_grade"):
        reporter = GradeReporter(terminalreporter.stats)
        reporter.print_report()
