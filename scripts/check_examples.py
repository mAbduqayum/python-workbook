"""Run the code examples in the docs and exercises, and check what they show.

A page shows what its code gives in a few ways, and this script runs the code
and compares each:

- a comment after a line, `print(len(text))  # 11`, or comment lines right
  under it, with or without an `# Output:` line first;
- the **Output:** block printed under a python block;
- a table row whose Example (or Call, or Expression) cell and Result (or
  Output, or Returns) cell are each `code`;
- an exercise's examples: the solution reads the input block and must print
  the output block.

A page's python blocks run in turn in one namespace, as a reader would type
them, in a scratch folder. A block labeled **File: `name.py`** is saved under
that name instead, and run only if it is `main.py`. An exercise's blocks,
tables and examples run against its solution, the reference the tests check,
and its hint's blocks do too; so the script runs on `solutions` only.

Most snippets are not complete programs: a syntax outline, a function the
page never calls, a file the reader is meant to have. So a snippet that fails
is only a problem when the failure hides an output the page shows. Comments
that describe a line rather than show its output are told apart by their
words: a comment is prose when it uses a word the output does not. A block
that reads input() runs only as an exercise example, which supplies the input.

Usage: uv run scripts/check_examples.py
"""

import ast
import builtins
import io
import math
import os
import posixpath
import random
import re
import shutil
import signal
import sys
import tempfile
import tokenize
from contextlib import redirect_stdout
from dataclasses import dataclass, field
from pathlib import Path
from typing import NamedTuple

ROOT = Path(__file__).resolve().parent.parent

PYTHON_FENCE = re.compile(r"^```python[^\n]*\n(.*?)^```", re.MULTILINE | re.DOTALL)
# A label on the line before a block: **File: `geometry.py`**.
FILE_LABEL = re.compile(r"\*\*File: `([^`]+)`[^*]*\*\*\s*\Z")
# The plain block of what the python block above it prints.
OUTPUT_BLOCK = re.compile(
    r"\A\s*\*\*Output:\*\*\s*\n\s*```\n(.*?)^```", re.MULTILINE | re.DOTALL
)
# An exercise's example, as pw-book's template/examples.typ reads it: an input
# block and an output block, or the output block alone of a program that reads
# nothing.
EXAMPLE = re.compile(
    r"^\*\*Example \d+:[ \t]*(.*?)\*\*(.*)\n\s*```\n((?s:.*?))^```[ \t]*\n?(?:\s*```\n((?s:.*?))^```[ \t]*\n?)?",
    re.MULTILINE,
)
TABLE_DIVIDER = re.compile(r"^\|[\s:|-]+\|\s*$")
CODE_SPAN = re.compile(r"\A`([^`]+)`\Z")
# A table is one of examples when its header names a code column and, to its
# right, a result column.
CODE_HEADERS = ("example", "call", "expression")
RESULT_HEADERS = ("result", "output", "returns", "generated values")

# How a comment says what a line gives, and how it goes on to explain it.
HEADER = re.compile(
    r"\A(?:output|prints?|returns?|result)\s*:\s*|\A(?:->|→|=>)\s*", re.IGNORECASE
)
LEADING_VERB = re.compile(r"\A(?:returns?|prints?|gives)\s+", re.IGNORECASE)
EXPLANATION = re.compile(r"\s+(?:-|—|\()|,\s+(?=[a-z]+\b(?!\s*[\],)]))")
ALTERNATIVE = re.compile(r"\s+or\s+")
ELLIPSIS_NUMBER = re.compile(r"(-?\d+\.\d+)\.\.\.")
WORD = re.compile(r"[A-Za-z]{2,}")
# Words in a comment that say the line fails on purpose.
FAILS_ON_PURPOSE = re.compile(
    r"error|exception|crash|raises|infinite|forever|never stops|slow|seconds",
    re.IGNORECASE,
)
# An exercise that leaves the order of its answer open:
# "Order of the sublists doesn't matter".
ANY_ORDER = re.compile(
    r"\border\b[^.\n]*\b(?:doesn't|does not|don't|do not) matter|\bin any order\b",
    re.IGNORECASE,
)

STATEMENT_TIME_LIMIT_SECONDS = 2
PRINTED_CHARS_LIMIT = 100_000
# Where an expression's value is kept, to compare with what the page shows.
VALUE_NAME = "_value"
# Where a table example keeps the literal it calls a method on: `[1, 2].append(3)`.
RECEIVER_NAME = "_literal"


class Stopped(BaseException):
    """Ends a snippet that runs too long, prints too much or reads input.

    A BaseException, so a snippet's own `except Exception:` lets it through.
    """


class ReadsInput(Stopped):
    pass


def stop_running(signum, frame) -> None:
    raise Stopped(f"still running after {STATEMENT_TIME_LIMIT_SECONDS}s")


