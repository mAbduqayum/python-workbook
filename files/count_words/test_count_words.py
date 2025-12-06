import pytest

try:
    from count_words import count_words
except ImportError:
    count_words = None


@pytest.mark.skipif(count_words is None, reason="count_words not implemented")
class TestCountWords:
    def test_simple_text(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("Hello world\nThis is a test file\n", encoding="utf-8")
        assert count_words(str(test_file)) == 7

    def test_single_word(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("Hello", encoding="utf-8")
        assert count_words(str(test_file)) == 1

    def test_empty_file(self, tmp_path):
        test_file = tmp_path / "empty.txt"
        test_file.write_text("", encoding="utf-8")
        assert count_words(str(test_file)) == 0

    def test_multiple_spaces(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("Hello    world   test", encoding="utf-8")
        assert count_words(str(test_file)) == 3

    def test_only_whitespace(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("   \n\n   \t   ", encoding="utf-8")
        assert count_words(str(test_file)) == 0
