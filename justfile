set positional-arguments

# List available recipes
default:
    @just --list

# One-time dev setup: install dependencies and git hooks
setup: sync
    lefthook install

# Run the whole suite, or part of it: `just test lists/sublists`
test *target:
    uv run pytest "$@"

# What the Grade Calculator workflow runs
grade:
    uv run pytest -n auto --tb=no --continue-on-collection-errors

# Run one solution script: `just run intro/average/average.py`
run file:
    uv run "{{ file }}"

lint:
    uv run ruff check .

fmt:
    uv run ruff format .

# Lint then format, in the lefthook ruff hook's order; format runs even if unfixable lint errors remain
fix:
    -uv run ruff check --fix .
    uv run ruff format .

# Run the code examples in the docs and exercises, and check what they show
examples:
    uv run scripts/check_examples.py

# Check index.toml's labels, and warn of code that uses a skill before the docs teach it
order:
    uv run scripts/check_order.py

# What the Lint workflow runs
check: lint order examples
    uv run ruff format --check .

# Install/refresh dependencies (unrelated to the "Sync to Main" workflow)
sync:
    uv sync
