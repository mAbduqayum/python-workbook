# Coin Sum - Hint

## Algorithm

- Recurse on two things at once: the remaining amount and the coins still allowed
- At each step, either use the first coin (subtract it from the amount, keeping the coin available for reuse) or skip it (drop it and move to the next coin) — add the counts of both branches
- Reaching exactly 0 counts as one way; going negative or running out of coins counts as zero

Here is `coin_sum(2, [1, 2])`. Each box shows the remaining amount and the coins
still allowed. The ends of the branches add up to 2 ways: `1 + 1` and `2`.

```mermaid
flowchart TD
    A["2 left, coins 1 and 2"] -->|use 1| B["1 left, coins 1 and 2"]
    A -->|skip 1| C["2 left, coin 2"]
    B -->|use 1| D["0 left: 1 way"]
    B -->|skip 1| E["1 left, coin 2"]
    E -->|use 2| F["-1 left: 0 ways"]
    E -->|skip 2| G["1 left, no coins: 0 ways"]
    C -->|use 2| H["0 left: 1 way"]
    C -->|skip 2| I["2 left, no coins: 0 ways"]
```

## Note

Deciding per coin (use it or drop it) counts each combination once — recursing only on the amount would count 2+1 and 1+2 as different ways.
