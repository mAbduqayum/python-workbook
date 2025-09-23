import re
import subprocess
import sys
from pathlib import Path
from typing import Tuple

import pytest


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

    def _validate_execution(self, stderr: str, return_code: int) -> None:
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

    def _clean_output(self, stdout: str) -> str:
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


class GradeReporter:
    """Handles grade calculation and reporting for test results."""

    GRADE_THRESHOLDS = [
        (97, "A+"),
        (93, "A"),
        (90, "A-"),
        (87, "B+"),
        (83, "B"),
        (80, "B-"),
        (77, "C+"),
        (73, "C"),
        (70, "C-"),
        (67, "D+"),
        (65, "D"),
    ]

    GRADE_MESSAGES = {
        90: "🎉 Excellent work!",
        80: "👍 Good job!",
        70: "📚 Keep studying!",
        0: "💪 More practice needed!",
    }

    def __init__(self, stats: dict) -> None:
        self.passed = len(stats.get("passed", []))
        self.failed = len(stats.get("failed", []))
        self.skipped = len(stats.get("skipped", []))
        self.error = len(stats.get("error", []))

    @property
    def total_tests(self) -> int:
        return self.passed + self.failed + self.skipped + self.error

    @property
    def possible_tests(self) -> int:
        return self.passed + self.failed + self.error

    def calculate_grade(self) -> Tuple[float, str]:
        """Calculate grade percentage and letter grade."""
        if self.possible_tests == 0:
            return 0.0, "N/A"

        percentage = (self.passed / self.possible_tests) * 100

        for threshold, letter in self.GRADE_THRESHOLDS:
            if percentage >= threshold:
                return percentage, letter

        return percentage, "F"

    def get_grade_message(self, percentage: float) -> str:
        """Get motivational message based on grade percentage."""
        for threshold in sorted(self.GRADE_MESSAGES.keys(), reverse=True):
            if percentage >= threshold:
                return self.GRADE_MESSAGES[threshold]
        return self.GRADE_MESSAGES[0]

    def print_report(self) -> None:
        """Print a comprehensive grade report."""
        grade_percentage, letter_grade = self.calculate_grade()

        print("\n" + "=" * 50)
        print("📊 FINAL GRADE REPORT")
        print("=" * 50)

        print(f"Total Tests: {self.total_tests}")
        print(f"Passed: {self.passed}")
        print(f"Failed: {self.failed}")
        print(f"Skipped: {self.skipped}")
        if self.error > 0:
            print(f"Errors: {self.error}")

        print()
        print(f"Grade: {grade_percentage:.1f}% ({letter_grade})")
        print(self.get_grade_message(grade_percentage))
        print("=" * 50)


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
