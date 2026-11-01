# Binary Search - Hint

## Algorithm

- Keep two boundaries, `low` and `high`, that bracket where the target can still be
- Look at the middle element between them
- If it's the target, you're done; if it's too small, the target must be in the right half; if too big, the left half
- Move the matching boundary past the middle and repeat until the boundaries cross

```mermaid
flowchart TD
    A["low = first index<br/>high = last index"] --> B{"low <= high?"}
    B -->|No| C["Return -1"]
    B -->|Yes| D["middle = halfway between<br/>low and high, rounded down"]
    D --> E{"Item at middle"}
    E -->|"= target"| F["Return middle"]
    E -->|"< target"| G["low = middle + 1"]
    E -->|"> target"| H["high = middle - 1"]
    G --> B
    H --> B
```

## Note

Each comparison halves the remaining range, so the search takes O(log n) steps instead of scanning every element.
