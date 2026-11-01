# Longest Consecutive Sequence - Hint

## Algorithm

- Put all numbers into a set for O(1) membership checks
- A number starts a sequence only if `num - 1` is not in the set — skip all other numbers
- From each sequence start, count upward (`num + 1`, `num + 2`, …) while the next number is in the set
- Track the longest count seen

```mermaid
flowchart TD
    A{"Numbers left?"} -->|No| Z["Return the longest"]
    A -->|Yes| B{"Is the number before<br/>this one in the set?"}
    B -->|"Yes: skip it"| A
    B -->|"No: it starts a sequence"| C["Set the count to 1"]
    C --> D{"Is the next number<br/>in the set?"}
    D -->|Yes| E["Add 1 to the count"]
    E --> D
    D -->|No| F["Update the longest"]
    F --> A
```

## Note

Counting only from sequence starts visits each number at most twice, making the algorithm O(n) instead of O(n²).
