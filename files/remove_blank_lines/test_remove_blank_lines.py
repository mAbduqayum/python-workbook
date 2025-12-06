import pytest

try:
    from remove_blank_lines import remove_blank_lines
except ImportError:
    remove_blank_lines = None


@pytest.mark.skipif(
    remove_blank_lines is None, reason="remove_blank_lines not implemented"
)
class TestRemoveBlankLines:
    def test_remove_blank_lines(self, tmp_path):
        input_file = tmp_path / "input.txt"
        output_file = tmp_path / "output.txt"
        input_file.write_text("Line 1\n\nLine 2\n   \nLine 3\n", encoding="utf-8")

        removed = remove_blank_lines(str(input_file), str(output_file))

        assert removed == 2
        assert output_file.read_text(encoding="utf-8") == "Line 1\nLine 2\nLine 3\n"

    def test_no_blank_lines(self, tmp_path):
        input_file = tmp_path / "input.txt"
        output_file = tmp_path / "output.txt"
        input_file.write_text("Line 1\nLine 2\nLine 3\n", encoding="utf-8")

        removed = remove_blank_lines(str(input_file), str(output_file))

        assert removed == 0
        assert output_file.read_text(encoding="utf-8") == "Line 1\nLine 2\nLine 3\n"

    def test_all_blank_lines(self, tmp_path):
        input_file = tmp_path / "input.txt"
        output_file = tmp_path / "output.txt"
        input_file.write_text("\n\n   \n\t\n", encoding="utf-8")

        removed = remove_blank_lines(str(input_file), str(output_file))

        assert removed == 4
        assert output_file.read_text(encoding="utf-8") == ""

    def test_empty_file(self, tmp_path):
        input_file = tmp_path / "input.txt"
        output_file = tmp_path / "output.txt"
        input_file.write_text("", encoding="utf-8")

        removed = remove_blank_lines(str(input_file), str(output_file))

        assert removed == 0
        assert output_file.read_text(encoding="utf-8") == ""
