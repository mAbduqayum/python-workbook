# Exercise: Bank Annual Interest

Write a program that calculates the balance of a savings account after earning annual interest.

## Task

- Read the initial deposit amount (as `float`)
- Read the annual interest rate percentage (as `float`)
- Read the number of years (as `int`)
- Calculate and display the balance after the specified number of years

## Examples

**Example 1:**

```
Enter initial deposit: 1000.00
Enter annual interest rate (%): 4.5
Enter number of years: 3
```

```
Balance after 3 years: 1141.17
```

**Example 2:**

```
Enter initial deposit: 2500.00
Enter annual interest rate (%): 3.25
Enter number of years: 5
```

```
Balance after 5 years: 2933.53
```

**Example 3:**

```
Enter initial deposit: 500.00
Enter annual interest rate (%): 2.8
Enter number of years: 1
```

```
Balance after 1 year: 514.00
```

## Formula

`balance = deposit × (1 + rate/100)^years`

## Note

Use `.2f` formatting to display 2 decimal places.
