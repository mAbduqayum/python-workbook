import pytest

try:
    from find_missing_comments import find_missing_comments
except ImportError:
    find_missing_comments = None


@pytest.mark.skipif(
    find_missing_comments is None, reason="find_missing_comments not implemented"
)
class TestFindMissingComments:
    def test_function_with_comment(self, tmp_path):
        test_file = tmp_path / "test.py"
        test_file.write_text("# Comment\ndef foo():\n    pass\n", encoding="utf-8")

        result = find_missing_comments(str(test_file))

        assert result == []

    def test_function_without_comment(self, tmp_path):
        test_file = tmp_path / "test.py"
        test_file.write_text("def foo():\n    pass\n", encoding="utf-8")

        result = find_missing_comments(str(test_file))

        assert result == [[1, "foo"]]

    def test_mixed_functions(self, tmp_path):
        test_file = tmp_path / "test.py"
        test_file.write_text(
            "# Good\ndef good():\n    pass\n\ndef bad():\n    pass\n",
            encoding="utf-8",
        )

        result = find_missing_comments(str(test_file))

        assert result == [[5, "bad"]]

    def test_inline_comment(self, tmp_path):
        test_file = tmp_path / "test.py"
        test_file.write_text(
            "x = 1  # not a function comment\ndef foo():\n    pass\n", encoding="utf-8"
        )

        result = find_missing_comments(str(test_file))

        assert result == []

    def test_empty_lines_before_function(self, tmp_path):
        test_file = tmp_path / "test.py"
        test_file.write_text("# Comment\n\n\ndef foo():\n    pass\n", encoding="utf-8")

        result = find_missing_comments(str(test_file))

        assert result == []

    def test_multiple_missing(self, tmp_path):
        test_file = tmp_path / "test.py"
        test_file.write_text(
            "def foo():\n    pass\n\ndef bar():\n    pass\n", encoding="utf-8"
        )

        result = find_missing_comments(str(test_file))

        assert result == [[1, "foo"], [4, "bar"]]

    def test_function_with_parameters(self, tmp_path):
        test_file = tmp_path / "test.py"
        test_file.write_text("def foo(x, y, z):\n    pass\n", encoding="utf-8")

        result = find_missing_comments(str(test_file))

        assert result == [[1, "foo"]]

    def test_empty_file(self, tmp_path):
        test_file = tmp_path / "test.py"
        test_file.write_text("", encoding="utf-8")

        result = find_missing_comments(str(test_file))

        assert result == []
