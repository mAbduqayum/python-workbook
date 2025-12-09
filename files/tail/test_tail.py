import pytest

try:
    from tail import tail
except ImportError:
    tail = None


@pytest.mark.skipif(tail is None, reason="tail not implemented")
class TestTail:
    def test_last_three_lines(self, tmp_path, capsys):
        test_file = tmp_path / "test.txt"
        test_file.write_text(
            "Line 1\nLine 2\nLine 3\nLine 4\nLine 5\n", encoding="utf-8"
        )
        tail(str(test_file), 3)
        captured = capsys.readouterr()
        assert captured.out == "Line 3\nLine 4\nLine 5\n"

    def test_default_ten_lines(self, tmp_path, capsys):
        test_file = tmp_path / "test.txt"
        content = "\n".join(f"Line {i}" for i in range(1, 16)) + "\n"
        test_file.write_text(content, encoding="utf-8")
        tail(str(test_file))
        captured = capsys.readouterr()
        lines = captured.out.strip().split("\n")
        assert len(lines) == 10
        assert lines[0] == "Line 6"
        assert lines[9] == "Line 15"

    def test_fewer_lines_than_requested(self, tmp_path, capsys):
        test_file = tmp_path / "test.txt"
        test_file.write_text("Line 1\nLine 2\n", encoding="utf-8")
        tail(str(test_file), 5)
        captured = capsys.readouterr()
        assert captured.out == "Line 1\nLine 2\n"

    def test_empty_file(self, tmp_path, capsys):
        test_file = tmp_path / "empty.txt"
        test_file.write_text("", encoding="utf-8")
        tail(str(test_file), 3)
        captured = capsys.readouterr()
        assert captured.out == ""

    def test_single_line(self, tmp_path, capsys):
        test_file = tmp_path / "test.txt"
        test_file.write_text("Only line\n", encoding="utf-8")
        tail(str(test_file), 1)
        captured = capsys.readouterr()
        assert captured.out == "Only line\n"
