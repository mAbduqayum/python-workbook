import pytest

try:
    from element_lookup import load_elements, lookup_element
except ImportError:
    load_elements = None
    lookup_element = None


@pytest.mark.skipif(load_elements is None, reason="load_elements not implemented")
class TestLoadElements:
    def test_load_simple(self, tmp_path):
        test_file = tmp_path / "elements.txt"
        test_file.write_text("1 H Hydrogen\n2 He Helium\n", encoding="utf-8")

        result = load_elements(str(test_file))

        assert "by_number" in result
        assert "by_symbol" in result
        assert "by_name" in result
        assert result["by_number"]["1"] == "Hydrogen"
        assert result["by_symbol"]["h"] == "Hydrogen"
        assert result["by_name"]["hydrogen"] == "Hydrogen"

    def test_load_multiple_elements(self, tmp_path):
        test_file = tmp_path / "elements.txt"
        test_file.write_text("1 H Hydrogen\n6 C Carbon\n8 O Oxygen\n", encoding="utf-8")

        result = load_elements(str(test_file))

        assert len(result["by_number"]) == 3
        assert result["by_number"]["6"] == "Carbon"
        assert result["by_symbol"]["o"] == "Oxygen"

    def test_empty_file(self, tmp_path):
        test_file = tmp_path / "elements.txt"
        test_file.write_text("", encoding="utf-8")

        result = load_elements(str(test_file))

        assert result["by_number"] == {}
        assert result["by_symbol"] == {}
        assert result["by_name"] == {}


@pytest.mark.skipif(lookup_element is None, reason="lookup_element not implemented")
class TestLookupElement:
    def test_lookup_by_number(self, tmp_path):
        test_file = tmp_path / "elements.txt"
        test_file.write_text("1 H Hydrogen\n", encoding="utf-8")
        elements = load_elements(str(test_file))

        result = lookup_element(elements, "1")

        assert result == "Hydrogen"

    def test_lookup_by_symbol(self, tmp_path):
        test_file = tmp_path / "elements.txt"
        test_file.write_text("2 He Helium\n", encoding="utf-8")
        elements = load_elements(str(test_file))

        result = lookup_element(elements, "He")

        assert result == "Helium"

    def test_lookup_by_symbol_case_insensitive(self, tmp_path):
        test_file = tmp_path / "elements.txt"
        test_file.write_text("2 He Helium\n", encoding="utf-8")
        elements = load_elements(str(test_file))

        result = lookup_element(elements, "he")

        assert result == "Helium"

    def test_lookup_by_name(self, tmp_path):
        test_file = tmp_path / "elements.txt"
        test_file.write_text("6 C Carbon\n", encoding="utf-8")
        elements = load_elements(str(test_file))

        result = lookup_element(elements, "Carbon")

        assert result == "Carbon"

    def test_lookup_by_name_case_insensitive(self, tmp_path):
        test_file = tmp_path / "elements.txt"
        test_file.write_text("6 C Carbon\n", encoding="utf-8")
        elements = load_elements(str(test_file))

        result = lookup_element(elements, "carbon")

        assert result == "Carbon"

    def test_lookup_not_found(self, tmp_path):
        test_file = tmp_path / "elements.txt"
        test_file.write_text("1 H Hydrogen\n", encoding="utf-8")
        elements = load_elements(str(test_file))

        result = lookup_element(elements, "99")

        assert result is None

    def test_lookup_multiple_elements(self, tmp_path):
        test_file = tmp_path / "elements.txt"
        test_file.write_text(
            "1 H Hydrogen\n2 He Helium\n6 C Carbon\n", encoding="utf-8"
        )
        elements = load_elements(str(test_file))

        assert lookup_element(elements, "1") == "Hydrogen"
        assert lookup_element(elements, "He") == "Helium"
        assert lookup_element(elements, "carbon") == "Carbon"
