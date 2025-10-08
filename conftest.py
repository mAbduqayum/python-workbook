import re
import subprocess
import sys
from pathlib import Path
from typing import NamedTuple

import pytest

from tests.grading import GradeReporter


class RunResult(NamedTuple):
    """Result of running a script."""
    stdout: str
    stderr: str
    returncode: int


class ScriptRunner:
    """Helper class to run Python scripts and capture output."""

    DEFAULT_TIMEOUT = 3

    def __init__(self, script_path: str | Path) -> None:
        self.script_path = Path(script_path)

    def run(self, input_text: str = "") -> RunResult:
        """Run the script with optional input and return RunResult with stdout, stderr, returncode."""
        try:
            result = subprocess.run(
                [sys.executable, str(self.script_path)],
                input=input_text,
                text=True,
                capture_output=True,
                timeout=self.DEFAULT_TIMEOUT,
            )
            return RunResult(result.stdout.strip(), result.stderr.strip(), result.returncode)
        except subprocess.TimeoutExpired:
            return RunResult("", "Script timed out", 1)

    @staticmethod
    def _validate_execution(stderr: str, return_code: int) -> None:
        """Validate that script execution was successful."""
        if return_code != 0:
            pytest.fail(f"Script failed with error: {stderr}")

    def run_and_check(self, input_text: str = "", expected_output: str = "") -> str:
        """Run script and assert expected output."""
        result = self.run(input_text)
        self._validate_execution(result.stderr, result.returncode)

        actual = result.stdout.strip()
        expected = expected_output.strip()

        assert actual == expected, f"Expected: {expected!r}, Got: {actual!r}"
        return result.stdout

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
        result = self.run(input_text)
        self._validate_execution(result.stderr, result.returncode)

        actual_output = self._clean_output(result.stdout)

        assert actual_output == expected_output, (
            f"Expected: {expected_output!r}, Got: {actual_output!r}"
        )
        return result.stdout


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
