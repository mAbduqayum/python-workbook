import pytest

try:
    from vocabulary_size import vocabulary_size
except ImportError:
    vocabulary_size = None

pytestmark = pytest.mark.skipif(
    vocabulary_size is None, reason="vocabulary_size not implemented"
)


class TestVocabularySize:
    def test_repeated_words(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("The cat and the hat\nThe end\n", encoding="utf-8")
        assert vocabulary_size(str(test_file)) == 5

    def test_all_different(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("one two three", encoding="utf-8")
        assert vocabulary_size(str(test_file)) == 3

    def test_case_ignored(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("Go go GO", encoding="utf-8")
        assert vocabulary_size(str(test_file)) == 1

    def test_repeats_across_lines(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("red blue\nblue green\ngreen red\n", encoding="utf-8")
        assert vocabulary_size(str(test_file)) == 3

    def test_extra_whitespace(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("  hello \t world\n\n  hello  ", encoding="utf-8")
        assert vocabulary_size(str(test_file)) == 2

    def test_empty_file(self, tmp_path):
        test_file = tmp_path / "empty.txt"
        test_file.write_text("", encoding="utf-8")
        assert vocabulary_size(str(test_file)) == 0
