# Discount Table

A retailer is having a 60% off sale and needs a discount table for customers.

## Task
- Generate a table showing original prices, discount amounts, and new prices
- Include prices: $4.95, $9.95, $14.95, $19.95, and $24.95
- Round discount amounts and new prices to 2 decimal places
- Use a loop to generate the table

## Example Output
```
Original Price    Discount Amount    New Price
$4.95            $2.97              $1.98
$9.95            $5.97              $3.98
$14.95           $8.97              $5.98
$19.95           $11.97             $7.98
$24.95           $14.97             $9.98
```

## Logic
- Use a for loop with a list of prices: [4.95, 9.95, 14.95, 19.95, 24.95]
- For each price:
  - Calculate discount = price * 0.60
  - Calculate new_price = price - discount
  - Round to 2 decimal places
  - Display in formatted output

## Hints
- Use f-strings or format() for formatted output
- round(value, 2) rounds to 2 decimal places
- Consider column alignment for better presentation
