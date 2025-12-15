import pytest

try:
    from element_sequences import ELEMENTS_LOWER, longest_element_sequence
except ImportError:
    longest_element_sequence = None
    ELEMENTS_LOWER = None


@pytest.mark.skipif(
    longest_element_sequence is None, reason="longest_element_sequence not implemented"
)
class TestElementSequences:
    def test_invalid_element(self):
        assert longest_element_sequence("NotAnElement") == []

    def test_molybdenum_sequence(self):
        # Molybdenum should have a longest sequence of at least 8 elements
        result = longest_element_sequence("Molybdenum")
        assert len(result) >= 8
        assert result[0] == "Molybdenum"

    def test_magnesium_sequence(self):
        # Magnesium should have a longest sequence of at least 8 elements
        result = longest_element_sequence("Magnesium")
        assert len(result) >= 8
        assert result[0] == "Magnesium"

    def test_case_insensitive(self):
        result1 = longest_element_sequence("molybdenum")
        result2 = longest_element_sequence("MOLYBDENUM")
        result3 = longest_element_sequence("Molybdenum")
        assert result1 == result2 == result3

    def test_sequence_validity(self):
        result = longest_element_sequence("Molybdenum")
        # Each element should start with the last letter of the previous
        for i in range(1, len(result)):
            prev_last = result[i - 1][-1].upper()
            curr_first = result[i][0].upper()
            assert prev_last == curr_first, f"{result[i - 1]} -> {result[i]}"

    def test_no_duplicates(self):
        result = longest_element_sequence("Molybdenum")
        assert len(result) == len(set(result))
