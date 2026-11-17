# Exercise: Richter Scale

Write a program that reads an earthquake magnitude and displays the appropriate descriptor according to the Richter scale.

## Richter Scale Classifications
| Magnitude               | Descriptor |
|-------------------------|------------|
| magnitude < 2.0         | micro      |
| 2.0 <= magnitude < 3.0  | very minor |
| 3.0 <= magnitude < 4.0  | minor      |
| 4.0 <= magnitude < 5.0  | light      |
| 5.0 <= magnitude < 6.0  | moderate   |
| 6.0 <= magnitude < 7.0  | strong     |
| 7.0 <= magnitude < 8.0  | major      |
| 8.0 <= magnitude < 10.0 | great      |
| magnitude >= 10.0       | meteoric   |

## Examples
**Example 1:**
```
1.5
```
```
micro
```

## About the Richter Scale
The Richter scale is a **logarithmic scale**, not linear. Each whole number increase represents a 10-fold increase in amplitude and approximately 31.6 times more energy release. For example, a magnitude 5.0 earthquake is 10 times stronger than a magnitude 4.0 earthquake.
