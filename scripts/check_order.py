"""Check the index, and flag code that uses a skill before the docs teach it.

index.toml lists, for each term, the sections that teach it, and the first of
them in reading order is where the term is taught. The reading order is
README's: each topic's docs, then its exercises, and the appendix last. This
script reads the code a reader meets: the python blocks of the docs, exercises
and hints, and each exercise's solution, the program the exercise asks for. It
finds the terms the code uses, from keywords, operators, built-in functions,
methods and modules to constructs such as comprehensions and slices, and flags
a use on a page before the one that teaches the term. A page may use a term it
teaches itself, since its examples often come before the section that explains
them. A hint's code counts as its exercise's.

The uses it finds are warnings, not failures: a page may use a term early on
purpose, as set_best_practices.md shows `{}` making a dict to warn against it.
What fails is a label for a heading that is gone, as renaming the heading
leaves it. Labels for the book's own pages, such as getting-started, are left
to the book's build.

Usage: uv run scripts/check_order.py
"""

import ast
import builtins
import io
import posixpath
import re
import sys
import tokenize
import tomllib
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "index.toml"
README = "README.md"
APPENDIX_TOC = "appendix/_docs/_table_of_contents.md"

PYTHON_FENCE = re.compile(r"^```python[^\n]*\n(.*?)^```", re.MULTILINE | re.DOTALL)
FENCE = re.compile(r"^```.*?^```", re.MULTILINE | re.DOTALL)
INLINE_CODE = re.compile(r"`[^`\n]*`")
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
EXTERNAL = re.compile(r"^[a-z][a-z0-9+.-]*:", re.IGNORECASE)
HEADING = re.compile(r"^#{1,6}[ \t]+(.+?)[ \t]*$", re.MULTILINE)
# A label for a page of this repo; the book's own pages have labels of their own.
WORKBOOK_LABEL = re.compile(r"\A(?:doc|ex|hint|appendix):")

# Keywords the code shows as words; and, or, not, in and is come from the
# syntax tree instead, since `for x in` and `is not` hold them too.
KEYWORDS = {
    "as", "assert", "break", "continue", "def", "del", "elif", "else", "except", "False",
    "finally", "for", "global", "if", "None", "raise", "return", "True", "try", "while", "with",
}  # fmt: skip
OPERATORS = {
    ast.Add: "`+`", ast.Sub: "`-`", ast.Mult: "`*`", ast.Div: "`/`", ast.FloorDiv: "`//`",
    ast.Mod: "`%`", ast.Pow: "`**`", ast.BitOr: "`|`", ast.BitAnd: "`&`", ast.BitXor: "`^`",
    ast.Eq: "`==`", ast.NotEq: "`!=`", ast.Lt: "`<`", ast.LtE: "`<=`", ast.Gt: "`>`",
    ast.GtE: "`>=`", ast.Is: "`is`", ast.IsNot: "`is`", ast.In: "`in`", ast.NotIn: "`in`",
    ast.And: "`and`", ast.Or: "`or`", ast.Not: "`not`",
}  # fmt: skip
COMPREHENSIONS = {
    ast.ListComp: "comprehension › list",
    ast.SetComp: "comprehension › set",
    ast.DictComp: "comprehension › dictionary",
}
LITERALS = {
    ast.List: "list › creating",
    ast.Set: "set › creating",
    ast.Dict: "dictionary › creating",
}
MAIN_GUARD = '`if __name__ == "__main__"`'


@dataclass
class Page:
    path: str
    label: str
    # Its place in reading order; a hint shares its exercise's.
    order: int


@dataclass
class Use:
    term: str
    path: str
    line: int
    order: int


# Where the docs teach each term.


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def section(markdown: str, heading: str) -> str:
    """Body of the ``## heading`` section, up to the next ``##`` heading."""
    match = re.search(
        rf"^## {re.escape(heading)}\s*$(.*?)(?=^## |\Z)",
        markdown,
        re.MULTILINE | re.DOTALL,
    )
    if match is None:
        return ""
    return match.group(1)


def linked_paths(source: str, markdown: str) -> list[str]:
    """The repo paths ``markdown``'s links lead to, in order, leaving out code and the web."""
    prose = INLINE_CODE.sub("", FENCE.sub("", markdown))
    paths = []
    for target in LINK.findall(prose):
        if not EXTERNAL.match(target):
            file = target.partition("#")[0]
            paths.append(
                posixpath.normpath(posixpath.join(posixpath.dirname(source), file))
            )
    return paths


