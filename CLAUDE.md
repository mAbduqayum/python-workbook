# Python Workbook Project

This is a structured collection of Python programming exercises designed for learning and practice.

## Project Structure

- Each exercise is in a numbered directory
  - `0**` basics
  - `1**` conditionals
  - `2**` repetitions
  - `3**` functions
  - `4**` lists
  - `5**` dictionaries
  - `6**` files and exceptions
  - `7**` recursion
- Exercise directories contain:
- Reference materials are in `*_docs` directories

## Exercise Categories

- **Basic I/O**: Hello world, user input/output
- **Computer Science**: Arithmetic, geometry, area/perimeter calculations
- **Mathematics**: Arithmetic, geometry, area/perimeter calculations
- **Physics**: Free fall, ideal gas law, pressure conversions
- **Chemistry**: Free fall, ideal gas law, pressure conversions
- **Biology**: Free fall, ideal gas law, pressure conversions
- **Finance**: Interest calculations, tip calculators, banking
- **Time/Date**: Time conversions, date calculations
- **Utilities**: Sorting, string manipulation, unit conversions

## Testing and Validation

- Manually verify outputs match the examples in the `.md` files
- Test edge cases and boundary conditions
- Ensure mathematical calculations are accurate to specified precision
- Use Python REPL or scripts to validate formulas and expected outputs

## Mathematical Accuracy

- Double-check all mathematical formulas using Python calculations
- Use proper mathematical constants (e.g., `math.pi`, `math.e`)
- Verify trigonometric calculations use correct units (radians vs degrees)
- Test complex formulas (Heron's formula, great circle distance, etc.) thoroughly

## Commands
- `uv run`
- `git mv` to reorder files. don't use temp dirs, the dirs are unique even without enumeration

## Quality Checklist

Before finalizing slides:
- [ ] Each dir contains a question, test, and solution
- [ ] Table-driven tests have logic order for subcases (logically from small to big or alphabetically based on the question logic)
- [ ] All code examples are tested and working
- [ ] Do not add docs. Try to use self commented code
