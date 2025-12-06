import pytest

try:
    from spell_checker import spell_checker
except ImportError:
    spell_checker = None


@pytest.mark.skipif(spell_checker is None, reason="spell_checker not implemented")
class TestSpellChecker:
    def test_simple_misspelled(self, tmp_path):
        dict_file = tmp_path / "dict.txt"
        text_file = tmp_path / "text.txt"
        dict_file.write_text("hello\nworld\n", encoding="utf-8")
        text_file.write_text("hello wrld\n", encoding="utf-8")

        result = spell_checker(str(text_file), str(dict_file))

        assert result == ["wrld"]

    def test_case_insensitive(self, tmp_path):
        dict_file = tmp_path / "dict.txt"
        text_file = tmp_path / "text.txt"
        dict_file.write_text("hello\nworld\n", encoding="utf-8")
        text_file.write_text("HELLO World\n", encoding="utf-8")

        result = spell_checker(str(text_file), str(dict_file))

        assert result == []

    def test_punctuation(self, tmp_path):
        dict_file = tmp_path / "dict.txt"
        text_file = tmp_path / "text.txt"
        dict_file.write_text("hello\nworld\n", encoding="utf-8")
        text_file.write_text("Hello, world!\n", encoding="utf-8")

        result = spell_checker(str(text_file), str(dict_file))

        assert result == []

    def test_multiple_misspelled(self, tmp_path):
        dict_file = tmp_path / "dict.txt"
        text_file = tmp_path / "text.txt"
        dict_file.write_text("hello\nworld\n", encoding="utf-8")
        text_file.write_text("helo wrld xyz\n", encoding="utf-8")

        result = spell_checker(str(text_file), str(dict_file))

        assert result == ["helo", "wrld", "xyz"]

    def test_no_duplicates(self, tmp_path):
        dict_file = tmp_path / "dict.txt"
        text_file = tmp_path / "text.txt"
        dict_file.write_text("hello\nworld\n", encoding="utf-8")
        text_file.write_text("xyz xyz xyz\n", encoding="utf-8")

        result = spell_checker(str(text_file), str(dict_file))

        assert result == ["xyz"]

    def test_all_correct(self, tmp_path):
        dict_file = tmp_path / "dict.txt"
        text_file = tmp_path / "text.txt"
        dict_file.write_text("hello\nworld\n", encoding="utf-8")
        text_file.write_text("hello world\n", encoding="utf-8")

        result = spell_checker(str(text_file), str(dict_file))

        assert result == []

    def test_empty_text(self, tmp_path):
        dict_file = tmp_path / "dict.txt"
        text_file = tmp_path / "text.txt"
        dict_file.write_text("hello\nworld\n", encoding="utf-8")
        text_file.write_text("", encoding="utf-8")

        result = spell_checker(str(text_file), str(dict_file))

        assert result == []
