# Exercise: Bank Annual Interest

Write a program that calculates the balance of a savings account after earning annual interest.

## Task
- Read the initial deposit amount (as `float`)
- Read the annual interest rate percentage (as `float`)
- Calculate and display the balance after 1, 2, and 3 years

## Examples
**Example 1:**
```
Enter initial deposit: 1000.00
Enter annual interest rate (%): 4.5
Balance after 1 year: 1045.00
Balance after 2 years: 1092.03
Balance after 3 years: 1141.17
```

**Example 2:**
```
Enter initial deposit: 2500.00
Enter annual interest rate (%): 3.25
Balance after 1 year: 2581.25
Balance after 2 years: 2665.14
Balance after 3 years: 2751.75
```

**Example 3:**
```
Enter initial deposit: 500.00
Enter annual interest rate (%): 2.8
Balance after 1 year: 514.00
Balance after 2 years: 528.39
Balance after 3 years: 543.20
```

## Formula
- Year 1: `balance = deposit × (1 + rate/100)`
- Year 2: `balance = year1_balance × (1 + rate/100)`  
- Year 3: `balance = year2_balance × (1 + rate/100)`

## Note
Use `.2f` formatting to display 2 decimal places.