# String Edit Distance - Hint

## Algorithm

- If either string is empty, the distance is the length of the other — insert or delete everything
- If the last characters of both strings match, drop them and recurse; they cost nothing
- Otherwise try each operation on the last position — insert, delete, replace — as a recursive call on the correspondingly shortened string(s), and take the cheapest plus one

## Note

Every call shortens at least one string, so the recursion always reaches an empty-string base case.
