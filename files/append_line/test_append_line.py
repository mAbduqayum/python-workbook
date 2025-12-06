import pytest

try:
    from append_line import append_line
except ImportError:
    append_line = None


@pytest.mark.skipif(append_line is None, reason="append_line not implemented")
class TestAppendLine:
    def test_append_to_existing(self, tmp_path):
        test_file = tmp_path / "log.txt"
        test_file.write_text("Entry 1\n", encoding="utf-8")
        append_line(str(test_file), "Entry 2")
        assert test_file.read_text(encoding="utf-8") == "Entry 1\nEntry 2\n"

    def test_append_multiple(self, tmp_path):
        test_file = tmp_path / "log.txt"
        test_file.write_text("", encoding="utf-8")
        append_line(str(test_file), "First")
        append_line(str(test_file), "Second")
        append_line(str(test_file), "Third")
        assert test_file.read_text(encoding="utf-8") == "First\nSecond\nThird\n"

    def test_creates_new_file(self, tmp_path):
        test_file = tmp_path / "new.txt"
        append_line(str(test_file), "Hello")
        assert test_file.read_text(encoding="utf-8") == "Hello\n"

    def test_append_empty_string(self, tmp_path):
        test_file = tmp_path / "log.txt"
        test_file.write_text("Start\n", encoding="utf-8")
        append_line(str(test_file), "")
        assert test_file.read_text(encoding="utf-8") == "Start\n\n"
