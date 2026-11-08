import pytest

try:
    from format_duration import format_duration, plural
except ImportError:
    format_duration = None
    plural = None

pytestmark = pytest.mark.skipif(
    format_duration is None or plural is None,
    reason="format_duration or plural not implemented",
)


@pytest.mark.parametrize(
    "count, word, expected",
    [
        (1, "hour", "1 hour"),
        (2, "hour", "2 hours"),
        (0, "second", "0 seconds"),
        (1, "minute", "1 minute"),
        (59, "minute", "59 minutes"),
    ],
)
def test_plural(count, word, expected):
    assert plural(count, word) == expected


@pytest.mark.parametrize(
    "seconds, expected",
    [
        (0, "0 seconds"),
        (1, "1 second"),
        (59, "59 seconds"),
        (60, "1 minute"),
        (61, "1 minute 1 second"),
        (120, "2 minutes"),
        (3600, "1 hour"),
        (3601, "1 hour 1 second"),
        (3660, "1 hour 1 minute"),
        (3725, "1 hour 2 minutes 5 seconds"),
        (7205, "2 hours 5 seconds"),
        (7322, "2 hours 2 minutes 2 seconds"),
        (90061, "25 hours 1 minute 1 second"),
    ],
)
def test_format_duration(seconds, expected):
    assert format_duration(seconds) == expected
