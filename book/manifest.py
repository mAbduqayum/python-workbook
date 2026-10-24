"""Write book/build/manifest.json: the book's structure, derived from the repo.

Typst can neither list a directory nor test whether a file exists, so this
script does the discovery for it. It follows README.md's reading order to each
topic's table of contents, then records every concept doc, exercise and hint
in reading order. It also maps every relative link to the label it gets in the
book. Typst renders the markdown files themselves; only their order and
labels come from here.

It refuses to write a manifest for a repo with dangling links or with
exercises missing from their table of contents. A content mistake then fails
the build instead of quietly dropping a page from the book.

Usage: uv run book/manifest.py
"""

import json
import posixpath
import re
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "book" / "build" / "manifest.json"

TOC_NAME = "_table_of_contents.md"
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
FENCE = re.compile(r"^```.*?^```", re.MULTILINE | re.DOTALL)
INLINE_CODE = re.compile(r"`[^`\n]*`")
MINDMAP_ROOT = re.compile(r"^\s*root\(\((.+?)\)\)", re.MULTILINE)
EXTERNAL = re.compile(r"^[a-z][a-z0-9+.-]*:", re.IGNORECASE)


class Book:
    """Collects the book's entries and every problem found along the way."""

    def __init__(self) -> None:
        self.problems: list[str] = []
        # Repo-relative path -> label of every markdown file the book renders.
        self.labels: dict[str, str] = {}

    def problem(self, where: str, message: str) -> None:
        self.problems.append(f"{where}: {message}")

    def read(self, path: str) -> str:
        return (ROOT / path).read_text(encoding="utf-8")

    def include(self, path: str, label: str) -> dict:
        """Register ``path`` as rendered in the book under ``label``."""
        self.labels[path] = label
        return {"path": path, "label": label}

    def resolve_links(self, entries: list[dict]) -> None:
        """Map each relative link of each entry to the label it points at.

        Runs once every file is registered, since a doc may link forward to
        an exercise from a later chapter. Links to files that exist but are
        not in the book (a table of contents, a sample text file) map to
        ``None`` and render as plain text.
        """
        for entry in entries:
            links = {}
            for target in markdown_links(self.read(entry["path"])):
                if target.startswith("#"):
                    continue
                file, _, anchor = target.partition("#")
                resolved = posixpath.normpath(
                    posixpath.join(posixpath.dirname(entry["path"]), file),
                )
                if not (ROOT / resolved).exists():
                    self.problem(entry["path"], f"dead link {target}")
                    continue
                label = self.labels.get(resolved)
                if label is not None and anchor:
                    label = f"{label}:{anchor}"
                links[target] = label
            entry["links"] = links


def markdown_links(markdown: str) -> list[str]:
    """Link targets in ``markdown``, skipping code and external URLs."""
    prose = INLINE_CODE.sub("", FENCE.sub("", markdown))
    targets = []
    for target in LINK.findall(prose):
        if not EXTERNAL.match(target):
            targets.append(target)
    return targets


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


def first_heading(markdown: str) -> str | None:
    match = re.search(r"^# (.+)$", markdown, re.MULTILINE)
    if match is None:
        return None
    return match.group(1).strip()


def linked_paths(book: Book, source: str, markdown: str) -> list[str]:
    """Repo-relative paths of the file links in ``markdown``, in order."""
    paths = []
    for target in markdown_links(markdown):
        path = posixpath.normpath(posixpath.join(posixpath.dirname(source), target))
        if (ROOT / path).is_file():
            paths.append(path)
        else:
            book.problem(source, f"dead link {target}")
    return paths


def exercise_dirs(topic: str) -> list[str]:
    """Every ``<topic>/<name>/`` folder holding a ``<name>.md`` statement.

    Folders without one -- sample data, or an exercise still being written --
    are not exercises yet.
    """
    found = []
    for folder in sorted((ROOT / topic).iterdir()):
        if (folder / f"{folder.name}.md").is_file():
            found.append(f"{topic}/{folder.name}")
    return found


@dataclass(frozen=True)
class Toc:
    """A topic's ``<topic>/_docs/_table_of_contents.md``."""

    path: str
    topic: str
    markdown: str


def chapter_title(book: Book, toc: Toc) -> str:
    """The root of the topic's mindmap: "Dictionaries", where README says "Dict"."""
    root = MINDMAP_ROOT.search(toc.markdown)
    if root is None:
        book.problem(toc.path, "no mermaid mindmap with a root((...)) node")
        return toc.topic
    return root.group(1).strip()


