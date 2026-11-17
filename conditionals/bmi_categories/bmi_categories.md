# BMI Categories

Write a program that reads a person's height in meters, then their weight in kilograms, and displays the weight category of their `BMI`. It reads the two values in the same order as [Body Mass Index](../../intro/bmi/bmi.md).

## BMI Categories

| BMI Range           | Category      |
|---------------------|---------------|
| `BMI < 18.5`        | underweight   |
| `18.5 ≤ BMI < 25.0` | normal weight |
| `25.0 ≤ BMI < 30.0` | overweight    |
| `BMI ≥ 30.0`        | obese         |

## Examples

**Example 1:**

```
1.75
70
```

```
normal weight
```

## Formula

`BMI = weight (kg) / height² (m²)`