@dataclass
class Printed:
    """One call to print(): its text, and where in the block it came from."""

    text: str
    # The line of the block's own top-level code that led to it: the call
    # of a function the block defined, not the print() inside the function.
    line: int
    # Every line of the block on the call stack.
    lines: set[int]


@dataclass
class Failure:
    error: BaseException
    lines: set[int]


@dataclass
class Page:
    """A markdown page of the workbook, and the namespace its code runs in."""

    path: str
    namespace: dict
    folder: Path
    # A list it shows may hold its items in any order.
    any_order: bool = False
    findings: list[str] = field(default_factory=list)
    checked: int = 0
    unchecked: int = 0

    def problem(self, line: int, message: str) -> None:
        self.findings.append(f"{self.path}:{line}: {message}")

    def broke(self, error: Exception) -> None:
        """This check failed on the page: report it, and go on to the next page."""
        self.findings.append(
            f"{self.path}: checking it raised {type(error).__name__}: {error}"
        )


# Recording what the code prints.


class Recorder:
    """Stands in for print() while a block runs, noting where each call came from."""

    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.printed: list[Printed] = []
        self.chars_printed = 0

    def print(self, *args, sep=" ", end="\n", file=None, flush=False) -> None:
        if file is not None and file is not sys.stdout:
            REAL_PRINT(*args, sep=sep, end=end, file=file, flush=flush)
            return
        if sep is None:
            sep = " "
        if end is None:
            end = "\n"
        texts = []
        for arg in args:
            texts.append(str(arg))
        text = sep.join(texts) + end
        self.chars_printed += len(text)
        if self.chars_printed > PRINTED_CHARS_LIMIT:
            raise Stopped(f"printed more than {PRINTED_CHARS_LIMIT:,} characters")
        lines = set()
        outermost = None
        frame = sys._getframe(1)
        while frame is not None:
            if frame.f_code.co_filename == self.filename:
                lines.add(frame.f_lineno)
                outermost = frame.f_lineno
            frame = frame.f_back
        self.printed.append(Printed(text, outermost or 0, lines))


REAL_PRINT = builtins.print
REAL_INPUT = builtins.input


def refuse_input(prompt: object = "") -> str:
    raise ReadsInput("reads input")


def run_statement(code, namespace: dict, recorder: Recorder) -> BaseException | None:
    """Run one compiled statement; return the error it raised, if any."""
    builtins.print = recorder.print
    signal.setitimer(signal.ITIMER_REAL, STATEMENT_TIME_LIMIT_SECONDS)
    try:
        with redirect_stdout(io.StringIO()):
            exec(code, namespace)
    except BaseException as error:  # the snippet's own, to report or excuse
        return error
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        builtins.print = REAL_PRINT
    return None


def assignment(
    name: str, value: ast.expr, filename: str = "<table>", at: ast.stmt | None = None
):
    """`name = value`, compiled, on the lines of the statement ``at``."""
    statement = ast.Assign([ast.Name(name, ast.Store())], value)
    if at is not None:
        ast.copy_location(statement, at)
    module = ast.fix_missing_locations(ast.Module([statement], []))
    return compile(module, filename, "exec")


def evaluate(source: str, namespace: dict) -> tuple[object, BaseException | None]:
    """The value of a table's example: an expression, or the name an assignment sets.

    A method called on a literal, `[1, 2].append(3)`, changes the literal and
    returns None; its value is then the literal, as the table shows it.
    """
    tree = ast.parse(source)
    if len(tree.body) != 1:
        raise SyntaxError("not one statement")
    statement = tree.body[0]
    recorder = Recorder("<table>")
    if isinstance(statement, ast.Expr):
        expression = statement.value
        on_literal = (
            isinstance(expression, ast.Call)
            and isinstance(expression.func, ast.Attribute)
            and isinstance(expression.func.value, (ast.List, ast.Dict, ast.Set))
        )
        if on_literal:
            literal_node = expression.func.value
            expression.func.value = ast.Name(RECEIVER_NAME, ast.Load())
            error = run_statement(
                assignment(RECEIVER_NAME, literal_node), namespace, recorder
            )
            if error is not None:
                return None, error
        error = run_statement(assignment(VALUE_NAME, expression), namespace, recorder)
        value = namespace.pop(VALUE_NAME, None)
        receiver = namespace.pop(RECEIVER_NAME, None)
        if on_literal and value is None:
            value = receiver
        return value, error
    if (
        isinstance(statement, ast.Assign)
        and len(statement.targets) == 1
        and isinstance(statement.targets[0], ast.Name)
    ):
        error = run_statement(compile(tree, "<table>", "exec"), namespace, recorder)
        return namespace.get(statement.targets[0].id), error
    raise SyntaxError("not an expression or an assignment")


