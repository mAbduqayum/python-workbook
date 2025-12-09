import pytest

try:
    from count_lines import count_lines
except ImportError:
    count_lines = None


@pytest.mark.skipif(count_lines is None, reason="count_lines not implemented")
class TestCountLines:
    def test_three_lines(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("Line 1\nLine 2\nLine 3\n", encoding="utf-8")
        assert count_lines(str(test_file)) == 3

    def test_single_line(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("Hello", encoding="utf-8")
        assert count_lines(str(test_file)) == 1

    def test_empty_file(self, tmp_path):
        test_file = tmp_path / "empty.txt"
        test_file.write_text("", encoding="utf-8")
        assert count_lines(str(test_file)) == 0

    def test_multiple_lines_no_trailing_newline(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("Line 1\nLine 2\nLine 3", encoding="utf-8")
        assert count_lines(str(test_file)) == 3
