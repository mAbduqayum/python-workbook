import pytest

try:
    from remove_comments import remove_comments
except ImportError:
    remove_comments = None


@pytest.mark.skipif(remove_comments is None, reason="remove_comments not implemented")
class TestRemoveComments:
    def test_remove_comment_lines(self, tmp_path):
        input_file = tmp_path / "input.py"
        output_file = tmp_path / "output.py"
        input_file.write_text("# comment\nx = 1\n# another\ny = 2\n", encoding="utf-8")

        removed = remove_comments(str(input_file), str(output_file))

        assert removed == 2
        assert output_file.read_text(encoding="utf-8") == "x = 1\ny = 2\n"

    def test_indented_comments(self, tmp_path):
        input_file = tmp_path / "input.py"
        output_file = tmp_path / "output.py"
        input_file.write_text(
            "x = 1\n    # indented comment\ny = 2\n", encoding="utf-8"
        )

        removed = remove_comments(str(input_file), str(output_file))

        assert removed == 1
        assert output_file.read_text(encoding="utf-8") == "x = 1\ny = 2\n"

    def test_keep_inline_comments(self, tmp_path):
        input_file = tmp_path / "input.py"
        output_file = tmp_path / "output.py"
        input_file.write_text("x = 1  # inline comment\ny = 2\n", encoding="utf-8")

        removed = remove_comments(str(input_file), str(output_file))

        assert removed == 0
        assert (
            output_file.read_text(encoding="utf-8")
            == "x = 1  # inline comment\ny = 2\n"
        )

    def test_no_comments(self, tmp_path):
        input_file = tmp_path / "input.py"
        output_file = tmp_path / "output.py"
        input_file.write_text("x = 1\ny = 2\n", encoding="utf-8")

        removed = remove_comments(str(input_file), str(output_file))

        assert removed == 0
        assert output_file.read_text(encoding="utf-8") == "x = 1\ny = 2\n"

    def test_all_comments(self, tmp_path):
        input_file = tmp_path / "input.py"
        output_file = tmp_path / "output.py"
        input_file.write_text("# one\n# two\n# three\n", encoding="utf-8")

        removed = remove_comments(str(input_file), str(output_file))

        assert removed == 3
        assert output_file.read_text(encoding="utf-8") == ""

    def test_empty_file(self, tmp_path):
        input_file = tmp_path / "input.py"
        output_file = tmp_path / "output.py"
        input_file.write_text("", encoding="utf-8")

        removed = remove_comments(str(input_file), str(output_file))

        assert removed == 0
        assert output_file.read_text(encoding="utf-8") == ""
