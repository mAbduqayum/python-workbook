import pytest

try:
    from find_repeated_words import find_repeated_words
except ImportError:
    find_repeated_words = None


@pytest.mark.skipif(
    find_repeated_words is None, reason="find_repeated_words not implemented"
)
class TestFindRepeatedWords:
    def test_simple_repeat(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("the the quick fox\n", encoding="utf-8")

        result = find_repeated_words(str(test_file))

        assert result == [[1, "the"]]

    def test_case_insensitive(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("The the quick fox\n", encoding="utf-8")

        result = find_repeated_words(str(test_file))

        assert result == [[1, "the"]]

    def test_multiple_repeats(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("the the fox fox\n", encoding="utf-8")

        result = find_repeated_words(str(test_file))

        assert result == [[1, "the"], [1, "fox"]]

    def test_across_lines(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("the quick\nquick fox\n", encoding="utf-8")

        result = find_repeated_words(str(test_file))

        assert result == [[2, "quick"]]

    def test_no_repeats(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("the quick brown fox\n", encoding="utf-8")

        result = find_repeated_words(str(test_file))

        assert result == []

    def test_empty_file(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("", encoding="utf-8")

        result = find_repeated_words(str(test_file))

        assert result == []

    def test_with_punctuation(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("Hello, hello! World world.\n", encoding="utf-8")

        result = find_repeated_words(str(test_file))

        assert result == [[1, "hello"], [1, "world"]]