# Reading what the page shows.


def comments(source: str) -> tuple[dict[int, str], dict[int, str]]:
    """The block's comments by line: those after code, and those on lines of their own."""
    trailing = {}
    whole_line = {}
    code_lines = set()
    for token in tokenize.generate_tokens(io.StringIO(source).readline):
        if token.type == tokenize.COMMENT:
            text = token.string.lstrip("#").strip()
            if token.start[0] in code_lines:
                trailing[token.start[0]] = text
            else:
                whole_line[token.start[0]] = text
        elif token.type not in (
            tokenize.NL,
            tokenize.NEWLINE,
            tokenize.INDENT,
            tokenize.DEDENT,
            tokenize.ENDMARKER,
        ):
            for line in range(token.start[0], token.end[0] + 1):
                code_lines.add(line)
    return trailing, whole_line


def readings(claim: str) -> list[str]:
    """The ways to read a comment as an output: whole, without its explanation, each alternative."""
    texts = [claim]
    without_verb = LEADING_VERB.sub("", claim)
    if without_verb != claim:
        texts.append(without_verb)
    for text in list(texts):
        for explanation in EXPLANATION.finditer(text):
            if explanation.start() > 0:
                texts.append(text[: explanation.start()])
    found = []
    for text in texts:
        found.append(text)
        if ALTERNATIVE.search(text):
            found.extend(ALTERNATIVE.split(text))
    return found


def literal(text: str) -> tuple[bool, object]:
    try:
        return True, ast.literal_eval(text)
    except (ValueError, TypeError, SyntaxError, MemoryError, RecursionError):
        return False, None


def in_any_order(items) -> list[str]:
    """Items to compare whatever order they come in."""
    found = []
    for item in items:
        found.append(repr(normal(item)))
    return sorted(found)


def normal(value: object) -> object:
    """A value to compare: a set's order is arbitrary, and `1` is not `True`."""
    if isinstance(value, (set, frozenset)):
        return ("set", in_any_order(value))
    if isinstance(value, (list, tuple)):
        items = []
        for item in value:
            items.append(normal(item))
        return (type(value).__name__, items)
    if isinstance(value, dict):
        items = []
        for key, item in value.items():
            items.append((normal(key), normal(item)))
        return ("dict", items)
    return (type(value).__name__, value)


def rounds_to(shown: str, actual: str) -> bool:
    """`1.5708` for 1.5707963267948966: a float shown to four or more places."""
    if not re.fullmatch(r"-?\d+\.\d{4,}", shown):
        return False
    try:
        number = float(actual)
    except ValueError:
        return False
    places = len(shown.split(".")[1])
    return math.isclose(round(number, places), float(shown))


def elided(shown: str, actual: str) -> bool:
    """`3.333...`, `[1, 2, ...]`: `...` stands for the rest, a number's for its digits."""
    numbers = []
    parts = []
    position = 0
    for found in ELLIPSIS_NUMBER.finditer(shown):
        parts.append(
            re.escape(shown[position : found.start()]).replace(r"\.\.\.", ".*?")
        )
        parts.append(r"(-?\d+(?:\.\d+)?(?:e-?\d+)?)")
        numbers.append(found.group(1))
        position = found.end()
    parts.append(re.escape(shown[position:]).replace(r"\.\.\.", ".*?"))
    match = re.fullmatch("".join(parts), actual, re.DOTALL)
    if match is None:
        return False
    for number, digits in zip(numbers, match.groups(), strict=True):
        places = len(number.split(".")[1])
        if not (
            digits.startswith(number)
            or math.isclose(round(float(digits), places), float(number))
        ):
            return False
    return True


def same(shown: str, actual: str) -> bool:
    if shown == actual or rounds_to(shown, actual):
        return True
    shown_is_literal, shown_value = literal(shown)
    if shown_is_literal:
        if isinstance(shown_value, str) and shown_value == actual:
            return True
        actual_is_literal, actual_value = literal(actual)
        if actual_is_literal and normal(shown_value) == normal(actual_value):
            return True
    return "..." in shown and elided(shown, actual)


def same_items(shown: str, actual: str) -> bool:
    """`[[3], [2]]` for [[2], [3]]: a list of the same items in another order."""
    shown_is_literal, shown_value = literal(shown)
    actual_is_literal, actual_value = literal(actual)
    return (
        shown_is_literal
        and actual_is_literal
        and isinstance(shown_value, list)
        and isinstance(actual_value, list)
        and in_any_order(shown_value) == in_any_order(actual_value)
    )


def agrees(claim: str, forms: list[str], any_order: bool = False) -> bool:
    for reading in readings(claim):
        for form in forms:
            if same(reading, form) or (any_order and same_items(reading, form)):
                return True
    return False


