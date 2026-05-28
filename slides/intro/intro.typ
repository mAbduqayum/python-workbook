#import "@preview/touying:0.6.1": *
#import themes.dewdrop: *
#import "@preview/numbly:0.1.0": numbly

#show: dewdrop-theme.with(
  aspect-ratio: "16-9",
  footer: self => self.info.institution,
  navigation: "mini-slides",
  config-info(
    title: [Introduction to Python],
    subtitle: [Programming Fundamentals],
    author: [Python Workbook],
    date: datetime.today(),
    institution: [Programming Workshop],
  ),
)

#set heading(numbering: numbly("{1}.", default: "1.1"))

#title-slide()

#outline-slide()

= What is Python?

== Python Overview

Python is a *high-level*, *interpreted* programming language created by Guido van Rossum in 1991.

#pause

*Key Characteristics:*
- Easy to read and write
- Interpreted (no compilation needed)
- Cross-platform (Windows, Mac, Linux)
- Object-oriented and functional programming support
- Extensive standard library

#pause

*Why Python?*
- Beginner-friendly syntax
- Rapid development
- Large community and ecosystem
- Used in web development, data science, AI, automation, and more

== Python Philosophy

*The Zen of Python* (PEP 20):

#pause

- Beautiful is better than ugly
- Explicit is better than implicit
- Simple is better than complex
- Readability counts
- There should be one obvious way to do it

#pause

```python
import this  # Try this in Python!
```

= Getting Started

== Python Installation

*Option 1: Official Python*
- Download from python.org
- Includes IDLE (Python's built-in editor)
- Command line: `python` or `python3`

#pause

*Option 2: Anaconda Distribution*
- Includes Python + data science packages
- Jupyter Notebook included
- Great for beginners and data science

#pause

*Option 3: Online Editors*
- replit.com
- colab.research.google.com
- trinket.io

== Running Python Code

*Interactive Mode (REPL):*
```bash
$ python
>>> print("Hello, World!")
Hello, World!
>>> 2 + 3
5
```

#pause

*Script Mode:*
```python
# hello.py
print("Hello, World!")
```

```bash
$ python hello.py
Hello, World!
```

= Basic Syntax

== Your First Program

```python
print("Hello, World!")
```

#pause

*Let's break this down:*
- `print()` is a *function* that displays output
- `"Hello, World!"` is a *string* (text data)
- Parentheses `()` contain the function's arguments
- No semicolon needed at the end!

#pause

*Try it yourself!*

== Variables and Assignment

```python
# Creating variables
name = "Alice"
age = 25
height = 5.6
is_student = True
```

#pause

*Key Points:*
- No need to declare variable types
- Variable names should be descriptive
- Use lowercase with underscores: `first_name`
- Case sensitive: `Name` ≠ `name`

#pause

```python
print(name)        # Alice
print(age)         # 25
print(is_student)  # True
```

== Comments

*Single-line comments:*
```python
# This is a comment
print("Hello!")  # Comment at end of line
```

#pause

*Multi-line comments:*
```python
"""
This is a multi-line comment
Used for longer explanations
"""

'''
You can also use single quotes
for multi-line comments
'''
```

#pause

*Best Practice:* Write comments to explain *why*, not *what*

= Data Types

== Basic Data Types

*Numbers:*
```python
integer = 42          # int
decimal = 3.14159     # float
complex_num = 2 + 3j  # complex
```

#pause

*Text:*
```python
single_quotes = 'Hello'
double_quotes = "World"
multi_line = """This is a
multi-line string"""
```

#pause

*Boolean:*
```python
is_true = True
is_false = False
```

== Working with Numbers

*Basic arithmetic:*
```python
a = 10
b = 3

print(a + b)    # 13 (addition)
print(a - b)    # 7  (subtraction)
print(a * b)    # 30 (multiplication)
print(a / b)    # 3.33... (division)
print(a // b)   # 3  (floor division)
print(a % b)    # 1  (modulus/remainder)
print(a ** b)   # 1000 (exponentiation)
```

#pause

*Type conversion:*
```python
int("42")      # 42
float("3.14")  # 3.14
str(123)       # "123"
```

== Working with Strings

*String operations:*
```python
first_name = "John"
last_name = "Doe"

# Concatenation
full_name = first_name + " " + last_name
print(full_name)  # John Doe

# String methods
print(full_name.upper())      # JOHN DOE
print(full_name.lower())      # john doe
print(full_name.title())      # John Doe
print(len(full_name))         # 8
```

#pause

*F-strings (formatted strings):*
```python
age = 25
message = f"I am {age} years old"
print(message)  # I am 25 years old
```

= Input and Output

== Getting User Input

```python
name = input("What's your name? ")
print(f"Hello, {name}!")
```

#pause

*Input is always a string!*
```python
# Wrong way
age = input("How old are you? ")
next_year = age + 1  # Error!

# Right way
age = int(input("How old are you? "))
next_year = age + 1
print(f"Next year you'll be {next_year}")
```

== Output Formatting

*Basic print:*
```python
print("Hello")
print("World")
# Output:
# Hello
# World
```

#pause

*Print on same line:*
```python
print("Hello", end=" ")
print("World")
# Output: Hello World
```

#pause

*Multiple values:*
```python
name = "Alice"
age = 25
print("Name:", name, "Age:", age)
# Output: Name: Alice Age: 25

print(f"Name: {name}, Age: {age}")
# Output: Name: Alice, Age: 25
```

= Practice Exercise

== Your Turn!

Create a simple program that:
1. Asks for the user's name
2. Asks for their age
3. Calculates what year they were born
4. Displays a personalized message

#pause

*Example output:*
```
What's your name? Alice
How old are you? 25
Hello Alice! You were born in 1998.
```

#pause

*Try it yourself before looking at the solution!*

== Solution

```python
# Get user input
name = input("What's your name? ")
age = int(input("How old are you? "))

# Calculate birth year (simplified)
current_year = 2023  # or use datetime.now().year
birth_year = current_year - age

# Display result
print(f"Hello {name}! You were born in {birth_year}.")
```

#pause

*Bonus challenges:*
- Handle the current year automatically
- Add error checking for invalid ages
- Make the message more creative!

= Summary

== What We've Learned

*Core Concepts:*
- What Python is and why it's popular
- How to run Python code
- Basic syntax rules
- Variables and data types
- User input and output

#pause

*Key Skills:*
- Writing your first Python program
- Working with numbers and strings
- Getting user input
- Using comments effectively

#pause

*Next Steps:*
- Practice with more exercises
- Learn about conditionals (if/else)
- Explore loops and functions
- Start building real projects!

== Resources for Learning

*Official Documentation:*
- python.org/doc/
- docs.python.org/3/tutorial/

#pause

*Practice Platforms:*
- Python.org tutorial
- codecademy.com
- replit.com
- Our Python Workbook exercises!

#pause

*Community:*
- r/learnpython (Reddit)
- Python Discord communities
- Stack Overflow for questions

#focus-slide[
  Ready to start coding in Python?

  Let's practice! 🐍
]