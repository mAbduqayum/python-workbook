import pytest

try:
    from read_file_content import read_file_content
except ImportError:
    read_file_content = None


@pytest.mark.skipif(
    read_file_content is None, reason="read_file_content not implemented"
)
class TestReadFileContent:
    def test_simple_content(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("Hello, World!", encoding="utf-8")
        assert read_file_content(str(test_file)) == "Hello, World!"

    def test_multiline_content(self, tmp_path):
        test_file = tmp_path / "test.txt"
        content = "Line 1\nLine 2\nLine 3"
        test_file.write_text(content, encoding="utf-8")
        assert read_file_content(str(test_file)) == content

    def test_empty_file(self, tmp_path):
        test_file = tmp_path / "empty.txt"
        test_file.write_text("", encoding="utf-8")
        assert read_file_content(str(test_file)) == ""

    def test_unicode_content(self, tmp_path):
        test_file = tmp_path / "unicode.txt"
        content = "Hello\nWorld"
        test_file.write_text(content, encoding="utf-8")
        assert read_file_content(str(test_file)) == content
