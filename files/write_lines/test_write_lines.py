import pytest

try:
    from write_lines import write_lines
except ImportError:
    write_lines = None


@pytest.mark.skipif(write_lines is None, reason="write_lines not implemented")
class TestWriteLines:
    def test_write_three_lines(self, tmp_path):
        test_file = tmp_path / "output.txt"
        write_lines(str(test_file), ["apple", "banana", "cherry"])
        assert test_file.read_text(encoding="utf-8") == "apple\nbanana\ncherry\n"

    def test_write_single_line(self, tmp_path):
        test_file = tmp_path / "output.txt"
        write_lines(str(test_file), ["hello"])
        assert test_file.read_text(encoding="utf-8") == "hello\n"

    def test_write_empty_list(self, tmp_path):
        test_file = tmp_path / "output.txt"
        write_lines(str(test_file), [])
        assert test_file.read_text(encoding="utf-8") == ""

    def test_overwrites_existing(self, tmp_path):
        test_file = tmp_path / "output.txt"
        test_file.write_text("old content", encoding="utf-8")
        write_lines(str(test_file), ["new"])
        assert test_file.read_text(encoding="utf-8") == "new\n"
