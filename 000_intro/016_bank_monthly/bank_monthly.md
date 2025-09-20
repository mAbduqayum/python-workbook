# Exercise: Bank Monthly Interest

Write a program that calculates compound interest with monthly compounding.

## Task

- Read the initial deposit amount (as `float`)
- Read the annual interest rate percentage (as `float`)
- Read the number of years (as `int`)
- Calculate and display the balance after the specified number of years with monthly compounding

## Examples

**Example 1:**

```
Enter initial deposit: 1000.00
Enter annual interest rate (%): 4.0
Enter number of years: 3
```

```
Balance after 3 years: 1127.27
```

**Example 2:**

```
Enter initial deposit: 5000.00
Enter annual interest rate (%): 3.5
Enter number of years: 2
```

```
Balance after 2 years: 5361.99
```

**Example 3:**

```
Enter initial deposit: 2500.00
Enter annual interest rate (%): 2.25
Enter number of years: 1
```

```
Balance after 1 year: 2556.83
```

## Formula

`balance = principal × (1 + rate/1200)^(12×years)`

## Note

Use `.2f` formatting to display 2 decimal places.
