# Infix to Postfix - Hint

## Algorithm

- Keep an output list and an operator stack
- Numbers go straight to the output
- `(` is pushed onto the stack; `)` pops operators to the output until the matching `(`
- Before pushing an operator, first pop operators of higher or equal precedence to the output
- After the last token, pop whatever remains on the stack to the output

```mermaid
flowchart TD
    A{"Kind of token"} -->|Number| B["Add it to<br/>the output"]
    A -->|"("| C["Push it onto<br/>the stack"]
    A -->|")"| D["Pop to the output<br/>until the (, then<br/>discard the ("]
    A -->|Operator| E["Pop to the output while the<br/>top operator has higher or<br/>equal precedence, then<br/>push the token"]
    B --> F{"More tokens?"}
    C --> F
    D --> F
    E --> F
    F -->|Yes| A
    F -->|No| G["Pop everything left on<br/>the stack to the output"]
```

## Note

This is Dijkstra's Shunting Yard algorithm — the stack holds back operators until their operands have reached the output.