def stem(path: str) -> str:
    return posixpath.splitext(posixpath.basename(path))[0]


def reading_order() -> list[Page]:
    """The pages in README's reading order, labeled as the book labels them.

    Each topic's table of contents lists its docs, then its exercises; a hint
    is read beside its exercise. The appendix comes last.
    """
    pages = []
    chapters = section(read(README), "Recommended Reading Order")
    for toc in linked_paths(README, chapters):
        topic = posixpath.basename(posixpath.dirname(posixpath.dirname(toc)))
        markdown = read(toc)
        for doc in linked_paths(toc, section(markdown, "Recommended Reading Order")):
            pages.append(Page(doc, f"doc:{topic}:{stem(doc)}", len(pages)))
        for statement in linked_paths(toc, section(markdown, "Practice Questions")):
            name = stem(statement)
            order = len(pages)
            pages.append(Page(statement, f"ex:{topic}:{name}", order))
            hint = f"{posixpath.dirname(statement)}/{name}_hint.md"
            if (ROOT / hint).is_file():
                pages.append(Page(hint, f"hint:{topic}:{name}", order))
    appendix = section(read(APPENDIX_TOC), "Recommended Reading Order")
    for doc in linked_paths(APPENDIX_TOC, appendix):
        pages.append(Page(doc, f"appendix:{stem(doc)}", len(pages)))
    return pages


def by_label(pages: list[Page]) -> dict[str, Page]:
    found = {}
    for page in pages:
        found[page.label] = page
    return found


def index_entries(index: dict) -> list[tuple[str, list[str]]]:
    """Each term with its labels, a term's sub-entries before the term itself.

    A sub-entry is named `comprehension › list`, and a term with sub-entries
    has all of their labels.
    """
    entries = []
    for term, value in index.items():
        if isinstance(value, list):
            entries.append((term, value))
        elif isinstance(value, dict):
            whole = []
            for subentry, labels in value.items():
                entries.append((f"{term} › {subentry}", labels))
                whole.extend(labels)
            entries.append((term, whole))
    return entries


def anchors(markdown: str) -> set[str]:
    """The anchors of a page's headings, as GitHub and the book make them.

    `is` and `==` -> is-and-; a repeated heading gets -1, -2.
    """
    found = set()
    seen = {}
    for heading in HEADING.findall(FENCE.sub("", markdown)):
        anchor = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        count = seen.get(anchor, 0)
        seen[anchor] = count + 1
        found.add(anchor if count == 0 else f"{anchor}-{count}")
    return found


def stale_labels(entries: list[tuple[str, list[str]]], pages: list[Page]) -> list[str]:
    """The labels for this repo's pages that name a page or a heading it lacks."""
    pages_by_label = by_label(pages)
    text = INDEX.read_text(encoding="utf-8")
    checked = set()
    problems = []
    for term, labels in entries:
        for label in labels:
            if label in checked or not WORKBOOK_LABEL.match(label):
                continue
            checked.add(label)
            line = text[: text.find(f'"{label}"')].count("\n") + 1
            page = page_of(label, pages_by_label)
            if page is None:
                problems.append(
                    f"index.toml:{line}: {term} names {label}, a page the reading order lacks"
                )
                continue
            anchor = label[len(page.label) + 1 :]
            if anchor and anchor not in anchors(read(page.path)):
                problems.append(
                    f"index.toml:{line}: {term} names {label}, a heading {page.path} lacks"
                )
    return problems


def page_of(label: str, pages_by_label: dict[str, Page]) -> Page | None:
    """The page a heading's label is on: doc:lists:tuple:creating-tuples is on doc:lists:tuple."""
    parts = label.split(":")
    while parts:
        page = pages_by_label.get(":".join(parts))
        if page is not None:
            return page
        parts.pop()
    return None


def teaching_pages(
    entries: list[tuple[str, list[str]]], pages: list[Page]
) -> dict[str, Page]:
    """The first page that teaches each term.

    A term with sub-entries is taught where its first sub-entry is.
    """
    pages_by_label = by_label(pages)
    taught_in = {}
    for term, labels in entries:
        for label in labels:
            page = page_of(label, pages_by_label)
            if page is not None and (
                term not in taught_in or page.order < taught_in[term].order
            ):
                taught_in[term] = page
    return taught_in


# The terms code uses.


