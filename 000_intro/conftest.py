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


def pytest_addoption(parser):
    """Add custom command line options."""
    parser.addoption(
        "--grade",
        action="store_true",
        default=False,
        help="Show grade report after running tests",
    )


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """Add grade report to terminal summary if --grade option is used."""
    if config.getoption("grade"):
        print_grade_report(terminalreporter, exitstatus)


def print_grade_report(terminalreporter, exitstatus):
    """Print a comprehensive grade report."""
    print("\n" + "=" * 50)
    print("📊 FINAL GRADE REPORT")
    print("=" * 50)

    # Get test results from terminalreporter stats
    stats = terminalreporter.stats

    passed = len(stats.get("passed", []))
    failed = len(stats.get("failed", []))
    skipped = len(stats.get("skipped", []))
    error = len(stats.get("error", []))

    total_tests = passed + failed + skipped + error

    # Calculate grade (excluding errors and skipped tests from total possible)
    possible_tests = passed + failed + error
    if possible_tests == 0:
        grade_percentage = 0
        letter_grade = "N/A"
    else:
        grade_percentage = (passed / possible_tests) * 100

        # Letter grade
        if grade_percentage >= 97:
            letter_grade = "A+"
        elif grade_percentage >= 93:
            letter_grade = "A"
        elif grade_percentage >= 90:
            letter_grade = "A-"
        elif grade_percentage >= 87:
            letter_grade = "B+"
        elif grade_percentage >= 83:
            letter_grade = "B"
        elif grade_percentage >= 80:
            letter_grade = "B-"
        elif grade_percentage >= 77:
            letter_grade = "C+"
        elif grade_percentage >= 73:
            letter_grade = "C"
        elif grade_percentage >= 70:
            letter_grade = "C-"
        elif grade_percentage >= 67:
            letter_grade = "D+"
        elif grade_percentage >= 65:
            letter_grade = "D"
        else:
            letter_grade = "F"

    print(f"Total Tests: {total_tests}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print(f"Skipped: {skipped}")
    if error > 0:
        print(f"Errors: {error}")
    print()
    print(f"Grade: {grade_percentage:.1f}% ({letter_grade})")

    # Grade interpretation
    if grade_percentage >= 90:
        print("🎉 Excellent work!")
    elif grade_percentage >= 80:
        print("👍 Good job!")
    elif grade_percentage >= 70:
        print("📚 Keep studying!")
    else:
        print("💪 More practice needed!")

    print("=" * 50)
