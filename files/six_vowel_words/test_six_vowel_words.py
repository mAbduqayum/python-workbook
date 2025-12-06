import pytest

try:
    from six_vowel_words import six_vowel_words
except ImportError:
    six_vowel_words = None


@pytest.mark.skipif(six_vowel_words is None, reason="six_vowel_words not implemented")
class TestSixVowelWords:
    def test_facetiously(self, tmp_path):
        test_file = tmp_path / "words.txt"
        test_file.write_text("facetiously\n", encoding="utf-8")

        result = six_vowel_words(str(test_file))

        assert result == ["facetiously"]

    def test_abstentiously(self, tmp_path):
        test_file = tmp_path / "words.txt"
        test_file.write_text("abstentiously\n", encoding="utf-8")

        result = six_vowel_words(str(test_file))

        assert result == ["abstentiously"]

    def test_multiple_valid_words(self, tmp_path):
        test_file = tmp_path / "words.txt"
        test_file.write_text(
            "facetiously\nabstentiously\nabstemiously\n", encoding="utf-8"
        )

        result = six_vowel_words(str(test_file))

        assert result == ["facetiously", "abstentiously", "abstemiously"]

    def test_mixed_valid_and_invalid(self, tmp_path):
        test_file = tmp_path / "words.txt"
        test_file.write_text("facetiously\nhello\nworld\n", encoding="utf-8")

        result = six_vowel_words(str(test_file))

        assert result == ["facetiously"]

    def test_no_valid_words(self, tmp_path):
        test_file = tmp_path / "words.txt"
        test_file.write_text("hello\nworld\npython\n", encoding="utf-8")

        result = six_vowel_words(str(test_file))

        assert result == []

    def test_case_insensitive(self, tmp_path):
        test_file = tmp_path / "words.txt"
        test_file.write_text("FacEtIoUsLy\n", encoding="utf-8")

        result = six_vowel_words(str(test_file))

        assert result == ["FacEtIoUsLy"]

    def test_empty_file(self, tmp_path):
        test_file = tmp_path / "words.txt"
        test_file.write_text("", encoding="utf-8")

        result = six_vowel_words(str(test_file))

        assert result == []

    def test_vowels_out_of_order(self, tmp_path):
        test_file = tmp_path / "words.txt"
        test_file.write_text("eiaouy\n", encoding="utf-8")

        result = six_vowel_words(str(test_file))

        assert result == []