def is_prose(claim: str, forms: list[str]) -> bool:
    """A comment that describes a line rather than show what it gives.

    It uses a word that none of the line's outputs has.
    """
    shown = " ".join(forms).lower()
    core = LEADING_VERB.sub("", claim)
    for explanation in EXPLANATION.finditer(core):
        if explanation.start() > 0:
            core = core[: explanation.start()]
            break
    for word in WORD.findall(core):
        if word.lower() in ("true", "false", "none", "or"):
            continue
        if word.lower() not in shown:
            return True
    return False


def looks_like_output(claim: str) -> bool:
    """A comment whose line failed is a claim only if it reads as a value."""
    if HEADER.match(claim):
        return True
    for reading in readings(claim):
        if literal(reading)[0]:
            return True
    return False


def output_lines(text: str) -> list[str]:
    lines = []
    for line in text.split("\n"):
        lines.append(line.rstrip())
    while lines and lines[-1] == "":
        lines.pop()
    while lines and lines[0] == "":
        lines.pop(0)
    return lines


def same_lines(shown: list[str], actual: list[str]) -> bool:
    """A block of output lines; a line of `...` stands for the lines it leaves out."""
    if "..." not in shown:
        return shown == actual
    cut = shown.index("...")
    head, tail = shown[:cut], shown[cut + 1 :]
    if len(actual) < len(head) + len(tail):
        return False
    return actual[: len(head)] == head and actual[len(actual) - len(tail) :] == tail


def output_forms(text: str) -> list[str]:
    """What a comment may show of the printed ``text``.

    Its lines as printed, or on one line when a loop prints one per line,
    `0, 1, 2` or `0 red, then 1 green`, and the value after a `label: `.
    """
    lines = output_lines(text)
    forms = ["\n".join(lines), ", ".join(lines), " ".join(lines), ", then ".join(lines)]
    if len(lines) == 1 and ": " in lines[0]:
        forms.append(lines[0].rsplit(": ", 1)[1])
    return forms


def value_forms(value: object) -> list[str]:
    forms = [repr(value), str(value)]
    if isinstance(value, range):
        numbers = []
        for number in value:
            numbers.append(str(number))
        forms.append(", ".join(numbers))
    return forms


def strip_header(claim: str) -> tuple[bool, str]:
    """Whether the comment says it shows the output, and the comment without that."""
    header = HEADER.match(claim)
    if header is None:
        return False, claim
    return True, claim[header.end() :].strip()


# Running a python block.


@dataclass
class Block:
    source: str
    # The block's first line in the markdown file.
    start: int
    tree: ast.Module
    trailing: dict[int, str]
    whole_line: dict[int, str]

    def markdown_line(self, line: int) -> int:
        return self.start + line - 1


def simple_statements(tree: ast.AST) -> list[ast.stmt]:
    found = []
    for node in ast.walk(tree):
        if isinstance(node, ast.stmt) and not hasattr(node, "body"):
            found.append(node)
    return found


def statement_at(statements: list[ast.stmt], line: int) -> ast.stmt | None:
    """The simple statement that ends on ``line``, or spans it."""
    for statement in statements:
        if statement.lineno <= line <= statement.end_lineno:
            return statement
    return None


def comment_run(block: Block, after: int) -> tuple[int, list[str]]:
    """The comment lines right under line ``after``, and the last one's line."""
    texts = []
    line = after + 1
    while line in block.whole_line:
        texts.append(block.whole_line[line])
        line += 1
    return line - 1, texts


def failure_of(error: BaseException, statement: ast.stmt, filename: str) -> Failure:
    """The error, with the statement's lines and the block's lines it went through."""
    lines = set(range(statement.lineno, statement.end_lineno + 1))
    trace = error.__traceback__
    while trace is not None:
        if trace.tb_frame.f_code.co_filename == filename:
            lines.add(trace.tb_lineno)
        trace = trace.tb_next
    return Failure(error, lines)


def assigned_name(statement: ast.stmt) -> str | None:
    """The one name an assignment sets: `total = 0`, `total += 1`, `total: int = 0`."""
    if isinstance(statement, ast.Assign):
        targets = statement.targets
    elif isinstance(statement, (ast.AugAssign, ast.AnnAssign)):
        targets = [statement.target]
    else:
        return None
    if len(targets) == 1 and isinstance(targets[0], ast.Name):
        return targets[0].id
    return None


