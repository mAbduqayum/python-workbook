class GradeReporter:
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
        return self.passed + self.failed + self.error + self.skipped

    def calculate_grade(self) -> float:
        if self.possible_tests == 0:
            return 0.0
        return (self.passed / self.possible_tests) * 100

    def get_grade_message(self, percentage: float) -> str:
        for threshold in sorted(self.GRADE_MESSAGES.keys(), reverse=True):
            if percentage >= threshold:
                return self.GRADE_MESSAGES[threshold]
        return self.GRADE_MESSAGES[0]

    def print_report(self) -> None:
        grade_percentage = self.calculate_grade()

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
        print(f"Grade: {grade_percentage:.1f}%")
        print(self.get_grade_message(grade_percentage))
        print("=" * 50)
