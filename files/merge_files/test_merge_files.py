import pytest

try:
    from merge_files import merge_files
except ImportError:
    merge_files = None


@pytest.mark.skipif(merge_files is None, reason="merge_files not implemented")
class TestMergeFiles:
    def test_merge_three_files(self, tmp_path):
        file1 = tmp_path / "file1.txt"
        file2 = tmp_path / "file2.txt"
        file3 = tmp_path / "file3.txt"
        output = tmp_path / "merged.txt"

        file1.write_text("Content 1\n", encoding="utf-8")
        file2.write_text("Content 2\n", encoding="utf-8")
        file3.write_text("Content 3\n", encoding="utf-8")

        merge_files([str(file1), str(file2), str(file3)], str(output))

        assert output.read_text(encoding="utf-8") == "Content 1\nContent 2\nContent 3\n"

    def test_merge_single_file(self, tmp_path):
        file1 = tmp_path / "file1.txt"
        output = tmp_path / "merged.txt"

        file1.write_text("Only content\n", encoding="utf-8")

        merge_files([str(file1)], str(output))

        assert output.read_text(encoding="utf-8") == "Only content\n"

    def test_merge_empty_list(self, tmp_path):
        output = tmp_path / "merged.txt"

        merge_files([], str(output))

        assert output.read_text(encoding="utf-8") == ""

    def test_merge_without_trailing_newlines(self, tmp_path):
        file1 = tmp_path / "file1.txt"
        file2 = tmp_path / "file2.txt"
        output = tmp_path / "merged.txt"

        file1.write_text("First", encoding="utf-8")
        file2.write_text("Second", encoding="utf-8")

        merge_files([str(file1), str(file2)], str(output))

        assert output.read_text(encoding="utf-8") == "FirstSecond"

    def test_merge_with_empty_file(self, tmp_path):
        file1 = tmp_path / "file1.txt"
        file2 = tmp_path / "file2.txt"
        output = tmp_path / "merged.txt"

        file1.write_text("Content\n", encoding="utf-8")
        file2.write_text("", encoding="utf-8")

        merge_files([str(file1), str(file2)], str(output))

        assert output.read_text(encoding="utf-8") == "Content\n"
