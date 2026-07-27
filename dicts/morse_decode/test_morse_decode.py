try:
    from morse_decode import morse_decode
except ImportError:
    morse_decode = None


@pytest.mark.skipif(
    morse_decode is None, reason="morse_decode function not implemented"
)
def test_sos():
    assert morse_decode("... --- ...") == "SOS"


@pytest.mark.skipif(
    morse_decode is None, reason="morse_decode function not implemented"
)
def test_with_words():
    assert morse_decode(".... .. / - .... . .-. .") == "HI THERE"


@pytest.mark.skipif(
    morse_decode is None, reason="morse_decode function not implemented"
)
def test_numbers():
    assert morse_decode(".---- ..--- ...--") == "123"


@pytest.mark.skipif(
    morse_decode is None, reason="morse_decode function not implemented"
)
def test_empty():
    assert morse_decode("") == ""


@pytest.mark.skipif(
    morse_decode is None, reason="morse_decode function not implemented"
)
def test_single_letter():
    assert morse_decode(".-") == "A"


@pytest.mark.skipif(
    morse_decode is None, reason="morse_decode function not implemented"
)
def test_hello():
    assert morse_decode(".... . .-.. .-.. ---") == "HELLO"


@pytest.mark.skipif(
    morse_decode is None, reason="morse_decode function not implemented"
)
def test_alphabet():
    assert morse_decode(".- -... -.-.") == "ABC"


@pytest.mark.skipif(
    morse_decode is None, reason="morse_decode function not implemented"
)
def test_mixed():
    assert morse_decode(".- .----") == "A1"
