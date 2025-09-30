# Fizz-Buzz

Display the answers for the Fizz-Buzz game for numbers 1 to 100.

## Task
- Display answers for numbers 1 through 100
- Each answer on its own line
- Apply the Fizz-Buzz rules

## Rules
- If number is divisible by 3: say "fizz"
- If number is divisible by 5: say "buzz"
- If divisible by both 3 and 5: say "fizzbuzz"
- Otherwise: say the number

## Example Output
```
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz
...
```

## Logic
- Use a for loop from 1 to 100
- For each number:
  - Check if divisible by both 3 and 5 (divisible by 15)
  - Else check if divisible by 3
  - Else check if divisible by 5
  - Else print the number

## Hints
- Use range(1, 101) for numbers 1-100
- Check divisibility with modulo operator: n % 3 == 0
- Order matters: check 15 first, then 3, then 5
- Or use string concatenation for fizz and buzz
