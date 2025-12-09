import pytest

try:
    from find_longest_word import find_longest_word
except ImportError:
    find_longest_word = None


@pytest.mark.skipif(
    find_longest_word is None, reason="find_longest_word not implemented"
)
class TestFindLongestWord:
    def test_multiple_lines(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text(
            "The quick brown fox\nPython programming is wonderful\n",
            encoding="utf-8",
        )
        assert find_longest_word(str(test_file)) == "programming"

    def test_single_word(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("Hello", encoding="utf-8")
        assert find_longest_word(str(test_file)) == "Hello"

    def test_same_length_returns_first(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("cat dog bat", encoding="utf-8")
        assert find_longest_word(str(test_file)) == "cat"

    def test_with_numbers(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("a bb ccc 12345", encoding="utf-8")
        assert find_longest_word(str(test_file)) == "12345"
