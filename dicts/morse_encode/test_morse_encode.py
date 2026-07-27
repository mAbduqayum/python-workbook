try:
    from morse_encode import morse_encode
except ImportError:
    morse_encode = None


@pytest.mark.skipif(
    morse_encode is None, reason="morse_encode function not implemented"
)
def test_sos():
    assert morse_encode("SOS") == "... --- ..."


@pytest.mark.skipif(
    morse_encode is None, reason="morse_encode function not implemented"
)
def test_with_spaces():
    assert morse_encode("HI THERE") == ".... .. / - .... . .-. ."


@pytest.mark.skipif(
    morse_encode is None, reason="morse_encode function not implemented"
)
def test_numbers():
    assert morse_encode("123") == ".---- ..--- ...--"


@pytest.mark.skipif(
    morse_encode is None, reason="morse_encode function not implemented"
)
def test_case_insensitive():
    assert morse_encode("Hello") == morse_encode("HELLO")


@pytest.mark.skipif(
    morse_encode is None, reason="morse_encode function not implemented"
)
def test_empty():
    assert morse_encode("") == ""


@pytest.mark.skipif(
    morse_encode is None, reason="morse_encode function not implemented"
)
def test_single_char():
    assert morse_encode("A") == ".-"


@pytest.mark.skipif(
    morse_encode is None, reason="morse_encode function not implemented"
)
def test_lowercase():
    assert morse_encode("sos") == "... --- ..."


@pytest.mark.skipif(
    morse_encode is None, reason="morse_encode function not implemented"
)
def test_mixed_case():
    assert morse_encode("SoS") == "... --- ..."


@pytest.mark.skipif(
    morse_encode is None, reason="morse_encode function not implemented"
)
def test_alphabet():
    result = morse_encode("ABC")
    assert result == ".- -... -.-."


@pytest.mark.skipif(
    morse_encode is None, reason="morse_encode function not implemented"
)
def test_with_number_and_letter():
    result = morse_encode("A1")
    assert result == ".- .----"
