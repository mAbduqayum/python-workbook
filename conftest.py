import re
import subprocess
import sys
from pathlib import Path
from typing import NamedTuple

import pytest

from tests.grading import GradeReporter

_active_exercise_dir: str | None = None


def _evict_solutions_from(exercise_dir: Path) -> None:
    """Forget the solution modules imported while ``exercise_dir`` was active.

    Python caches imports by module name and never consults ``sys.path`` on a
    hit. Exercise names repeat across topics -- ``binary_search.py`` exists in
    both ``lists/`` and ``recursions/`` -- so a cached solution left in place
    is silently reused by the next exercise of the same name, whether or not
    that exercise has been solved.
    """
    directory = exercise_dir.resolve()
    for name, module in list(sys.modules.items()):
        file = getattr(module, "__file__", None)
        if not file:
            continue
        solution = Path(file)
        if solution.parent.resolve() != directory:
            continue
        if solution.name == "conftest.py" or solution.name.startswith("test_"):
            continue
        del sys.modules[name]


def _scope_to_exercise(exercise_dir: Path) -> None:
    """Make ``exercise_dir`` the only exercise directory imports can reach."""
    global _active_exercise_dir

    entry = str(exercise_dir)
    if entry == _active_exercise_dir:
        return
    if _active_exercise_dir is not None:
        if _active_exercise_dir in sys.path:
            sys.path.remove(_active_exercise_dir)
        _evict_solutions_from(Path(_active_exercise_dir))
    sys.path.insert(0, entry)
    _active_exercise_dir = entry


def pytest_pycollect_makemodule(module_path, parent, **kwargs):
    """Point imports at the exercise directory owning the test being collected.

    With ``--import-mode=importlib`` pytest does not add a test file's own
    directory to ``sys.path``. Many exercises import their solution as a
    sibling module (e.g. ``from chars_count import chars_count``), so we
    prepare both ``sys.path`` and ``sys.modules`` here, before the test module
    is imported. Every solution import in the suite happens at module level,
    so this is the only point at which the state has to be correct.
    """
    _scope_to_exercise(Path(module_path).parent)
    return None


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
            return RunResult(
                result.stdout.strip(), result.stderr.strip(), result.returncode
            )
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
