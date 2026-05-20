# H2O Phases

Write a program that determines the phase of water based on temperature.

## Temperature Ranges

| Temperature (°C)  | Phase             |
|-------------------|-------------------|
| Below 0           | `solid`           |
| Exactly 0         | `solid or liquid` |
| Between 0 and 100 | `liquid`          |
| Exactly 100       | `liquid or gas`   |
| Above 100         | `gas`             |

## Examples

**Example 1:**

```
-10
```

```
solid
```

**Example 2:**

```
25
```

```
liquid
```

**Example 3:**

```
0
```

```
solid or liquid
```
