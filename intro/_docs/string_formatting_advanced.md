# F-String Formatting Advanced

Formatting features for lining up output and making numbers easier to read.

## Width and Alignment

| Format    | Description            | Example            | Output       |
|-----------|------------------------|--------------------|--------------|
| `{n:5}`   | Minimum width 5        | `f"{42:5}"`        | `   42`      |
| `{n:05}`  | Width 5, zero-padded   | `f"{42:05}"`       | `00042`      |
| `{s:<10}` | Left align, width 10   | `f"{'hello':<10}"` | `hello     ` |
| `{s:>10}` | Right align, width 10  | `f"{'hello':>10}"` | `     hello` |
| `{s:^10}` | Center align, width 10 | `f"{'hello':^10}"` | `  hello   ` |

## Custom Fill Characters

| Format    | Description              | Example       | Output  |
|-----------|--------------------------|---------------|---------|
| `{n:*<5}` | Left align with * fill   | `f"{42:*<5}"` | `42***` |
| `{n:*>5}` | Right align with * fill  | `f"{42:*>5}"` | `***42` |
| `{n:*^5}` | Center align with * fill | `f"{42:*^5}"` | `*42**` |

## Grouping and Separators

| Format     | Description                    | Example                | Output         |
|------------|--------------------------------|------------------------|----------------|
| `{n:,}`    | Thousands separator            | `f"{1234567:,}"`       | `1,234,567`    |
| `{n:_}`    | Underscore separator           | `f"{1234567:_}"`       | `1_234_567`    |
| `{n:,.2f}` | Float with thousands separator | `f"{1234567.89:,.2f}"` | `1,234,567.89` |

## Percentage Formatting

| Format    | Description               | Example           | Output       |
|-----------|---------------------------|-------------------|--------------|
| `{n:%}`   | Percentage                | `f"{0.1234:%}"`   | `12.340000%` |
| `{n:.2%}` | Percentage with precision | `f"{0.1234:.2%}"` | `12.34%`     |

## Table Formatting

| Use Case   | Format Pattern                            | Example                     |
|------------|-------------------------------------------|-----------------------------|
| Header row | `f"{'Item':<10} {'Qty':>5} {'Price':>8}"` | `Item         Qty    Price` |
| Data rows  | `f"{item:<10} {qty:>5} ${price:>7.2f}"`   | `Apples         5 $   1.25` |
| Separator  | `"-" * total_width`                       | `-------------------------` |
