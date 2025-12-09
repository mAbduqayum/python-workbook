import pytest

try:
    from word_frequency import word_frequency, word_frequency2
except ImportError:
    word_frequency = None
    word_frequency2 = None


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

    def test_case_insensitive(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("Hello hello HELLO", encoding="utf-8")
        assert word_frequency(str(test_file)) == {"hello": 3}

    def test_repeated_word(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("test test test test", encoding="utf-8")
        assert word_frequency(str(test_file)) == {"test": 4}

    def test_punctuation_handling(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("Hello, world! Hello world.", encoding="utf-8")
        assert word_frequency(str(test_file)) == {"hello": 2, "world": 2}

    def test_mixed_punctuation_and_case(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("Python! python? PYTHON.", encoding="utf-8")
        assert word_frequency(str(test_file)) == {"python": 3}


@pytest.mark.skipif(word_frequency2 is None, reason="word_frequency2 not implemented")
class TestWordFrequency2:
    def test_simple_text(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("hello world\nhello python world\n", encoding="utf-8")
        result = word_frequency2(str(test_file))
        assert result == {"hello": 2, "world": 2, "python": 1}

    def test_single_word(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("hello", encoding="utf-8")
        assert word_frequency2(str(test_file)) == {"hello": 1}

    def test_empty_file(self, tmp_path):
        test_file = tmp_path / "empty.txt"
        test_file.write_text("", encoding="utf-8")
        assert word_frequency2(str(test_file)) == {}

    def test_case_insensitive(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("Hello hello HELLO", encoding="utf-8")
        assert word_frequency2(str(test_file)) == {"hello": 3}

    def test_repeated_word(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("test test test test", encoding="utf-8")
        assert word_frequency2(str(test_file)) == {"test": 4}

    def test_punctuation_handling(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("Hello, world! Hello world.", encoding="utf-8")
        assert word_frequency2(str(test_file)) == {"hello": 2, "world": 2}

    def test_mixed_punctuation_and_case(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("Python! python? PYTHON.", encoding="utf-8")
        assert word_frequency2(str(test_file)) == {"python": 3}
