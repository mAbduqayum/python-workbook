#import "@preview/touying:0.6.1": *
#import themes.dewdrop: *
#import "@preview/numbly:0.1.0": numbly

#show: dewdrop-theme.with(
  aspect-ratio: "16-9",
  footer: self => self.info.institution,
  navigation: none,
  config-info(
    title: [Repetition Structures in Python],
    subtitle: [Loops and Iteration],
    author: [Python Workbook],
    date: datetime.today(),
    institution: [Programming Workshop],
  ),
)

#set heading(numbering: numbly("{1}.", default: "1.1"))

#title-slide()

#outline-slide()

= Introduction to Loops

== Why Do We Need Loops?

In previous chapters, we learned about sequential programs and conditional statements.

#pause

*But what if we need to:*
- Print a pattern with 100 rows?
- Read values until the user enters a specific value?
- Process each character in a string?
- Find the sum of numbers from 1 to 1000?

#pause

Writing the same code repeatedly would be *impractical* and *error-prone*.

#pause

*Solution:* **Loops** allow you to execute a block of code multiple times efficiently!

== The Two Types of Loops

Python provides two main loop structures:

#pause

*1. `for` loop*
- Use when you know *how many times* to repeat
- Perfect for iterating over sequences
- Example: "Print numbers from 1 to 10"

#pause

*2. `while` loop*
- Use when you repeat based on a *condition*
- Continues until condition becomes false
- Example: "Read input until user enters 0"

= The `for` Loop

== Basic `for` Loop Syntax

```python
for variable in sequence:
    # code to execute
    # this block is indented
```

#pause

*Example: Counting from 1 to 5*
```python
for i in range(1, 6):
    print(i)
```

#pause

*Output:*
```
1
2
3
4
5
```

== The `range()` Function

The `range()` function generates a sequence of numbers:

#pause

```python
range(stop)              # From 0 to stop-1
range(start, stop)       # From start to stop-1
range(start, stop, step) # From start to stop-1 by step
```

#pause

*Examples:*
```python
range(5)           # 0, 1, 2, 3, 4
range(2, 6)        # 2, 3, 4, 5
range(1, 10, 2)    # 1, 3, 5, 7, 9
range(10, 0, -1)   # 10, 9, 8, ..., 1
```

== `range()` in Action

```python
# Count 0 to 4
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4
```

#pause

```python
# Count 1 to 10
for i in range(1, 11):
    print(i)  # 1, 2, 3, ..., 10
```

#pause

```python
# Count by 10s from 0 to 100
for i in range(0, 101, 10):
    print(i)  # 0, 10, 20, ..., 100
```

#pause

```python
# Count backwards from 5 to 1
for i in range(5, 0, -1):
    print(i)  # 5, 4, 3, 2, 1
```

== Iterating Over Strings

You can iterate over each character in a string:

```python
word = "hello"
for char in word:
    print(char)
```

#pause

*Output:*
```
h
e
l
l
o
```

#pause

*This is very useful for:*
- Processing text character by character
- Counting specific characters
- Building new strings from old ones

= The `while` Loop

== Basic `while` Loop Syntax

```python
while condition:
    # code to execute
    # usually modify something to make condition false
```

#pause

The loop repeats as long as the condition is `True`.

#pause

*Example: Count from 1 to 5*
```python
count = 1
while count <= 5:
    print(count)
    count += 1  # Important: increment count!
```

#pause

*Output:*
```
1
2
3
4
5
```

== `while` Loop with Sentinel Value

*Problem:* Read numbers from the user until they enter 0.

```python
num = int(input("Enter a number (0 to stop): "))
while num != 0:
    print(f"You entered: {num}")
    num = int(input("Enter a number (0 to stop): "))
print("Done!")
```

#pause

*Key concept:* A **sentinel value** (like 0) signals the end of input.

#pause

*Common sentinel values:*
- Empty string `""`
- Zero `0`
- Negative number `-1`
- Special keyword like `"quit"`

= Common Loop Patterns

== Pattern 1: Accumulation

Calculate the sum of numbers from 1 to 10:

```python
total = 0
for i in range(1, 11):
    total += i
print(f"Sum: {total}")  # Sum: 55
```

#pause

*Key steps:*
1. Initialize accumulator (`total = 0`)
2. Add to accumulator in loop (`total += i`)
3. Use result after loop

#pause

*Also works for:*
- Product: `product *= i`
- Concatenation: `text += char`

== Pattern 2: Counting

Count how many even numbers are between 1 and 10:

```python
count = 0
for i in range(1, 11):
    if i % 2 == 0:
        count += 1
print(f"Even numbers: {count}")  # Even numbers: 5
```

#pause

*Key steps:*
1. Initialize counter (`count = 0`)
2. Check condition in loop
3. Increment when condition is true (`count += 1`)

== Pattern 3: Finding Maximum/Minimum

Find the maximum of numbers entered by the user:

```python
max_value = float('-inf')  # Start with very small value
for i in range(5):
    num = int(input("Enter a number: "))
    if num > max_value:
        max_value = num
print(f"Maximum: {max_value}")
```

#pause

*For minimum:*
```python
min_value = float('inf')   # Start with very large value
# ... compare with < instead of >
```

= Nested Loops

== What are Nested Loops?

A *nested loop* is a loop inside another loop.

#pause

```python
for i in range(3):        # Outer loop
    for j in range(3):    # Inner loop
        print(f"i={i}, j={j}")
```

#pause

*The inner loop executes completely for each iteration of the outer loop.*