def run_block(page: Page, block: Block, keep=None) -> list[Printed]:
    """Run ``block``'s statements in the page's namespace and check its comments.

    ``keep`` picks the top-level statements to run; an exercise drops the
    template's stub functions, to run the solution's.
    """
    filename = f"<{page.path}:{block.start}>"
    recorder = Recorder(filename)
    values: dict[int, list[str]] = {}
    failures: list[Failure] = []
    for statement in block.tree.body:
        if keep is not None and not keep(statement):
            continue
        if isinstance(statement, ast.Expr):
            code = assignment(VALUE_NAME, statement.value, filename, statement)
        else:
            code = compile(ast.Module([statement], []), filename, "exec")
        error = run_statement(code, page.namespace, recorder)
        if error is not None:
            failures.append(failure_of(error, statement, filename))
            continue
        if isinstance(statement, ast.Expr):
            value = page.namespace.pop(VALUE_NAME, None)
            if value is not None:
                values[statement.end_lineno] = value_forms(value)
            continue
        name = assigned_name(statement)
        if name is not None and name in page.namespace:
            values[statement.end_lineno] = value_forms(page.namespace[name])
    check_comments(page, block, recorder.printed, values, failures)
    return recorder.printed


def printed_by(printed: list[Printed], first: int, end: int) -> str:
    """What the block's lines ``first`` to ``end`` printed."""
    text = ""
    for call in printed:
        if first <= call.line <= end:
            text += call.text
    return text


def failure_at(failures: list[Failure], line: int) -> Failure | None:
    for failure in failures:
        if line in failure.lines:
            return failure
    return None


class Claim(NamedTuple):
    """A comment that may show an output: one after a line, or a run of lines under one."""

    line: int
    last_line: int
    texts: list[str]
    on_the_line: bool


def claims_in(block: Block) -> list[Claim]:
    """The block's comments after a line, and its comment lines under a statement."""
    statement_ends = set()
    for node in ast.walk(block.tree):
        if isinstance(node, ast.stmt):
            statement_ends.add(node.end_lineno)
    claims = []
    for line, text in block.trailing.items():
        claims.append(Claim(line, line, [text], True))
    for line in sorted(block.whole_line):
        if line - 1 in statement_ends:
            last_line, texts = comment_run(block, line - 1)
            claims.append(Claim(line, last_line, texts, False))
    claims.sort()
    return claims


def run_claim(texts: list[str]) -> tuple[bool, str]:
    """Whether a run of comment lines says it shows the output, and what it shows.

    `# Output:` may stand on a line of its own, above the lines it introduces.
    """
    explicit, head = strip_header(texts[0])
    if not explicit:
        return False, "\n".join(texts)
    if head == "":
        return True, "\n".join(texts[1:])
    return True, "\n".join([head, *texts[1:]])


def check_comments(
    page: Page,
    block: Block,
    printed: list[Printed],
    values: dict,
    failures: list[Failure],
) -> None:
    """Compare each comment that shows an output with the output.

    A comment after a line shows what that line prints or gives. Comment
    lines right under a line show what the block printed since the last
    comment that showed an output.
    """
    statements = simple_statements(block.tree)
    shown_up_to = 0
    explained_up_to = 0
    for line, last, texts, on_the_line in claims_in(block):
        if on_the_line:
            statement = statement_at(statements, line)
            # A comment inside a statement of several lines is about that part.
            if statement is None or statement.end_lineno != line:
                continue
            first, end = statement.lineno, statement.end_lineno
            explicit, claim = strip_header(texts[0])
        else:
            first, end = shown_up_to + 1, line - 1
            explicit, claim = run_claim(texts)
        if claim == "":
            continue

        failure = failure_at(failures, end)
        if failure is not None:
            if (
                isinstance(failure.error, Stopped)
                or FAILS_ON_PURPOSE.search(claim)
                or type(failure.error).__name__ in claim
            ):
                continue
            if looks_like_output(claim):
                page.problem(
                    block.markdown_line(line),
                    f"can't show {claim!r}: line {block.markdown_line(max(failure.lines))} raises "
                    f"{type(failure.error).__name__}: {failure.error}",
                )
            continue

        text = printed_by(printed, first, end)
        if on_the_line and text == "":
            for call in printed:
                if line in call.lines:
                    text += call.text
        forms = []
        if text:
            forms.extend(output_forms(text))
        if on_the_line and end in values:
            forms.extend(values[end])
        if not forms:
            if explicit and not on_the_line:
                page.problem(
                    block.markdown_line(line),
                    f"shows output {claim!r}, but nothing is printed",
                )
            continue
        if agrees(claim, forms, page.any_order):
            page.checked += 1
            shown_up_to = last
            continue
        if not on_the_line and explained_up_to > shown_up_to:
            # `# hello` may show only what came after `# Says hi first`.
            since = printed_by(printed, explained_up_to + 1, end)
            if since and agrees(claim, output_forms(since), page.any_order):
                page.checked += 1
                shown_up_to = last
                continue
        if not explicit and is_prose(claim, forms):
            explained_up_to = last
            continue
        page.checked += 1
        shown_up_to = last
        actual = "\n".join(output_lines(text)) if text else forms[0]
        page.problem(
            block.markdown_line(line), f"shows {claim!r}, but the code gives {actual!r}"
        )