def bound_names(tree: ast.AST) -> set[str]:
    """The names the code sets itself, which may hide a built-in: `sum = 0`."""
    names = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
            names.add(node.id)
        elif isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            names.add(node.name)
        elif isinstance(node, ast.arg):
            names.add(node.arg)
        elif isinstance(node, ast.alias):
            names.add((node.asname or node.name).split(".")[0])
        elif isinstance(node, ast.ExceptHandler) and node.name:
            names.add(node.name)
    return names


def is_main_guard(node: ast.If) -> bool:
    test = node.test
    return (
        isinstance(test, ast.Compare)
        and isinstance(test.left, ast.Name)
        and test.left.id == "__name__"
        and len(test.comparators) == 1
        and isinstance(test.comparators[0], ast.Constant)
        and test.comparators[0].value == "__main__"
    )


def calls_itself(function: ast.FunctionDef) -> bool:
    for node in ast.walk(function):
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == function.name
        ):
            return True
    return False


def has_docstring(function: ast.FunctionDef) -> bool:
    first = function.body[0]
    return (
        isinstance(first, ast.Expr)
        and isinstance(first.value, ast.Constant)
        and isinstance(first.value.value, str)
    )


def module_path(node: ast.expr, modules: dict[str, str]) -> str | None:
    """The module an expression names: os.path for `os.path`, after `import os`."""
    if isinstance(node, ast.Name):
        return modules.get(node.id)
    if isinstance(node, ast.Attribute):
        module = module_path(node.value, modules)
        if module is not None:
            return f"{module}.{node.attr}"
    return None


def type_hint_nodes(tree: ast.AST) -> set[int]:
    """The ids of the nodes in type hints.

    A hint names a type, `-> tuple[int, int]`, without calling it.
    """
    found = set()
    for node in ast.walk(tree):
        hint = None
        if isinstance(node, ast.FunctionDef):
            hint = node.returns
        elif isinstance(node, (ast.arg, ast.AnnAssign)):
            hint = node.annotation
        if hint is not None:
            for part in ast.walk(hint):
                found.add(id(part))
    return found


def called_nodes(tree: ast.AST) -> set[int]:
    """The ids of the nodes that are called.

    A method is used in `words.count(w)`, not in `self.count = 0`.
    """
    found = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            found.add(id(node.func))
    return found


