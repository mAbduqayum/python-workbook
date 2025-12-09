import pytest

try:
    from word_frequency import word_frequency
except ImportError:
    word_frequency = None


@pytest.mark.skipif(word_frequency is None, reason="word_frequency not implemented")
class TestWordFrequency:
    def test_simple_text(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("hello world\nhello python world\n", encoding="utf-8")
        result = word_frequency(str(test_file))
        assert result == {"hello": 2, "world": 2, "python": 1}

    def test_single_word(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("hello", encoding="utf-8")
        assert word_frequency(str(test_file)) == {"hello": 1}

    def test_empty_file(self, tmp_path):
        test_file = tmp_path / "empty.txt"
        test_file.write_text("", encoding="utf-8")
        assert word_frequency(str(test_file)) == {}

    def test_case_sensitive(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("Hello hello HELLO", encoding="utf-8")
        assert word_frequency(str(test_file)) == {"Hello": 1, "hello": 1, "HELLO": 1}

    def test_repeated_word(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("test test test test", encoding="utf-8")
        assert word_frequency(str(test_file)) == {"test": 4}