def calls_input(tree: ast.AST) -> bool:
    for node in ast.walk(tree):
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "input"
        ):
            return True
    return False


def parse_block(page: Page, source: str, start: int) -> Block | None:
    try:
        tree = ast.parse(source)
    except SyntaxError as error:
        # A syntax outline, `if condition:` over a comment, is meant that way.
        if "expected an indented block" not in str(error.msg):
            page.problem(
                start + (error.lineno or 1) - 1, f"does not parse: {error.msg}"
            )
        return None
    trailing, whole_line = comments(source)
    return Block(source, start, tree, trailing, whole_line)


def check_output_block(
    page: Page, printed: list[Printed], markdown: str, block_end: int
) -> None:
    """The **Output:** block after ``block_end``, if any, shows all the code prints."""
    found = OUTPUT_BLOCK.match(markdown[block_end:])
    if found is None:
        return
    shown = output_lines(found.group(1))
    text = ""
    for call in printed:
        text += call.text
    actual = output_lines(text)
    page.checked += 1
    if not same_lines(shown, actual):
        output_line = markdown[: block_end + found.start(1)].count("\n") + 1
        shown_text = "\n".join(shown)
        actual_text = "\n".join(actual)
        page.problem(
            output_line,
            f"shows the output {shown_text!r}, but the code prints {actual_text!r}",
        )


def forget_modules_in(folder: Path) -> None:
    """Drop the modules imported from ``folder``, so a saved file is imported afresh."""
    for name, module in list(sys.modules.items()):
        file = getattr(module, "__file__", None)
        if file and Path(file).resolve().parent == folder.resolve():
            del sys.modules[name]


def run_file(
    page: Page, name: str, source: str, start: int, markdown: str, block_end: int
) -> None:
    """Save a block labeled **File:** to the page's folder, and run it if it is main.py."""
    (page.folder / name).write_text(source, encoding="utf-8")
    if name != "main.py":
        return
    forget_modules_in(page.folder)
    program = Page(page.path, {"__name__": "__main__"}, page.folder)
    block = parse_block(program, source, start)
    if block is not None:
        printed = run_block(program, block)
        check_output_block(program, printed, markdown, block_end)
    page.findings.extend(program.findings)
    page.checked += program.checked


def run_blocks(page: Page, markdown: str, keep=None) -> None:
    for found in PYTHON_FENCE.finditer(markdown):
        source = found.group(1)
        start = markdown[: found.start(1)].count("\n") + 1
        label = FILE_LABEL.search(markdown[: found.start()])
        if label is not None:
            run_file(page, label.group(1), source, start, markdown, found.end())
            continue
        block = parse_block(page, source, start)
        if block is None:
            continue
        if calls_input(block.tree):
            page.unchecked += 1
            continue
        printed = run_block(page, block, keep)
        check_output_block(page, printed, markdown, found.end())


# Tables.


def table_cells(line: str) -> list[str]:
    cells = []
    for cell in re.split(r"(?<!\\)\|", line.strip().strip("|")):
        cells.append(cell.strip().replace("\\|", "|"))
    return cells


def code_span(cell: str) -> str | None:
    """The code of a cell that is one `code` span, as CommonMark prints it.

    A span that both starts and ends with a space loses one of each.
    """
    found = CODE_SPAN.match(cell)
    if found is None:
        return None
    code = found.group(1)
    if len(code) > 1 and code.startswith(" ") and code.endswith(" ") and code.strip():
        code = code[1:-1]
    return code


def example_columns(header_line: str) -> tuple[int, int] | None:
    """The columns of a table of examples: the code, and a result to its right."""
    code_column = None
    for column, cell in enumerate(table_cells(header_line)):
        name = cell.lower()
        if code_column is None and name in CODE_HEADERS:
            code_column = column
        elif code_column is not None and name in RESULT_HEADERS:
            return code_column, column
    return None


def check_tables(page: Page, markdown: str, namespace_of_table) -> None:
    lines = markdown.split("\n")
    in_fence = False
    for index, line in enumerate(lines):
        if line.startswith("```"):
            in_fence = not in_fence
        if (
            in_fence
            or not line.startswith("|")
            or index + 1 >= len(lines)
            or not TABLE_DIVIDER.match(lines[index + 1])
        ):
            continue
        columns = example_columns(line)
        if columns is None:
            continue
        code_column, result_column = columns
        row = index + 2
        while row < len(lines) and lines[row].startswith("|"):
            cells = table_cells(lines[row])
            if len(cells) > max(code_column, result_column):
                check_row(
                    page,
                    row + 1,
                    cells[code_column],
                    cells[result_column],
                    namespace_of_table(),
                )
            row += 1


