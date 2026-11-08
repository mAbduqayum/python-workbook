# Duration in Words

Write functions that spell out a number of seconds in words.

In [Time Converter](../../intro/time_seconds/time_seconds.md) you split seconds into minutes and seconds; now write the result out in words.

## Task
- Create a function `plural(count, word)` that returns the count and the word, adding an `s` unless the count is 1
- Create a function `format_duration(seconds)` that returns the duration in hours, minutes and seconds; `seconds` is a natural number or 0
  - Leave out any unit that is 0
  - A duration of 0 seconds is `"0 seconds"`

## Examples

| Call                    | Returns                        |
|-------------------------|--------------------------------|
| `plural(1, "hour")`     | `"1 hour"`                     |
| `plural(2, "hour")`     | `"2 hours"`                    |
| `plural(0, "second")`   | `"0 seconds"`                  |
| `format_duration(3725)` | `"1 hour 2 minutes 5 seconds"` |
| `format_duration(3600)` | `"1 hour"`                     |
| `format_duration(61)`   | `"1 minute 1 second"`          |
| `format_duration(7205)` | `"2 hours 5 seconds"`          |
| `format_duration(0)`    | `"0 seconds"`                  |
