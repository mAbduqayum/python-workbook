import pytest

try:
    from search_lines import search_lines
except ImportError:
    search_lines = None


@pytest.mark.skipif(search_lines is None, reason="search_lines not implemented")
class TestSearchLines:
    def test_find_multiple_matches(self, tmp_path):
        test_file = tmp_path / "code.txt"
        test_file.write_text(
            "def hello():\n    print('Hello')\ndef goodbye():\n    print('Goodbye')\n",
            encoding="utf-8",
        )
        result = search_lines(str(test_file), "def")
        assert result == [[1, "def hello():"], [3, "def goodbye():"]]

    def test_find_single_match(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("Line 1\nTarget line\nLine 3\n", encoding="utf-8")
        result = search_lines(str(test_file), "Target")
        assert result == [[2, "Target line"]]

    def test_no_matches(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("Line 1\nLine 2\nLine 3\n", encoding="utf-8")
        result = search_lines(str(test_file), "notfound")
        assert result == []

    def test_case_sensitive(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("Hello\nhello\nHELLO\n", encoding="utf-8")
        result = search_lines(str(test_file), "hello")
        assert result == [[2, "hello"]]

    def test_empty_file(self, tmp_path):
        test_file = tmp_path / "empty.txt"
        test_file.write_text("", encoding="utf-8")
        result = search_lines(str(test_file), "test")
        assert result == []
