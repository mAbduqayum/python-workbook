# Creating Your First Python Project

This guide walks you through creating a Python project of your own and running
your first program in it. The workbook's exercises don't need one: the workbook
you cloned is already a Python project.

## Create Your First Python Project

1. Open Terminal
2. Navigate to where you want to create your project (ex. `~/repos`):

   ```
   cd ~/repos
   ```

3. Create a new Python project with uv:

   ```
   uv init --python 3.15 first-project
   ```

4. Move into your new project folder:

   ```
   cd first-project
   ```

## Open Your Project in PyCharm

1. While in your project folder in the terminal, type:

   ```
   pycharm .
   ```

   (This opens the current folder in PyCharm)

2. If your terminal doesn't know the `pycharm` command, start PyCharm, click
   **Open** on its welcome screen (or **File → Open**), and choose your
   `first-project` folder.

## Understanding Your Project

When you used `uv init`, it created several files, including:

- `pyproject.toml` - Contains project settings
- `.python-version` - Contains the Python version
- `README.md` - Information about your project

The others can stay as they are.

## Write Your First Program

1. In PyCharm, right-click the `first-project` folder, choose
   **New → Python File**, type `hello`, and press Enter
2. Type into `hello.py`:

```python
print("Hello, World!")
print("I'm learning Python!")
```

## Run Your Program

1. In PyCharm, open the terminal (View → Tool Windows → Terminal)
2. Run your program with:

   ```
   uv run hello.py
   ```

3. You should see your messages printed in the terminal

## What Just Happened?

- **uv init** created a complete Python project structure for you
- **PyCharm** is where you write and edit your code
- **uv run** executes your Python programs in the project's managed environment
- **Python** is the language that understands your code and makes it work

## Common Commands You'll Use

- `cd` - **C**hange **D**irectory
- `uv init --python 3.15 project-name` - Create a new Python project
- `pycharm .` - Open the current folder in PyCharm
- `uv run hello.py` - Run a Python file
- `uv run pytest path/to/exercise/` - Test an exercise solution

Congratulations! You now have a Python project of your own, ready for any program you want to write.
To learn how the workbook's exercises work, read [`working_through_an_exercise.md`](../../intro/_docs/working_through_an_exercise.md).