def check_row(
    page: Page, line: int, examples: str, results: str, namespace: dict
) -> None:
    """One table row; a cell may hold several examples, a <br> apart."""
    example_cells = examples.split("<br>")
    result_cells = results.split("<br>")
    if len(example_cells) != len(result_cells):
        return
    for example_cell, result_cell in zip(example_cells, result_cells, strict=True):
        example = code_span(example_cell.strip())
        result = code_span(result_cell.strip())
        if example is None or result is None:
            continue
        try:
            value, error = evaluate(example, namespace)
        except SyntaxError:
            continue
        if isinstance(error, (NameError, Stopped)):
            # Stands for a value the table leaves to the reader, or reads input.
            page.unchecked += 1
            continue
        if error is not None:
            if type(error).__name__ not in result:
                page.problem(
                    line,
                    f"`{example}` shows `{result}`, but raises {type(error).__name__}: {error}",
                )
            continue
        page.checked += 1
        if not agrees(result, value_forms(value)):
            page.problem(line, f"`{example}` shows `{result}`, but gives `{value!r}`")


# Exercises.


def exercise_solution(statement: str) -> Path:
    """The solution beside an exercise's statement: lists/average/average.md -> average.py."""
    folder = ROOT / posixpath.dirname(statement)
    return folder / f"{folder.name}.py"


def load_solution(solution: Path) -> tuple[dict, BaseException | None]:
    """The namespace of the solution, run as a module rather than as a program."""
    namespace = {"__name__": solution.stem, "__file__": str(solution)}
    recorder = Recorder(str(solution))
    source = solution.read_text(encoding="utf-8")
    error = run_statement(compile(source, str(solution), "exec"), namespace, recorder)
    return namespace, error


def scratch_folder(scratch: Path, statement: str) -> Path:
    """A copy of the exercise's place in the workbook to run it in.

    The exercise folder is empty, and the topic's data folders, such as
    files/samples, sit beside it, so `../samples/poem.txt` still opens.
    """
    exercise = ROOT / posixpath.dirname(statement)
    topic = exercise.parent
    copy = scratch / topic.name / exercise.name
    if copy.parent.exists():
        shutil.rmtree(copy.parent)
    copy.mkdir(parents=True)
    for entry in topic.iterdir():
        if entry.is_dir() and not (entry / f"{entry.name}.md").exists():
            (copy.parent / entry.name).symlink_to(entry, target_is_directory=True)
    return copy


def feed(lines: list[str]):
    """input() that answers with ``lines``, less a prompt printed before an answer."""

    def answer(prompt: object = "") -> str:
        if not lines:
            raise EOFError("EOF when reading a line")
        line = lines.pop(0)
        prompt = str(prompt)
        if prompt and line.startswith(prompt):
            return line[len(prompt) :]
        if prompt.strip() and line.startswith(prompt.strip()):
            return line[len(prompt.strip()) :].strip()
        if ": " in line:
            return line.rsplit(": ", 1)[1]
        return line

    return answer


def plain(lines: list[str]) -> list[str]:
    """Output as the tests compare it: each line stripped, blank lines dropped."""
    kept = []
    for line in lines:
        if line.strip():
            kept.append(line.strip())
    return kept


def uses_random(source: str) -> bool:
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name == "random":
                    return True
        if isinstance(node, ast.ImportFrom) and node.module == "random":
            return True
    return False


def check_examples(page: Page, markdown: str, solution: Path) -> None:
    """Each example's input, given to the solution, prints its output."""
    source = solution.read_text(encoding="utf-8")
    random_output = uses_random(source)
    for found in EXAMPLE.finditer(markdown):
        first_block, second_block = found.group(3), found.group(4)
        if second_block is None:
            given, shown = "", first_block
        else:
            given, shown = first_block, second_block
        line = markdown[: found.start()].count("\n") + 1
        if random_output:
            page.unchecked += 1
            continue
        recorder = Recorder(str(solution))
        namespace = {"__name__": "__main__", "__file__": str(solution)}
        # A blank last line is an answer too: Enter on an empty line.
        builtins.input = feed(given.split("\n")[:-1])
        try:
            error = run_statement(
                compile(source, str(solution), "exec"), namespace, recorder
            )
        finally:
            builtins.input = refuse_input
        printed = ""
        for call in recorder.printed:
            printed += call.text
        shown_lines = plain(shown.split("\n"))
        printed_lines = plain(printed.split("\n"))
        page.checked += 1
        if error is not None and not isinstance(error, SystemExit):
            page.problem(line, f"the solution raises {type(error).__name__}: {error}")
        elif not same_lines(shown_lines, printed_lines):
            shown_text = "\n".join(shown_lines)
            printed_text = "\n".join(printed_lines)
            page.problem(
                line,
                f"shows the output {shown_text!r}, but {solution.name} prints {printed_text!r}",
            )


