import os

# pytest files one report per test *phase*, so a single passing test produces
# three: setup, call and teardown. Only the phase that settled the outcome is
# filed under a real category; the other two land under "". Counting just these
# four therefore counts each test exactly once, and keeps non-test entries such
# as "warnings" -- whose nodeid may be None -- out of the report entirely.
TEST_OUTCOMES = ("passed", "failed", "skipped", "error")


class GradeReporter:
    def __init__(self, stats: dict) -> None:
        self.file_stats = self._group_by_test_file(stats)

        file_statuses = [s["status"] for s in self.file_stats.values()]
        self.passed = file_statuses.count("passed")
        self.failed = file_statuses.count("failed")
        self.skipped = file_statuses.count("skipped")
        self.error = file_statuses.count("error")

    def _group_by_test_file(self, stats: dict) -> dict:
        """Group test results by test file, determining overall file status."""
        file_stats = {}

        for status, test_list in stats.items():
            if status not in TEST_OUTCOMES:
                continue
            for test_report in test_list:
                # nodeid looks like "intro/name_age/test_name_age.py::test_name_age[Farid-22]"
                test_file = test_report.nodeid.split("::")[0]

                if test_file not in file_stats:
                    file_stats[test_file] = {
                        "status": "passed",
                        "total_count": 0,
                    }

                file_stats[test_file]["total_count"] += 1

                # File status precedence: failed/error beat skipped, skipped beats passed
                if status in ["failed", "error"]:
                    file_stats[test_file]["status"] = status
                elif status == "skipped" and file_stats[test_file]["status"] not in [
                    "failed",
                    "error",
                ]:
                    file_stats[test_file]["status"] = "skipped"

        return file_stats

    @property
    def total_files(self) -> int:
        """How many test files ran. The grade is a fraction of these.

        Named for what it counts: ``passed`` and friends are per-file tallies,
        so this is a file count, not a test count.
        """
        return self.passed + self.failed + self.skipped + self.error

    def calculate_grade(self) -> float:
        if self.total_files == 0:
            return 0.0
        return (self.passed / self.total_files) * 100

    def print_report(self) -> None:
        grade_percentage = self.calculate_grade()

        print("\n" + "=" * 50)
        print("FINAL GRADE REPORT")
        print("=" * 50)

        print(f"Total Test Files: {self.total_files}")
        print(f"Passed: {self.passed}")
        print(f"Failed: {self.failed}")
        print(f"Skipped: {self.skipped}")
        if self.error > 0:
            print(f"Errors: {self.error}")

        total_individual_tests = sum(
            stats["total_count"] for stats in self.file_stats.values()
        )
        print(f"Total Individual Test Cases: {total_individual_tests}")

        print()
        print(f"Grade: {grade_percentage:.1f}%")
        print("=" * 50)

        if summary_file := os.getenv("GITHUB_STEP_SUMMARY"):
            with open(summary_file, "a") as f:
                f.write(
                    f"**Grade: {grade_percentage:.1f}%** ({self.passed}/{self.total_files} passed)\n\n"
                )