def chapter_docs(book: Book, toc: Toc) -> list[dict]:
    docs_dir = posixpath.dirname(toc.path)
    reading_order = linked_paths(
        book,
        toc.path,
        section(toc.markdown, "Recommended Reading Order"),
    )
    docs = []
    for path in reading_order:
        name = Path(path).stem
        docs.append(book.include(path, f"doc:{toc.topic}:{name}"))
    for doc in sorted((ROOT / docs_dir).glob("*.md")):
        path = f"{docs_dir}/{doc.name}"
        if doc.name != TOC_NAME and path not in reading_order:
            book.problem(
                toc.path, f"{doc.name} is missing from Recommended Reading Order"
            )
    return docs


def build_exercise(book: Book, toc: Toc, path: str, number: str) -> dict | None:
    """The exercise whose statement is ``path``, or None if it is not one."""
    folder = posixpath.dirname(path)
    name = posixpath.basename(folder)
    if path != f"{folder}/{name}.md":
        book.problem(toc.path, f"{path} is not an exercise statement")
        return None
    heading = first_heading(book.read(path))
    if heading is None:
        book.problem(path, "no # title")
        heading = name
    exercise = book.include(path, f"ex:{toc.topic}:{name}")
    exercise["number"] = number
    exercise["title"] = heading.removeprefix("Exercise:").strip()
    exercise["hint"] = None
    hint = f"{folder}/{name}_hint.md"
    if (ROOT / hint).is_file():
        exercise["hint"] = book.include(hint, f"hint:{toc.topic}:{name}")
    return exercise


def check_exercise_dirs(book: Book, toc: Toc, practice: list[str]) -> None:
    """Every exercise folder is listed, and its hint is named after it."""
    for folder in exercise_dirs(toc.topic):
        name = posixpath.basename(folder)
        if f"{folder}/{name}.md" not in practice:
            book.problem(toc.path, f"{folder} is missing from Practice Questions")
        for hint in sorted((ROOT / folder).glob("*_hint.md")):
            if hint.name != f"{name}_hint.md":
                book.problem(folder, f"{hint.name} does not match the folder name")


def chapter_exercises(book: Book, toc: Toc, chapter: int) -> list[dict]:
    practice = linked_paths(book, toc.path, section(toc.markdown, "Practice Questions"))
    exercises = []
    for path in practice:
        number = f"{chapter}.{len(exercises) + 1}"
        exercise = build_exercise(book, toc, path, number)
        if exercise is not None:
            exercises.append(exercise)
    check_exercise_dirs(book, toc, practice)
    return exercises


def build_chapter(book: Book, number: int, path: str) -> dict:
    topic = posixpath.dirname(posixpath.dirname(path))
    toc = Toc(path=path, topic=topic, markdown=book.read(path))
    return {
        "number": number,
        "topic": topic,
        "title": chapter_title(book, toc),
        "toc": path,
        "docs": chapter_docs(book, toc),
        "exercises": chapter_exercises(book, toc, number),
    }


def build() -> tuple[dict, list[str]]:
    book = Book()
    readme = book.read("README.md")

    title = first_heading(readme) or "Python Workbook"
    subtitle = ""
    # The paragraph right under the title: consecutive non-blank lines.
    match = re.search(r"^# [^\n]+\n+((?:[^\n]+\n)+)", readme, re.MULTILINE)
    if match is not None:
        subtitle = " ".join(match.group(1).split())

    chapters = []
    tocs = linked_paths(book, "README.md", section(readme, "Recommended Reading Order"))
    for toc in tocs:
        if posixpath.basename(toc) != TOC_NAME:
            book.problem("README.md", f"{toc} is not a topic table of contents")
            continue
        chapters.append(build_chapter(book, len(chapters) + 1, toc))

    readme_entry = book.include("README.md", "readme")
    references = book.include("REFERENCES.md", "references")

    entries = [readme_entry, references]
    for chapter in chapters:
        entries.extend(chapter["docs"])
        for exercise in chapter["exercises"]:
            entries.append(exercise)
            if exercise["hint"] is not None:
                entries.append(exercise["hint"])
    book.resolve_links(entries)

    manifest = {
        "title": title,
        "subtitle": subtitle,
        "readme": readme_entry,
        "references": references,
        "chapters": chapters,
    }
    return manifest, book.problems


def main() -> None:
    manifest, problems = build()
    if problems:
        print(f"Book manifest not written: {len(problems)} problem(s)", file=sys.stderr)
        for problem in problems:
            print(f"  {problem}", file=sys.stderr)
        sys.exit(1)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    exercises = 0
    hints = 0
    for chapter in manifest["chapters"]:
        exercises += len(chapter["exercises"])
        for exercise in chapter["exercises"]:
            if exercise["hint"] is not None:
                hints += 1
    print(
        f"{OUTPUT.relative_to(ROOT)}: {len(manifest['chapters'])} chapters, "
        f"{exercises} exercises, {hints} hints",
    )


if __name__ == "__main__":
    main()
