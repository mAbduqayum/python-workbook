# Debugging Your Programs

A bug is a mistake in a program, and every programmer writes them. Finding one
is a skill you can practice. It takes the same steps every time, not luck.

## Five Steps for Any Bug

1. **Make it happen again.** Find the input that shows the bug and write it
   down. Without it, you can't tell whether a fix worked.
2. **Read what Python tells you.** A crash names the line and the error.
3. **Guess the cause.** Say what you think is wrong, and what you would see if
   you are right.
4. **Look.** Print the variables, or step through the program in the debugger,
   and compare them with what you worked out by hand.
5. **Fix one thing, then run again.** Try the input from step 1, then your other
   examples, because a fix can break something else.

A wrong guess still tells you something, so go back to step 3 with a better one.
Changing code at random until it works leaves you with a program you can't
explain.

## Reading a Traceback

When a program crashes, Python prints a **traceback**: the function calls that
were running when it stopped. This program crashes on its second call:

```python
def average(prices):
    total = 0
    for price in prices:
        total += price
    return total / len(prices)


print(average([10, 20, 30]))
print(average([]))
```

```
20.0
Traceback (most recent call last):
  File "/home/farid/prices.py", line 9, in <module>
    print(average([]))
          ~~~~~~~^^^^
  File "/home/farid/prices.py", line 5, in average
    return total / len(prices)
           ~~~~~~^~~~~~~~~~~~~
ZeroDivisionError: division by zero
```

Read it from the bottom up:

| Part of the traceback                 | What it tells you                                    |
|---------------------------------------|------------------------------------------------------|
| `ZeroDivisionError: division by zero` | What went wrong                                      |
| `line 5, in average`                  | Where: the line Python couldn't finish               |
| `line 9, in <module>`                 | Who called it: `<module>` means outside any function |
| `~~~^^^`                              | Which part of the line was running                   |

So `average([])` divided by `len(prices)`, which is `0`. Now you can decide what
the average of nothing should be.

A traceback shows where the program stopped, which isn't always where the
mistake is. A bad value may have been made many lines earlier. If the last lines
are in a file you didn't write, look for the lowest line from a file of your own.

## Syntax Errors

A `SyntaxError` means Python couldn't read your file, so none of it runs, not
even the lines above the mistake:

```
  File "/home/farid/hello.py", line 1
    print("hi"
         ^
SyntaxError: '(' was never closed
```

If the line it names looks right, check the line above it.

## Common Errors

You'll meet these as the chapters introduce what causes them.

| Error               | What it means             | Check first                               |
|---------------------|---------------------------|-------------------------------------------|
| `SyntaxError`       | Python can't read a line  | A missing `)`, `"` or `:`                 |
| `IndentationError`  | The indentation is wrong  | The block after a `:` is indented         |
| `NameError`         | No variable by that name  | The spelling, and that it's already set   |
| `TypeError`         | A value of the wrong type | `input()` returns a string: convert it    |
| `ValueError`        | A value that can't be used | What `int()` or `float()` was given      |
| `IndexError`        | No item at that index     | The last index is `len(items) - 1`        |
| `KeyError`          | No such key in the dict   | The spelling, and that the key was added  |
| `ZeroDivisionError` | Division by zero          | Where the divisor came from: an empty list? |
| `AttributeError`    | No such method            | The value's type: is it `None` or a dict? |
| `FileNotFoundError` | No file at that path      | The name, and the folder you run from     |
| `RecursionError`    | Too many nested calls     | That the base case can be reached         |

## When the Output Is Wrong

A wrong answer is harder than a crash, because there's no message. Work the
answer out by hand, then find the first place where the program disagrees with
you. This program should add the numbers from 1 to `n`:

```python
n = 4
total = 0
for i in range(1, n):
    total += i
print(total)  # 6, but 1 + 2 + 3 + 4 is 10
```

Print the variables inside the loop:

```python
n = 4
total = 0
for i in range(1, n):
    total += i
    print(f"i={i} total={total}")
print(total)
```

```
i=1 total=1
i=2 total=3
i=3 total=6
6
```

`i` never reaches 4, because `range` stops before its end. The fix is
`range(1, n + 1)`. Remove the extra `print` afterward: the tests compare
everything your program prints.

## When a Test Fails

A failed test on a function shows the check that failed, marked with `>`:

```
>       assert count_lines(str(test_file)) == 3
E       AssertionError: assert 4 == 3
```

The left number is what your function returned, and the right number is what it
should have returned. The lines above the `>` show the input. Call your function
with that same input yourself, and start again from step 1.

## Stepping Through a Program in PyCharm

The debugger runs your program one line at a time and shows you every variable.
It helps most with loops and functions, where a lot of `print` calls get hard to
read.

1. **Set a breakpoint.** Click the gutter, the strip beside the line numbers,
   next to the first line you want to look at. A red dot appears. The program
   will pause just before it runs that line.
2. **Start the debugger.** Right-click in the file and choose **Debug**. The
   **Debug** tool window opens, and the paused line is highlighted.
3. **Type any input.** A program that calls `input()` waits for you in the
   **Console** tab of the same window.
4. **Step through the program.** Use these keys, or the buttons on the window's
   toolbar:

   | Key        | Action    | What it does                                 |
   |------------|-----------|----------------------------------------------|
   | `F8`       | Step Over | Runs this line and stops at the next one     |
   | `F7`       | Step Into | Goes inside the function this line calls     |
   | `Shift+F8` | Step Out  | Finishes this function and returns to its caller |

   The **Resume Program** button runs on to the next breakpoint, or to the end.

5. **Watch the variables.** PyCharm shows their values beside each line and in
   the **Threads & Variables** tab. Before you press `F8`, predict what will
   change. When the program surprises you, you have found the bug or are close
   to it.

If PyCharm says no Python interpreter is configured, open
**Settings → Project: python-workbook → Python Interpreter** and choose the
Python in the `.venv` folder that `uv run` created.

## Still Stuck?

Explain your program out loud, one line at a time, as if to someone who has never
seen it. You'll often hear the mistake as you say it. If not, take a break: bugs
are easier to see after one.
