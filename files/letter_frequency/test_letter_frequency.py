import pytest

try:
    from letter_frequency import letter_frequency
except ImportError:
    letter_frequency = None


@pytest.mark.skipif(letter_frequency is None, reason="letter_frequency not implemented")
class TestLetterFrequency:
    def test_simple_text(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("Hello", encoding="utf-8")

        result = letter_frequency(str(test_file))

        assert result == {"h": 1, "e": 1, "l": 2, "o": 1}

    def test_case_insensitive(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("AaBbCc", encoding="utf-8")

        result = letter_frequency(str(test_file))

        assert result == {"a": 2, "b": 2, "c": 2}

    def test_ignores_non_letters(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("a1b2c3!@#", encoding="utf-8")

        result = letter_frequency(str(test_file))

        assert result == {"a": 1, "b": 1, "c": 1}

    def test_multiline(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("abc\nabc\nabc\n", encoding="utf-8")

        result = letter_frequency(str(test_file))

        assert result == {"a": 3, "b": 3, "c": 3}

    def test_empty_file(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("", encoding="utf-8")

        result = letter_frequency(str(test_file))

        assert result == {}

    def test_no_letters(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("123 !@# 456", encoding="utf-8")

        result = letter_frequency(str(test_file))

        assert result == {}
