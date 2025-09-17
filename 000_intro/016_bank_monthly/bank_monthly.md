# Exercise: Bank Monthly Interest

Write a program that calculates compound interest with monthly compounding.

## Task
- Read the initial deposit amount (as `float`)
- Read the annual interest rate percentage (as `float`)
- Calculate and display the balance after 1, 2, and 3 years with monthly compounding

## Examples
**Example 1:**
```
Enter initial deposit: 1000.00
Enter annual interest rate (%): 4.0
```
```
Balance after 1 year: 1040.74
Balance after 2 years: 1083.14
Balance after 3 years: 1127.16
```

**Example 2:**
```
Enter initial deposit: 5000.00
Enter annual interest rate (%): 3.5
```
```
Balance after 1 year: 5178.00
Balance after 2 years: 5364.66
Balance after 3 years: 5560.51
```

**Example 3:**
```
Enter initial deposit: 2500.00
Enter annual interest rate (%): 2.25
```
```
Balance after 1 year: 2556.77
Balance after 2 years: 2614.89
Balance after 3 years: 2674.42
```

## Formula
`balance = principal × (1 + rate/1200)^(12×years)`

## Note
Use `.2f` formatting to display 2 decimal places.