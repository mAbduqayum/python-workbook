import pytest

try:
    from redact_text import redact_text
except ImportError:
    redact_text = None


@pytest.mark.skipif(redact_text is None, reason="redact_text not implemented")
class TestRedactText:
    def test_simple_redaction(self, tmp_path):
        words_file = tmp_path / "words.txt"
        input_file = tmp_path / "input.txt"
        output_file = tmp_path / "output.txt"
        words_file.write_text("secret\n", encoding="utf-8")
        input_file.write_text("This is secret.\n", encoding="utf-8")

        count = redact_text(str(input_file), str(words_file), str(output_file))

        assert count == 1
        assert output_file.read_text(encoding="utf-8") == "This is ******.\n"

    def test_case_insensitive(self, tmp_path):
        words_file = tmp_path / "words.txt"
        input_file = tmp_path / "input.txt"
        output_file = tmp_path / "output.txt"
        words_file.write_text("secret\n", encoding="utf-8")
        input_file.write_text("SECRET Secret secret\n", encoding="utf-8")

        count = redact_text(str(input_file), str(words_file), str(output_file))

        assert count == 3
        assert output_file.read_text(encoding="utf-8") == "****** ****** ******\n"

    def test_multiple_words(self, tmp_path):
        words_file = tmp_path / "words.txt"
        input_file = tmp_path / "input.txt"
        output_file = tmp_path / "output.txt"
        words_file.write_text("secret\npassword\n", encoding="utf-8")
        input_file.write_text("The secret password is here.\n", encoding="utf-8")

        count = redact_text(str(input_file), str(words_file), str(output_file))

        assert count == 2
        assert (
            output_file.read_text(encoding="utf-8") == "The ****** ******** is here.\n"
        )

    def test_no_redaction(self, tmp_path):
        words_file = tmp_path / "words.txt"
        input_file = tmp_path / "input.txt"
        output_file = tmp_path / "output.txt"
        words_file.write_text("secret\n", encoding="utf-8")
        input_file.write_text("This is public.\n", encoding="utf-8")

        count = redact_text(str(input_file), str(words_file), str(output_file))

        assert count == 0
        assert output_file.read_text(encoding="utf-8") == "This is public.\n"

    def test_whole_word_only(self, tmp_path):
        words_file = tmp_path / "words.txt"
        input_file = tmp_path / "input.txt"
        output_file = tmp_path / "output.txt"
        words_file.write_text("pass\n", encoding="utf-8")
        input_file.write_text("pass the password\n", encoding="utf-8")

        count = redact_text(str(input_file), str(words_file), str(output_file))

        assert count == 1
        assert output_file.read_text(encoding="utf-8") == "**** the password\n"

    def test_multiline(self, tmp_path):
        words_file = tmp_path / "words.txt"
        input_file = tmp_path / "input.txt"
        output_file = tmp_path / "output.txt"
        words_file.write_text("secret\n", encoding="utf-8")
        input_file.write_text("Line 1 secret\nLine 2 secret\n", encoding="utf-8")

        count = redact_text(str(input_file), str(words_file), str(output_file))

        assert count == 2
        assert (
            output_file.read_text(encoding="utf-8") == "Line 1 ******\nLine 2 ******\n"
        )

    def test_empty_text(self, tmp_path):
        words_file = tmp_path / "words.txt"
        input_file = tmp_path / "input.txt"
        output_file = tmp_path / "output.txt"
        words_file.write_text("secret\n", encoding="utf-8")
        input_file.write_text("", encoding="utf-8")

        count = redact_text(str(input_file), str(words_file), str(output_file))

        assert count == 0
        assert output_file.read_text(encoding="utf-8") == ""
