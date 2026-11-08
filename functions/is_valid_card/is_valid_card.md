# Card Number Check

Write functions that check a card number with the Luhn rule, which catches most
typing mistakes.

## Task
- Create a function `digits_only(number)` that returns the number without its spaces
- Create a function `luhn_sum(digits)` that returns the Luhn sum of a string of digits
- Create a function `is_valid_card(number)` that returns `True` if the Luhn sum of the number's digits is divisible by 10, `False` otherwise

## Rule
Starting from the rightmost digit, double every second digit: the 2nd, 4th,
6th and so on, counting from the right. When doubling gives more than 9,
subtract 9. The Luhn sum is the total of all the digits after doubling.

For `"8763"`: 3 stays 3, 6 doubles to 12 and becomes 3, 7 stays 7, and 8
doubles to 16 and becomes 7, so the Luhn sum is 3 + 3 + 7 + 7 = 20.

## Examples

| Call                                   | Returns              |
|----------------------------------------|----------------------|
| `digits_only("4539 1488 0343 6467")`   | `"4539148803436467"` |
| `luhn_sum("8763")`                     | `20`                 |
| `luhn_sum("79927398713")`              | `70`                 |
| `is_valid_card("79927398713")`         | `True`               |
| `is_valid_card("79927398710")`         | `False`              |
| `is_valid_card("4539 1488 0343 6467")` | `True`               |
