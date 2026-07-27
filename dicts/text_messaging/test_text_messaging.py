try:
    from text_messaging import text_messaging
except ImportError:
    text_messaging = None


@pytest.mark.skipif(
    text_messaging is None, reason="text_messaging function not implemented"
)
def test_hi():
    assert text_messaging("HI") == "44444"


@pytest.mark.skipif(
    text_messaging is None, reason="text_messaging function not implemented"
)
def test_hello():
    assert text_messaging("HELLO") == "4433555555666"


@pytest.mark.skipif(
    text_messaging is None, reason="text_messaging function not implemented"
)
def test_with_space():
    assert text_messaging("HI THERE") == "4444408443377733"


@pytest.mark.skipif(
    text_messaging is None, reason="text_messaging function not implemented"
)
def test_with_punctuation():
    assert text_messaging("HI!") == "444441111"


@pytest.mark.skipif(
    text_messaging is None, reason="text_messaging function not implemented"
)
def test_single_char():
    assert text_messaging("A") == "2"


@pytest.mark.skipif(
    text_messaging is None, reason="text_messaging function not implemented"
)
def test_empty():
    assert text_messaging("") == ""


@pytest.mark.skipif(
    text_messaging is None, reason="text_messaging function not implemented"
)
def test_case_insensitive():
    assert text_messaging("hi") == text_messaging("HI")


@pytest.mark.skipif(
    text_messaging is None, reason="text_messaging function not implemented"
)
def test_with_period():
    assert text_messaging("OK.") == "666551"


@pytest.mark.skipif(
    text_messaging is None, reason="text_messaging function not implemented"
)
def test_same_key_letters():
    assert text_messaging("ABC") == "222222"
