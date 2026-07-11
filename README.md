# Python Workbook

A structured collection of Python programming exercises designed for learning and practice.

## Getting Started

### Prerequisites

Install the following tools:

- **Git** - Version control system
- **uv** - Python package manager
- **VS Code** - Code editor

### Setup Instructions

1. **Open your terminal**

2. **Create a directory for your repositories:**
   ```bash
   mkdir -p ~/repos
   cd ~/repos
   ```

3. **Clone the repository:**
   ```bash
   git clone https://github.com/mAbduqayum/python-workbook.git
   ```

4. **Navigate to the project:**
   ```bash
   cd python-workbook
   ```

5. **Open in VS Code:**
   ```bash
   code .
   ```

### Quick Start

1. Read the documentation in [`intro/_docs/`](intro/_docs/table_of_contents.md)
2. Start with basic exercises in the `intro/` directory
3. Use `uv run` to execute Python files

## Working Through an Exercise

Each exercise is a folder containing a problem statement (`<name>.md`) and
tests (`test_<name>.py`).

1. Read the problem statement, e.g. `conditionals/leap_year/leap_year.md`
2. Create your solution file in that same folder, named after the folder,
   e.g. `conditionals/leap_year/leap_year.py`
3. Run it manually:
   ```bash
   uv run conditionals/leap_year/leap_year.py
   ```
4. Check it against the tests:
   ```bash
   uv run pytest conditionals/leap_year
   ```

`uv run` installs any dependencies automatically, so there's no separate
install step.

### Reading Test Results

- **passed** - your output matches what's expected
- **failed** - your output doesn't match; read the diff to see exactly what
  differs. Tests compare output *exactly*, so spacing, capitalization, and
  punctuation all matter
- **skipped** with "Solution file not found" - you haven't created the
  solution file yet. Skipped does **not** mean passed

## Recommended Reading Order

1. [`Introduction`](intro/_docs/table_of_contents.md)
2. [`Conditional`](conditionals/_docs/table_of_contents.md)
3. [`Repetition`](repetitions/_docs/table_of_contents.md)
4. [`Function`](functions/_docs/table_of_contents.md)
5. [`List`](lists/_docs/table_of_contents.md)
6. [`Set`](sets/_docs/table_of_contents.md)
7. [`Dict`](dicts/_docs/table_of_contents.md)
8. [`Error`](errors/_docs/table_of_contents.md)
9. [`File`](files/_docs/table_of_contents.md)
10. [`Recursion`](recursions/_docs/table_of_contents.md)