#pause

*Output:*
```
i=0, j=0
i=0, j=1
i=0, j=2
i=1, j=0
i=1, j=1
...
```

== Nested Loop Example: Triangle Pattern

```python
n = int(input())

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()  # New line after each row
```

#pause

*Input:* `5`

*Output:*
```
1
12
123
1234
12345
```

#pause

*Use nested loops for:*
- 2D patterns and shapes
- Multiplication tables
- Processing matrices/grids

= Loop Control Statements

== `break` - Exit the Loop Early

The `break` statement immediately exits the loop:

```python
# Find first number divisible by 7 between 100 and 200
for i in range(100, 201):
    if i % 7 == 0:
        print(f"Found: {i}")
        break  # Exit loop immediately
```

#pause

*Output:* `Found: 105`

#pause

*Use `break` when:*
- You found what you're looking for
- A special condition is met
- You want to exit early

== `continue` - Skip to Next Iteration

The `continue` statement skips the rest of the current iteration:

```python
# Print odd numbers from 1 to 10
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)
```

#pause

*Output:*
```
1
3
5
7
9
```

#pause

*Use `continue` when:*
- You want to skip certain values
- Filtering items in a loop

== Printing on the Same Line

Use `end=""` parameter to prevent newline:

```python
# Print numbers on one line
for i in range(1, 6):
    print(i, end=" ")  # Print with space separator
print()  # Newline at the end
```

#pause

*Output:* `1 2 3 4 5`

#pause

*Default:* `end="\n"` (newline)

*Custom:* You can use any string: `end=", "` or `end=" -> "`

= When to Use `for` vs `while`

== Choosing the Right Loop

#grid(
  columns: (1fr, 1fr),
  gutter: 1em,
  [
    *Use `for` when:*
    - You know the number of iterations
    - Iterating over a sequence
    - Processing each element
    - Example: "Print 1 to 100"
  ],
  [
    *Use `while` when:*
    - You repeat based on a condition
    - Reading until sentinel value
    - Continuing until specific condition
    - Example: "Read until user enters 0"
  ]
)

#pause

*Rule of thumb:*
- Known iterations → `for`
- Condition-based → `while`

= Common Pitfalls

== Pitfall 1: Infinite Loops

Make sure your loop condition will eventually become false!

```python
# WRONG - Infinite loop!
i = 1
while i <= 5:
    print(i)
    # Forgot to increment i!
```

#pause

```python
# CORRECT
i = 1
while i <= 5:
    print(i)
    i += 1  # Now it will stop
```

#pause

*Warning signs:*
- Loop variable never changes
- Condition always remains True
- Your program "hangs" and never finishes

== Pitfall 2: Off-by-One Errors

Be careful with loop boundaries!

```python
# To print 1 to 10 (inclusive)
for i in range(1, 11):  # NOT range(1, 10)
    print(i)
```

#pause

*Remember:* `range()` is *exclusive* of the stop value!

#pause

```python
range(1, 5)    # 1, 2, 3, 4 (NOT 5)
range(1, 6)    # 1, 2, 3, 4, 5 (to include 5)
```

#pause

*Common mistakes:*
- `range(10)` gives 0-9, not 1-10
- `range(len(text) - 1)` misses last character

== Pitfall 3: Modifying Loop Variable in `for` Loop

Don't modify the loop variable inside a `for` loop:

```python
# WRONG - This doesn't work as expected!
for i in range(5):
    print(i)
    i += 1  # This doesn't affect the loop!
```

#pause

*Output:* Still `0, 1, 2, 3, 4` (not what you might expect)

#pause

```python
# Use a while loop if you need to control the increment
i = 0
while i < 5:
    print(i)
    i += 2  # Now this works: 0, 2, 4
```

= Tips for Success

== Best Practices

*1. Choose the right loop*
- Use `for` when you know the count
- Use `while` for conditions

#pause

*2. Initialize before the loop*
- Set up accumulators, counters, and variables

#pause

*3. Update inside the loop*
- Make sure loop variables change to avoid infinite loops

#pause

*4. Test loop boundaries*
- Verify your loop runs the correct number of times
- Test with 0, 1, and many iterations

== More Best Practices

*5. Use descriptive variable names*
```python
# Bad
for i in range(10):
    for j in range(10):
        pass

# Good
for row in range(10):
    for col in range(10):
        pass
```

#pause

*6. Indent properly*
- Python requires correct indentation for loop bodies

#pause

*7. Debug with print statements*
- Add `print()` to see what's happening in each iteration

= Summary

== What We've Learned

*Core Concepts:*
- Two types of loops: `for` and `while`
- The `range()` function for numeric sequences
- Iterating over strings character by character
- Common patterns: accumulation, counting, finding

#pause

*Advanced Topics:*
- Nested loops for 2D patterns
- Loop control with `break` and `continue`
- Choosing between `for` and `while`
- Common pitfalls and how to avoid them

#pause

*Next Steps:*
- Practice with loop exercises
- Combine loops with conditionals
- Build more complex programs

== Quick Reference

```python
# For loop patterns
for i in range(10):              # 0 to 9
for i in range(5, 10):           # 5 to 9
for i in range(0, 10, 2):        # 0, 2, 4, 6, 8
for i in range(10, 0, -1):       # 10 to 1
for char in text:                # Each character

# While loop
while condition:
    # code
    # update condition

# Loop control
break      # Exit loop
continue   # Skip to next iteration
```

#focus-slide[
  Ready to master loops?

  Let's practice! 🔄
]
