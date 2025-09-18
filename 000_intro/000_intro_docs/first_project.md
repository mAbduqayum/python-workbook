# Getting Started with Python Programming

Welcome to Python! This guide will help you set up everything you need to start programming in Python.

## What You'll Need

1. **Python** - The programming language itself
2. **VS Code** - A text editor for writing your code
3. **uv** - A tool to manage Python versions and packages

## Step 1: Install VS Code

1. Go to https://code.visualstudio.com/
2. Click the big blue "Download" button
3. Run the installer and follow the instructions
4. Open VS Code when installation is complete

## Step 2: Install uv

uv is a fast Python package manager that will help you install Python and manage your projects.

### On Windows:

1. Press `Windows key + R`
2. Type `cmd` and press Enter
3. Copy and paste this command, then press Enter:
   ```
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

### On Mac:

1. Press `Cmd + Space`
2. Type "Terminal" and press Enter
3. Copy and paste this command, then press Enter:
   ```
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

### On Linux:

1. Open Terminal (usually Ctrl+Alt+T)
2. Copy and paste this command, then press Enter:
   ```
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

After installation, close and reopen your terminal/command prompt.

## Step 3: Create Your First Python Project

1. Open Terminal (Mac/Linux) or Command Prompt (Windows)
2. Navigate to where you want to create your project (like your Desktop):
   ```
   cd Documents
   ```
3. Create a new Python project with uv:
   ```
   uv init first-project
   ```
4. Move into your new project folder:
   ```
   cd first-project
   ```

## Step 4: Open Your Project in VS Code

1. While in your project folder in the terminal, type:
   ```
   code .
   ```
   (This opens the current folder in VS Code)

2. If VS Code doesn't open, you can:
    - Open VS Code manually
    - Go to File the Open Folder
    - Select your `first-project` folder

## Step 5: Install Python Extension

1. In VS Code, click on the Extensions icon on the left side (it looks like building blocks)
2. Search for "Python"
3. Install the official Python extension by Microsoft (it should be the first result)

## Step 6: Understanding Your Project

When you used `uv init`, it created several files:

- `pyproject.toml` - Contains project settings
- `.python-version` - Contains the python version
- `README.md` - Information about your project
- `main.py` - A sample Python file

## Step 7: Write Your First Program

1. Open the `main.py` file (it should already exist)
2. Replace its contents with:

```python
print("Hello, World!")
print("I'm learning Python!")
```

## Step 8: Run Your Program

1. In VS Code, open the terminal (Terminal → New Terminal)
2. Run your program with:
   ```
    python main.py
   ```
3. You should see your messages printed in the terminal

## What Just Happened?

- **uv init** created a complete Python project structure for you
- **VS Code** is where you write and edit your code
- **python** executes your Python programs in a safe environment
- **Python** is the language that understands your code and makes it work

## Common Commands You'll Use

- `python main.py` - Run a Python file
- `uv init project-name` - Create a new Python project
- `code .` - Open the current folder in VS Code

## Tips for Success

- Always work inside a project folder created with `uv init`
- Use `uv run` to run your Python files
- Save your files before running them (Ctrl+S or Cmd+S)
- If you see red squiggly lines, VS Code is showing you errors to fix

## Getting Help

- Red squiggly lines in VS Code point out problems in your code
- The terminal shows error messages if something goes wrong
- Google error messages if you get stuck - other people have had the same problems!

Congratulations! You now have a proper Python development setup and you're ready to start programming.