def check_exercise(scratch: Path, statement: str, extra: list[str]) -> Page:
    """An exercise's statement and hint, run against its solution."""
    solution = exercise_solution(statement)
    folder = scratch_folder(scratch, statement)
    page = Page(statement, {}, folder)
    if not solution.is_file():
        page.problem(1, f"no {solution.name} to run the examples against")
        return page
    statement_markdown = (ROOT / statement).read_text(encoding="utf-8")
    any_order = ANY_ORDER.search(statement_markdown) is not None
    os.chdir(folder)
    sys.path.insert(0, str(solution.parent))
    try:
        namespace, error = load_solution(solution)
        if isinstance(error, ReadsInput):
            # A program rather than functions: only its examples run it.
            namespace = {}
        elif error is not None:
            page.problem(1, f"{solution.name} raises {type(error).__name__}: {error}")
            return page
        functions = set()
        for name, value in namespace.items():
            if callable(value) and getattr(value, "__module__", None) == solution.stem:
                functions.add(name)

        def keep(statement: ast.stmt) -> bool:
            return not (
                isinstance(statement, ast.FunctionDef) and statement.name in functions
            )

        for path in [statement, *extra]:
            markdown = (ROOT / path).read_text(encoding="utf-8")
            part = Page(path, namespace, folder, any_order=any_order)
            namespace["__name__"] = "__main__"
            random.seed(0)
            try:
                run_blocks(part, markdown, keep)
                check_tables(part, markdown, lambda: namespace)
                if path == statement:
                    check_examples(part, markdown, solution)
            except Exception as error:  # a bug in this check, not in the page
                part.broke(error)
            page.findings.extend(part.findings)
            page.checked += part.checked
            page.unchecked += part.unchecked
    finally:
        sys.path.remove(str(solution.parent))
        forget_modules_in(solution.parent)
        os.chdir(ROOT)
    return page


def check_page(scratch: Path, path: str) -> Page:
    folder = scratch / path.replace("/", "_")
    folder.mkdir()
    page = Page(path, {"__name__": "__main__"}, folder)
    markdown = (ROOT / path).read_text(encoding="utf-8")
    random.seed(0)
    os.chdir(folder)
    sys.path.insert(0, str(folder))
    try:
        run_blocks(page, markdown)

        def namespace_of_table() -> dict:
            # The page's modules and functions; a variable the page set for
            # its own example would stand in for the one the table means.
            namespace = {"__name__": "__main__"}
            for name, value in page.namespace.items():
                if type(value).__name__ in (
                    "module",
                    "function",
                    "type",
                    "builtin_function_or_method",
                ):
                    namespace[name] = value
            return namespace

        check_tables(page, markdown, namespace_of_table)
    except Exception as error:  # a bug in this check, not in the page
        page.broke(error)
    finally:
        sys.path.remove(str(folder))
        forget_modules_in(folder)
        os.chdir(ROOT)
    return page


def workbook_pages() -> tuple[list[str], list[tuple[str, list[str]]]]:
    """The docs, then the exercises with their hints, as paths from the repo root.

    An exercise is named after its folder: lists/average/average.md.
    """
    docs = []
    for doc in sorted(ROOT.glob("*/_docs/*.md")):
        docs.append(doc.relative_to(ROOT).as_posix())
    exercises = []
    for statement in sorted(ROOT.glob("*/*/*.md")):
        if statement.stem != statement.parent.name:
            continue
        hints = []
        hint = statement.with_name(f"{statement.stem}_hint.md")
        if hint.is_file():
            hints.append(hint.relative_to(ROOT).as_posix())
        exercises.append((statement.relative_to(ROOT).as_posix(), hints))
    return docs, exercises


def main() -> None:
    pages, exercises = workbook_pages()
    signal.signal(signal.SIGALRM, stop_running)
    builtins.input = refuse_input
    # So one exercise's solution can import another's, as the tests do.
    sys.path.insert(0, str(ROOT))
    findings = []
    checked = 0
    unchecked = 0
    with tempfile.TemporaryDirectory(prefix="workbook-examples-") as scratch:
        results = []
        for path in pages:
            results.append(check_page(Path(scratch), path))
        for statement, hints in exercises:
            results.append(check_exercise(Path(scratch), statement, hints))
        for result in results:
            findings.extend(result.findings)
            checked += result.checked
            unchecked += result.unchecked
    builtins.input = REAL_INPUT

    summary = f"{checked} examples checked, {unchecked} left unchecked (input, randomness or a value left to the reader)"
    if findings:
        print(f"Code examples: {len(findings)} problem(s); {summary}", file=sys.stderr)
        for finding in findings:
            print(f"  {finding}", file=sys.stderr)
        sys.exit(1)
    print(f"Code examples: {summary}")


if __name__ == "__main__":
    main()
