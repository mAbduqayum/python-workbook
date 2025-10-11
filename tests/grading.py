class GradeReporter:

    def __init__(self, stats: dict) -> None:
        # Group test results by test file
        self.file_stats = self._group_by_test_file(stats)

        # Count files instead of individual test cases
        self.passed = len([f for f, s in self.file_stats.items() if s['status'] == 'passed'])
        self.failed = len([f for f, s in self.file_stats.items() if s['status'] == 'failed'])
        self.skipped = len([f for f, s in self.file_stats.items() if s['status'] == 'skipped'])
        self.error = len([f for f, s in self.file_stats.items() if s['status'] == 'error'])

    def _group_by_test_file(self, stats: dict) -> dict:
        """Group test results by test file, determining overall file status."""
        file_stats = {}

        # Process all test results
        for status, test_list in stats.items():
            for test_report in test_list:
                # Extract test file path from test nodeid
                # Example nodeid: "000_intro/004_name_age/test_name_age.py::test_name_age[Farid-22]"
                nodeid = test_report.nodeid
                test_file = nodeid.split('::')[0]  # Get file part before ::

                if test_file not in file_stats:
                    file_stats[test_file] = {
                        'status': 'passed',  # Default to passed, will be overridden if needed
                        'passed_count': 0,
                        'failed_count': 0,
                        'skipped_count': 0,
                        'error_count': 0,
                        'total_count': 0
                    }

                # Count test cases per file for reporting
                count_key = f'{status}_count'
                if count_key in file_stats[test_file]:
                    file_stats[test_file][count_key] += 1
                else:
                    # Handle unknown status types by creating the key
                    file_stats[test_file][count_key] = 1
                file_stats[test_file]['total_count'] += 1

                # Update overall file status (failed/error takes precedence)
                if status in ['failed', 'error']:
                    file_stats[test_file]['status'] = status
                elif status == 'skipped' and file_stats[test_file]['status'] not in ['failed', 'error']:
                    file_stats[test_file]['status'] = 'skipped'
                # Only set to passed if no failures, errors, or skips
                elif (status == 'passed' and
                      file_stats[test_file]['status'] not in ['failed', 'error', 'skipped']):
                    file_stats[test_file]['status'] = 'passed'

        return file_stats

    @property
    def total_tests(self) -> int:
        return self.passed + self.failed + self.skipped + self.error

    @property
    def possible_tests(self) -> int:
        return self.passed + self.failed + self.error + self.skipped

    def calculate_grade(self) -> float:
        if self.possible_tests == 0:
            return 0.0
        return (self.passed / self.possible_tests) * 100


    def print_report(self) -> None:
        import os

        grade_percentage = self.calculate_grade()

        print("\n" + "=" * 50)
        print("📊 FINAL GRADE REPORT")
        print("=" * 50)

        print(f"Total Test Files: {self.total_tests}")
        print(f"Passed: {self.passed}")
        print(f"Failed: {self.failed}")
        print(f"Skipped: {self.skipped}")
        if self.error > 0:
            print(f"Errors: {self.error}")

        # Show individual test case counts for context
        total_individual_tests = sum(
            stats['total_count'] for stats in self.file_stats.values()
        )
        print(f"Total Individual Test Cases: {total_individual_tests}")

        print()
        print(f"Grade: {grade_percentage:.1f}%")
        print("=" * 50)

        # Write to GitHub Actions summary if in CI
        if summary_file := os.getenv('GITHUB_STEP_SUMMARY'):
            with open(summary_file, 'a') as f:
                f.write(f"**Grade: {grade_percentage:.1f}%** ({self.passed}/{self.possible_tests} passed)\n\n")