def terms_used(source: str, terms: set[str]) -> list[tuple[str, int]]:
    """Each term of the index the code uses, with the line it is used on."""
    tree = ast.parse(source)
    used = []
    for token in tokenize.generate_tokens(io.StringIO(source).readline):
        if token.type == tokenize.NAME and token.string in KEYWORDS:
            used.append((f"`{token.string}`", token.start[0]))
        elif token.type == tokenize.COMMENT:
            used.append(("`#`", token.start[0]))

    own = bound_names(tree)
    in_hints = type_hint_nodes(tree)
    called = called_nodes(tree)
    # What an imported name stands for: m -> math, sqrt -> math.sqrt.
    modules = {}
    imported = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                modules[alias.asname or alias.name] = alias.name
                # Importing a module is taught with the module.
                term = f"`{alias.name}` module"
                used.append((term if term in terms else "`import`", node.lineno))
        elif isinstance(node, ast.ImportFrom):
            used.append(("`from`", node.lineno))
            used.append((f"`{node.module}` module", node.lineno))
            for alias in node.names:
                imported[alias.asname or alias.name] = f"{node.module}.{alias.name}"
                used.append((f"`{alias.name}`", node.lineno))
                used.append((f"`{node.module}.{alias.name}`", node.lineno))

    for node in ast.walk(tree):
        line = getattr(node, "lineno", None)
        if id(node) in in_hints:
            continue
        if isinstance(node, (ast.BinOp, ast.UnaryOp, ast.BoolOp)):
            used.append((OPERATORS.get(type(node.op), ""), line))
        elif isinstance(node, ast.AugAssign):
            used.append(("augmented assignment", line))
            if isinstance(node.op, ast.Add):
                used.append(("`+=`", line))
        elif isinstance(node, ast.Compare):
            for op in node.ops:
                used.append((OPERATORS[type(op)], line))
            if len(node.ops) > 1:
                used.append(("chained comparisons", line))
        elif isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
            if node.id in imported:
                used.append((f"`{imported[node.id]}`", line))
                used.append((f"`{imported[node.id]}()`", line))
            elif node.id not in own and hasattr(builtins, node.id):
                used.append((f"`{node.id}()`", line))
                used.append((f"`{node.id}`", line))
        elif isinstance(node, ast.Attribute):
            module = module_path(node.value, modules)
            if module is not None:
                used.append((f"`{module}.{node.attr}`", line))
                used.append((f"`{module}.{node.attr}()`", line))
            elif id(node) in called:
                used.append((f"`{node.attr}()`", line))
        elif isinstance(node, ast.Subscript) and isinstance(node.slice, ast.Slice):
            used.append(("slice", line))
        elif type(node) in COMPREHENSIONS:
            used.append((COMPREHENSIONS[type(node)], line))
        elif type(node) in LITERALS and isinstance(
            getattr(node, "ctx", ast.Load()), ast.Load
        ):
            used.append((LITERALS[type(node)], line))
        elif isinstance(node, ast.JoinedStr):
            used.append(("f-string › basics", line))
        elif isinstance(node, (ast.Assign, ast.For)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            for target in targets:
                if isinstance(target, (ast.Tuple, ast.List)):
                    used.append(("unpacking", line))
        elif isinstance(node, ast.Match):
            used.append(("`match`", line))
            used.append(("`case`", node.cases[0].pattern.lineno))
        elif isinstance(node, ast.If) and is_main_guard(node):
            used.append((MAIN_GUARD, line))
        elif isinstance(node, ast.FunctionDef):
            if node.args.defaults or any(node.args.kw_defaults):
                used.append(("default parameter values", line))
            if node.returns is not None:
                used.append(("`->`", line))
                used.append(("type hint", line))
            for argument in node.args.args:
                if argument.annotation is not None:
                    used.append(("type hint", line))
            if has_docstring(node):
                used.append(("docstring", node.body[0].lineno))
            if calls_itself(node):
                used.append(("recursion", line))
        elif isinstance(node, ast.AnnAssign):
            used.append(("type hint", line))

    kept = []
    for term, line in used:
        if term in terms:
            kept.append((term, line))
    return kept


# Reading the pages' code.


def solution_of(statement: str) -> Path:
    folder = ROOT / posixpath.dirname(statement)
    return folder / f"{folder.name}.py"


def uses_on(page: Page, terms: set[str]) -> list[Use]:
    """The ``terms`` the code on ``page`` uses, and its exercise's solution."""
    uses = []
    markdown = read(page.path)
    for found in PYTHON_FENCE.finditer(markdown):
        start = markdown[: found.start(1)].count("\n") + 1
        try:
            block_terms = terms_used(found.group(1), terms)
        except (SyntaxError, tokenize.TokenError):
            # A syntax outline, `if condition:` over a comment.
            continue
        for term, line in block_terms:
            uses.append(Use(term, page.path, start + line - 1, page.order))
    if page.label.startswith("ex:"):
        solution = solution_of(page.path)
        if solution.is_file():
            path = solution.relative_to(ROOT).as_posix()
            for term, line in terms_used(read(path), terms):
                uses.append(Use(term, path, line, page.order))
    return uses


def report_early(early: dict[str, list[Use]], taught_in: dict[str, Page]) -> None:
    if not early:
        print("Skill order: no code uses a term before the page that teaches it")
        return
    count = 0
    for found in early.values():
        count += len(found)
    print(
        f"Skill order: {count} use(s) of {len(early)} term(s) before the page that teaches them",
        file=sys.stderr,
    )
    for term in sorted(early, key=lambda term: taught_in[term].order):
        print(f"  {term}, taught in {taught_in[term].path}:", file=sys.stderr)
        seen = set()
        for use in early[term]:
            # One line per file, at the first use in it.
            if use.path in seen:
                continue
            seen.add(use.path)
            print(f"    {use.path}:{use.line}", file=sys.stderr)


def main() -> None:
    entries = index_entries(tomllib.loads(INDEX.read_text(encoding="utf-8")))
    pages = reading_order()
    taught_in = teaching_pages(entries, pages)
    terms = set(taught_in)

    early: dict[str, list[Use]] = {}
    for page in pages:
        for use in uses_on(page, terms):
            if use.order < taught_in[use.term].order:
                early.setdefault(use.term, []).append(use)
    report_early(early, taught_in)

    stale = stale_labels(entries, pages)
    if stale:
        print(
            f"Index: {len(stale)} label(s) for a heading that is gone", file=sys.stderr
        )
        for problem in stale:
            print(f"  {problem}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
