## 200_repetitions
- n numbers
- n even numbers
- n odd numbers
- n numbers divisible by 10
- read input from the user until user enters
skip (continue) or quit (break)
- table of numbers:
 1  2   3   4   5   6   7   8   9   10
11 12  13                           20
.
.
.
91 ...                             100

### Todos
-[ ] collatz question: output in multiple lines to make it easier

## 300_functions
- time_it (which prints how much time did a function take?)

## Test Refactoring

### High Priority
- [ ] Extract script path boilerplate - create fixture/helper to eliminate 4-5 lines per test
  ```python
  # Current (repeated everywhere):
  script_path = Path(__file__).parent / "script_name.py"
  if not script_path.exists():
      pytest.skip("Solution file script_name.py not found")
  runner = script_runner(script_path)
  ```
- [ ] Standardize function import pattern for 300_functions tests
  ```python
  # Current (repeated in every function test):
  try:
      from function_name import function_name
  except ImportError:
      function_name = None
  @pytest.mark.skipif(function_name is None, reason="...")
  ```

### Medium Priority
- [ ] Standardize output checking methods (3 different patterns exist)
  - `run_and_check_output_only()`
  - `run_and_check()`
  - `result = runner.run(); assert expected in result.stdout`
- [ ] Add more assertion helpers to ScriptRunner class
  - `assert_output_contains()` for multiple string checks
  - `assert_numeric_output()` for float comparisons

### Low Priority
- [ ] Externalize large parametrize test data (e.g., sound_levels with 16 cases)
- [ ] Consider test base classes for different test types (script tests vs function tests)
