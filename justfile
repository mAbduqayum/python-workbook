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

# Force main to match pushed solutions, minus solution scripts and .mainignore paths
mirror-main:
    #!/usr/bin/env bash
    set -eu
    git fetch -q origin
    # Build main's files in a scratch index, leaving the working tree alone
    export GIT_INDEX_FILE=$(mktemp)
    git read-tree origin/solutions
    git ls-files | grep -E '^([^/]+)/([^/]+)/\2\.py$' | xargs git rm -qf --cached
    git show origin/solutions:.mainignore | grep -v -e '^#' -e '^$' | xargs git rm -qrf --cached --ignore-unmatch
    tree=$(git write-tree) && rm "$GIT_INDEX_FILE"
    if [ "$tree" = "$(git rev-parse 'origin/main^{tree}')" ]; then echo "main already mirrors solutions"; exit; fi
    # The Source-commit trailer is where the Sync to Main workflow resumes
    git push origin "$(git commit-tree "$tree" -p origin/main -m 'ref: mirror main from solutions' -m "Source-commit: $(git rev-parse origin/solutions)"):refs/heads/main"

