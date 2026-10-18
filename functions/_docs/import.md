# Importing Modules in Python

A **module** is a file of ready-made Python code: functions, variables, and
constants you can use in your own programs. Python comes with many modules,
such as `math` and `random`. To use one, you **import** it.

## Importing an Entire Module

```python
import math

result = math.sqrt(16)  # 4.0
area = math.pi * 5 ** 2  # 78.53981633974483
```

When you `import math`, you must use the `math.` prefix to access its
functions. This makes it clear where each function comes from.

## Importing Specific Functions

```python
from math import sqrt, pi

result = sqrt(16)  # 4.0
area = pi * 5 ** 2  # 78.53981633974483
```

No prefix is needed, which keeps code shorter when you use the same functions
many times.

## Using Aliases

```python
import math as m

result = m.sqrt(16)  # 4.0
```

## Avoid Importing Everything

```python
from math import *  # Not recommended
```

It hides which names come from which module, and the imported names can
silently replace your own.

## Where to Place Imports

Put all imports at the top of your file, before any functions:

```python
import math


def calculate_area(radius):
    return math.pi * radius ** 2
```

## Built-in Modules You Already Know

| Module   | Used for                     | Reference                                                        |
|----------|------------------------------|------------------------------------------------------------------|
| `math`   | Math functions and constants | [`math_functions.md`](../../intro/_docs/math_functions.md)       |
| `random` | Random numbers               | [`random_numbers.md`](../../repetitions/_docs/random_numbers.md) |

## Exploring a Module

- `help(math)` shows the documentation of a module
- `dir(math)` lists everything a module contains

## Common Errors

```python
import maths
# ModuleNotFoundError: No module named 'maths'

from math import square_root
# ImportError: cannot import name 'square_root' from 'math'
```

Check the spelling of the module or function name.

```python
from math import sqrt

def sqrt(x):  # Oops! Replaces the imported sqrt
    return x ** 0.5
```

Don't reuse imported names for your own functions, or use `import math` and
write `math.sqrt`.

## Next Steps

To create modules of your own, see [`modules.md`](modules.md).
