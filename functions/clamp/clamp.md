# Clamp

Write a function that keeps a number inside a range.

## Task
- Create a function `clamp(value, low, high)`
- Return `low` if `value` is below `low`, `high` if it is above `high`, and `value` itself otherwise

## Examples

| Call               | Returns |
|--------------------|---------|
| `clamp(13, 1, 12)` | `12`    |
| `clamp(0, 1, 12)`  | `1`     |
| `clamp(7, 1, 12)`  | `7`     |
| `clamp(-5, -3, 3)` | `-3`    |
