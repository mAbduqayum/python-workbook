# Wrap Around

Write a function that keeps a number inside a range by wrapping around, the way
a clock goes from 12 back to 1.

## Task
- Create a function `wrap(value, low, high)`
- A value inside the range comes back unchanged
- A value outside the range keeps wrapping around: after `high` comes `low` again, and before `low` comes `high`

## Examples

| Call              | Returns |
|-------------------|---------|
| `wrap(13, 1, 12)` | `1`     |
| `wrap(0, 1, 12)`  | `12`    |
| `wrap(25, 1, 12)` | `1`     |
| `wrap(7, 1, 12)`  | `7`     |
| `wrap(10, 0, 6)`  | `3`     |
| `wrap(-1, 0, 6)`  | `6`     |
| `wrap(-8, 0, 6)`  | `6`     |
