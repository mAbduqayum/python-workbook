# Working Through an Exercise

Each exercise lives in its own folder. Inside, you'll find a problem
statement (`<name>.md`) and a test file (`test_<name>.py`). You write the
solution file yourself, naming it after the folder.

## Read the Problem

Start by reading the problem statement. It explains what your program
should do and ends with an **Examples** section.

For example, open `intro/circle_area/circle_area.md` before writing any
code.

## Reading the Examples

Problem statements show examples as pairs of plain code blocks. The first
block is what you type as input while your program runs, one value per
line, pressing **Enter** after each. The second block is the exact output
your program must print.

Here's the example from `circle_area`:

```
5.2
```

```
84.95
```

If an exercise needs no input, like `hello_world`, the first block is
omitted.

### Prompts Are Optional

You do **not** have to write a prompt string, and if you do, the wording is
yours to choose. All of these are accepted:

```python
radius = float(input("Enter radius: "))  # prompt is fine
radius = float(input("Radius? "))        # any wording is fine
radius = float(input())                  # no prompt is also fine
```

The checker never sees your prompts. It compares only the values you read
and the output you print. Some exercises still show prompts in their
examples (e.g. multi-value ones like `bmi`); those prompts are optional too.

## Write Your Solution

Create the solution file in the same folder, named after the folder.

For the `circle_area` exercise, that means creating
`intro/circle_area/circle_area.py`.

## Run Your Program

Run your program manually to see it in action:

```
uv run intro/circle_area/circle_area.py
```

`uv run` installs any dependencies automatically, so there's no separate
install step.

## Check Your Work with the Tests

Once you're happy with your solution, run the tests to check it:

```
uv run pytest intro/circle_area
```

To run every test in a chapter:

```
uv run pytest intro
```

## Reading Test Results

- **passed** - your output matches the expected output exactly
- **failed** - your output doesn't match; read the diff to see what was
  expected versus what your program actually printed
- **skipped** with "circle_area.py not implemented" - you haven't created the
  solution file yet. Skipped does **not** mean passed!

Tests compare your output *exactly*. Spacing, capitalization, and
punctuation all matter.

## Stuck?

If you get stuck, reference solutions live on the `solutions` branch:

```
git switch solutions
```

When you're ready to come back to your own work:

```
git switch main
```

Try to solve each exercise honestly before peeking. You'll learn a lot more
that way.

You've got this! Every exercise you finish makes the next one a little easier.
