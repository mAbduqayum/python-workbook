# Coin Sum - Hint

## Algorithm

- Recurse on two things at once: the remaining amount and the coins still allowed
- At each step, either use the first coin (subtract it from the amount, keeping the coin available for reuse) or skip it (drop it and move to the next coin) - add the counts of both branches
- Reaching exactly 0 counts as one way; going negative or running out of coins counts as zero

Here is `coin_sum(2, [1, 2])`. Each box shows the remaining amount and the coins
still allowed. Each rounded box ends a branch, and together they add up to 2 ways:
`1 + 1` and `2`.

```mermaid
flowchart TD
    A["Amount 2<br/>Coins 1, 2"] -->|use 1| B["Amount 1<br/>Coins 1, 2"]
    A -->|skip 1| C["Amount 2<br/>Coin 2"]
    B -->|use 1| D(["Exact<br/>1 way"])
    B -->|skip 1| E["Amount 1<br/>Coin 2"]
    C -->|use 2| F(["Exact<br/>1 way"])
    C -->|skip 2| G(["No coins<br/>0 ways"])
    E -->|use 2| H(["Too much<br/>0 ways"])
    E -->|skip 2| I(["No coins<br/>0 ways"])
```

## Note

Deciding per coin (use it or drop it) counts each combination once - recursing only on the amount would count 2+1 and 1+2 as different ways.
