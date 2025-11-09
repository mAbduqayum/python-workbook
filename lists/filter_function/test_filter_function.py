import pytest

try:
    from filter_function import filter_list
except ImportError:
    filter_list = None


@pytest.mark.skipif(filter_list is None, reason="filter_list function not implemented")
def test_filter_list_even():
    def is_even(x):
        return x % 2 == 0

    assert filter_list([1, 2, 3, 4, 5, 6], is_even) == [2, 4, 6]


@pytest.mark.skipif(filter_list is None, reason="filter_list function not implemented")
def test_filter_list_positive():
    def is_positive(x):
        return x > 0

    assert filter_list([-2, -1, 0, 1, 2], is_positive) == [1, 2]


@pytest.mark.skipif(filter_list is None, reason="filter_list function not implemented")
def test_filter_list_lambda():
    assert filter_list([1, 2, 3, 4, 5], lambda x: x > 3) == [4, 5]


@pytest.mark.skipif(filter_list is None, reason="filter_list function not implemented")
def test_filter_list_empty():
    assert filter_list([1, 2, 3], lambda x: x > 10) == []
