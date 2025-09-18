# String Functions in Conditionals

## Essential String Functions for Conditional Logic

| Function/Operation | Example                                                               | Purpose                                               |
|--------------------|-----------------------------------------------------------------------|-------------------------------------------------------|
| `==` operator      | `"cat" == "dog"` # `False`<br>`"cat" == "cat"` # `True`               | Compare strings for exact equality                    |
| `in` operator      | `"a" in "hello"` # `False`<br>`"e" in "hello"` # `True`               | Check if character/substring exists in string         |
| `[?]` indexing     | `"hello"[0]` # `"h"`<br>`"hello"[4]` # `"o"`<br>`"hello"[-1]` # `"o"` | Extract character at specific position                |
| `.lower()`         | `"Hello".lower()` # `"hello"`                                         | Convert to lowercase for case-insensitive comparisons |
| `.upper()`         | `"hello".upper()` # `"HELLO"`                                         | Convert to uppercase                                  |
| `.title()`         | `"hello".title()` # `"Hello"`                                         | Convert to title case (first letter capitalized)      |
| `len()`            | `len("hello")` # `5`                                                  | Get the number of characters in a string              |
| `ord()`            | `ord("A")` # `65`                                                     | Convert character to ASCII numeric value              |
| `chr()`            | `chr(65)` # `"A"`                                                     | Convert ASCII numeric value to character              |

