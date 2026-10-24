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

# What the Lint workflow runs
check: lint
    uv run ruff format --check .

# Install/refresh dependencies (unrelated to the "Sync to Main" workflow)
sync:
    uv sync

# Build the book: book/build/python-workbook.pdf
book: (_book "compile")

# Rebuild the book on every content edit; rerun after adding or removing an exercise or doc
book-watch: (_book "watch")

# The same build the Book workflow runs, stamped with the current commit
_book mode:
    uv run book/manifest.py
    SOURCE_DATE_EPOCH="$(git log -1 --format=%ct)" typst "{{ mode }}" --root . --ignore-system-fonts \
        --input commit="$(git rev-parse --short HEAD)" \
        --input date="$(git log -1 --format=%cs)" \
        --input repo="$(git remote get-url origin | sed -E 's#^git@([^:]+):#https://\1/#; s#\.git$##')" \
        book/main.typ book/build/python-workbook.pdf
