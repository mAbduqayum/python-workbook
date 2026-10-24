// How the book looks. main.typ decides what goes where; every page style,
// heading style and building block (exercise, hint, diagram) lives here.

#import "@preview/cmarker:0.1.10"
#import "@preview/codly:2.0.0" as codly
#import "@preview/merman:0.5.0"

// Dark enough to print as near-black on a grayscale printer.
#let accent = rgb("#1d4f7c")
#let muted = luma(105)
#let mono = "DejaVu Sans Mono"
// The border of every code block: 3.4:1 against white, above the 3:1 a
// boundary needs to stay visible.
#let frame = 0.75pt + luma(140)

// Chapters number as 7 and 7.1, appendices as A and A.1. Deeper headings --
// a doc's subsections, an exercise's "Task" -- never show a number.
#let numbered(pattern) = (..parts) => {
  if parts.pos().len() <= 2 { numbering(pattern, ..parts) }
}

// Diagrams are drawn from inside the raw-block rule, where the font is the
// code font, so the body font is named explicitly rather than inherited.
#let diagram(code) = merman.mermaid(
  code,
  typography: (font: ("Libertinus Serif",)),
  theme-name: "neutral",
  width: 100%,
  height: 10cm,
  fit: "contain",
  alt: "Diagram",
)

// A topic's mermaid mindmap, drawn as one card per branch. The Typst mermaid
// renderers fail on mindmaps -- merman runs out of layout budget, mmdr nests
// siblings under each other -- and the maps are plain indented outlines
// anyway: root, branches, leaves.
#let concept-map(source) = {
  // Mermaid spells brackets as entities (`#40;` is "("), since brackets
  // would make a node shape; `root((Sets))` is such a shape around "Sets".
  let decode(text) = text.replace(regex("#(\d+);"), found => str.from-unicode(int(found.captures.first())))
  let unwrap(text) = {
    let shaped = text.match(regex("^\w*[\[({]+(.*?)[\])}]+$"))
    if shaped == none { text } else { shaped.captures.first() }
  }
  let lines = source.split("\n").filter(line => line.trim() not in ("", "mindmap"))
  let indent(line) = line.len() - line.trim(at: start).len()
  let levels = lines.map(indent).dedup().sorted()

  let branches = ()
  for line in lines {
    let level = levels.position(width => width == indent(line))
    let name = decode(unwrap(line.trim()))
    if level == 1 {
      branches.push((name: name, leaves: ()))
    } else if level > 1 and branches.len() > 0 {
      branches.at(-1).leaves.push((depth: level - 2, name: name))
    }
  }

  let card(branch) = block(
    width: 100%,
    inset: 8pt,
    radius: 3pt,
    stroke: 0.5pt + luma(185),
    fill: luma(252),
    {
      text(fill: accent, weight: "bold", branch.name)
      set text(size: 0.9em)
      for leaf in branch.leaves {
        linebreak()
        h(leaf.depth * 1em)
        leaf.name
      }
    },
  )
  grid(columns: (1fr,) * 3, gutter: 8pt, ..branches.map(card))
}

// The example blocks of an exercise: what the student types, then what the
// program prints. Framed and left uncoloured so they never read as Python.
#let console-inset = (x: 8pt, y: 6pt)
#let console(it) = block(
  width: 100%,
  fill: luma(250),
  stroke: frame,
  radius: 2pt,
  inset: console-inset,
  it,
)

// One example of an exercise, as the statements write it: `**Example 2:**`
// with an optional note, inside the bold or after it, then the input block
// and the output block. A lone block is the output of a program that reads
// no input.
#let example-pattern = regex(
  "(?m)^\*\*Example \d+:[ \t]*(.*?)\*\*(.*)\n\s*```\n((?s:.*?))^```[ \t]*\n?(?:\s*```\n((?s:.*?))^```[ \t]*\n?)?",
)

// The markdown cut around its runs of examples: markdown strings alternate
// with arrays of examples, each with a note, an input and an output.
#let split-examples(markdown) = {
  let pieces = ()
  let end = 0
  for found in markdown.matches(example-pattern) {
    let gap = markdown.slice(end, found.start)
    if pieces.len() == 0 or type(pieces.last()) == str or gap.trim() != "" {
      pieces.push(gap)
      pieces.push(())
    }
    let (inside, after, first, second) = found.captures
    let note = (inside + " " + after).trim()
    if note.starts-with("(") and note.ends-with(")") { note = note.slice(1, -1) }
    pieces.at(-1).push((
      note: note,
      input: if second == none { none } else { first },
      output: if second == none { first } else { second },
    ))
    end = found.end
  }
  pieces.push(markdown.slice(end))
  pieces
}

// A run of examples as one table, a row per example. The columns are equal
// unless a line would then wrap; the input column then takes its full width.
#let example-table(examples, render) = layout(size => {
  let cell(code) = if code != none [#raw(code, block: true)<example-io>]
  let has-input = examples.any(example => example.input != none)
  let room = size.width / 2 - 2 * console-inset.x
  // Lines are measured as inline raw, less that box's own padding.
  let padding = measure(raw("")).width
  let fits(code) = code == none or code.split("\n").all(line => measure(raw(line)).width - padding <= room)
  let columns = if not has-input {
    (1fr,)
  } else if examples.all(example => fits(example.input) and fits(example.output)) {
    (1fr, 1fr)
  } else {
    (auto, 1fr)
  }

  // A note row stays on the page of its example: an empty cell spanning
  // both rows, in a first column of no width, holds them together.
  let tie(span) = table.cell(rowspan: span, inset: 0pt)[]
  let rows = ()
  for example in examples {
    if example.note != "" {
      let note = text(fill: muted, style: "italic", render(example.note))
      rows.push(tie(2))
      rows.push(table.cell(colspan: columns.len(), fill: none, note))
    } else {
      rows.push(tie(1))
    }
    if has-input { rows.push(cell(example.input)) }
    rows.push(cell(example.output))
  }
  // An example split over two pages reads as two examples.
  set table.cell(breakable: false)
  table(
    columns: (0pt, ..columns),
    stroke: frame,
    inset: console-inset,
    fill: (_, y) => if y == 0 { luma(238) } else { luma(250) },
    table.header(tie(1), ..if has-input { ([Input],) } else { () }, [Output]),
    ..rows,
  )
})

// The markdown cut at its `## ... Formula ...` sections: (text, formula)
// pairs, in order.
#let split-formulas(markdown) = {
  let sections = ((text: "", formula: false),)
  for line in markdown.split("\n") {
    if line.starts-with("## ") {
      let formula = line.contains("Formula")
      if formula != sections.last().formula { sections.push((text: "", formula: formula)) }
    }
    sections.at(-1).text += line + "\n"
  }
  sections
}

// Typst's own names for these, set upright: `sin(x)`, `x mod 7`.
#let math-operators = ("sin", "cos", "tan", "arcsin", "arccos", "arctan", "exp", "ln", "log", "max", "min")
// Typst math functions that wrap what follows: `floor(x)` is ⌊x⌋.
#let math-calls = ("floor", "ceil", "abs")
#let superscripts = (
  "⁰": "0", "¹": "1", "²": "2", "³": "3", "⁴": "4", "⁵": "5", "⁶": "6", "⁷": "7", "⁸": "8", "⁹": "9",
)
#let subscripts = (
  "₀": "0", "₁": "1", "₂": "2", "₃": "3", "₄": "4", "₅": "5", "₆": "6", "₇": "7", "₈": "8", "₉": "9",
)
// Characters that mean the same in Typst math as in a written formula.
#let math-symbols = "+-−=<>(),.:/|!×·±→≤≥≠≈"
#let formula-token = regex("\p{L}[\p{L}\d_]*|\d+(?:[.,]\d+)*|[⁰¹²³⁴⁵⁶⁷⁸⁹]+|[₀-₉]+|\s+|(?s:.)")
// Units a formula gives after a number, `9.8 m/s²`, or in parentheses after
// a name, `weight (kg)`.
#let units = ("m", "cm", "km", "s", "h", "g", "kg", "J", "W", "kWh", "K", "Pa", "kPa", "mol", "liter")

#let is-name(token) = token.match(regex("^\p{L}")) != none
#let is-script(token) = token.first() in superscripts or token.first() in subscripts
// `²³` as `^23`, `₁` as `_1`.
#let script(token) = {
  let marker = if token.first() in superscripts { "^" } else { "_" }
  marker + token.clusters().map(digit => (superscripts + subscripts).at(digit)).join()
}

// How many tokens from `start` spell a unit, `J/(mol·K)` or `°C`: 0 when
// they do not start one.
#let unit-length(tokens, start) = {
  let length = 0
  let depth = 0
  for token in tokens.slice(start) {
    // The scale after a degree sign: `°C`.
    let degree-scale = length > 0 and tokens.at(start + length - 1) == "°" and is-name(token)
    if token == "(" {
      depth += 1
    } else if token == ")" {
      if depth == 0 { break }
      depth -= 1
    } else if not (
      token in units or token in ("/", "·", "°") or token.first() in superscripts or degree-scale
    ) {
      break
    }
    length += 1
  }
  let first = tokens.at(start, default: "")
  if (first in units or first == "°") and depth == 0 { length } else { 0 }
}

// Where the unit after the whitespace at `i` ends, or none: a bare unit
// follows a number, `9.8 m/s²`; a bracketed one any quantity, `weight (kg)`.
#let unit-end(tokens, i, last-kind) = {
  let bracketed = tokens.at(i + 1, default: "") == "("
  let start = if bracketed { i + 2 } else { i + 1 }
  let end = start + unit-length(tokens, start)
  if end == start { return none }
  if bracketed {
    if tokens.at(end, default: "") != ")" { return none }
    end += 1
  }
  let quantity = if bracketed { last-kind != none } else { last-kind == "number" }
  if quantity { end } else { none }
}

// The tokens of a unit as upright math. Text would do, but Typst spaces text
// in math like a word, and so `(kg) /` apart.
#let unit(tokens) = {
  let parts = ()
  for token in tokens {
    if token.first() in superscripts {
      parts.at(-1) += script(token)
    } else if token == "/" {
      parts.push("\\/")
    } else if token == "·" {
      parts.push("class(\"normal\", dot.c)")
    } else if token == "°" {
      parts.push("degree")
    } else {
      parts.push(token.clusters().join(" "))
    }
  }
  "upright(" + parts.join(" ") + ")"
}

// A multi-letter name as italic letters, spaced like a product of variables:
// `4ac` and `PV` come out right, and so does `rate`. An escaped underscore
// stays tight; quoted, it would be spaced like a word.
#let word(name) = eval(
  name.clusters().map(letter => if letter == "_" { "\\_" } else { letter }).join(" "),
  mode: "math",
)

// Any other sign as math: `*` and `%` as Python writes them, and anything
// Typst math has no meaning for as plain text.
#let sign(token, block: false) = {
  if token == "*" {
    "times"
  } else if token == "%" {
    "mod"
  } else if token == "/" and not block {
    "\\/"
  } else if math-symbols.contains(token) {
    token
  } else {
    repr(token)
  }
}

// A formula as the statements write it, `balance = deposit × (1 + rate/100)^years`,
// typeset as math. Names become `word("rate")`, so `rate/100` puts all of
// "rate" over 100; anything unknown is set as plain text, so any source
// gives valid math. Only a displayed formula stacks its fractions: inline,
// they would shrink to unreadable, so `/` stays a slash.
#let formula(source, block: false) = {
  let source = source.replace("<=", "≤").replace(">=", "≥").replace("!=", "≠").replace("->", "→")
  let tokens = source.matches(formula-token).map(found => found.text)
  let atoms = ()
  // The next atom joins the last one: after `^`, `√` or a call's name.
  let glue = false
  let root = false
  // What the last atom is, for a unit after it: "number", "name" or none.
  let last-kind = none
  let skip = 0
  for (i, token) in tokens.enumerate() {
    if skip > 0 {
      skip -= 1
      continue
    }
    let next = tokens.at(i + 1, default: "")
    let opens = false
    let atom = none
    if token.trim() == "" {
      // A unit joins its quantity, upright and as written, so
      // `weight (kg) / height² (m²)` puts both units in the fraction.
      let end = unit-end(tokens, i, last-kind)
      if end != none and not glue {
        atoms.at(-1) = "group(" + atoms.at(-1) + " thin " + unit(tokens.slice(i + 1, end)) + ")"
        last-kind = "name"
        skip = end - i - 1
      }
      continue
    }
    if is-script(token) {
      if atoms.len() == 0 { atoms.push("") }
      atoms.at(-1) += script(token)
      continue
    }
    if token == "^" and atoms.len() > 0 {
      atoms.at(-1) += "^"
      glue = true
      continue
    }
    if token == "√" {
      root = true
      continue
    }
    last-kind = none
    if is-name(token) {
      if token in math-operators {
        atom = token
      } else if next == "(" and token in math-calls {
        atom = token
        opens = true
      } else if next == "(" and token.clusters().len() > 1 {
        atom = "op(" + repr(token) + ")"
      } else {
        let (name, digits) = token.match(regex("^(.*?)(\d*)$")).captures
        atom = if name.clusters().len() == 1 { name } else { "word(" + repr(name) + ")" }
        if digits != "" { atom += "_" + digits }
        last-kind = "name"
      }
    } else if token.match(regex("^\d")) != none {
      atom = if token.contains(",") { repr(token) } else { token }
      last-kind = "number"
    } else if token == "°" {
      // A temperature on its own: `°C + 273.15`.
      let length = unit-length(tokens, i)
      atom = unit(tokens.slice(i, i + length))
      skip = length - 1
      last-kind = "name"
    } else {
      atom = sign(token, block: block)
    }
    if root and atom == "(" {
      atom = "sqrt("
    } else if root {
      atom = "sqrt(" + atom + ")"
    }
    root = false
    if glue { atoms.at(-1) += atom } else { atoms.push(atom) }
    glue = opens
  }
  // `group` makes one atom of a quantity and its unit, for `/` to take whole.
  let scope = (word: word, group: body => body)
  math.equation(block: block, eval(atoms.join(" "), mode: "math", scope: scope))
}

// Shrinks a displayed formula too wide for the page, since math never
// wraps, instead of letting it run into the margin.
#let fit-width(body) = layout(size => {
  let width = measure(body).width
  if width <= size.width { body } else { scale(size.width / width * 100%, reflow: true, body) }
})

// cmarker's `raw` inside a Formula section: plain code spans and blocks are
// formulas. A block is displayed on its own line.
#let formula-raw(text, block: false, lang: none, ..rest) = {
  if lang != none { return raw(text, block: block, lang: lang, ..rest) }
  if block { fit-width(formula(text.trim(), block: true)) } else { formula(text) }
}

// A code span alone on its line is a formula to display, like a block.
#let display-formula = regex("(?m)^`([^`\n]+)`[ \t]*$")
#let fence-display-formulas(markdown) = markdown.replace(
  display-formula,
  found => "```\n" + found.captures.first() + "\n```",
)

// Renders a repo markdown file. `entry` is its manifest entry: `links` sends
// each relative link to its label in the book (`none` when the target is not
// in the book, e.g. a table of contents), and `label` prefixes every heading
// label, since 222 exercises each have a "Task" heading. `anchor: false` is
// for callers that put `entry.label` on a heading of their own.
#let render-md(entry, h1-level: 1, markdown: none, anchor: true) = {
  let source = if markdown == none { read("/" + entry.path) } else { markdown }
  let follow(dest, ..body) = {
    if type(dest) != str or dest not in entry.links {
      return link(dest, ..body)
    }
    let target = entry.links.at(dest)
    if target == none { body.pos().first() } else { link(label(target), ..body) }
  }
  let render(part, formulas: false) = cmarker.render(
    if formulas { fence-display-formulas(part) } else { part },
    h1-level: h1-level,
    label-prefix: entry.label + ":",
    set-document-title: false,
    scope: if formulas { (link: follow, raw: formula-raw) } else { (link: follow) },
  )
  if anchor { [#metadata(entry.path)#label(entry.label)] }
  for section in split-formulas(source) {
    for piece in split-examples(section.text) {
      if type(piece) == str { render(piece, formulas: section.formula) } else { example-table(piece, render) }
    }
  }
}

#let without-title(markdown) = markdown.replace(regex("^# [^\n]*\n"), "", count: 1)

#let exercise(entry) = {
  [#heading(level: 3, outlined: false, bookmarked: true)[
      #text(fill: accent)[Exercise #entry.number] #h(0.3em)#entry.title
    ]#label(entry.label)]
  render-md(entry, h1-level: 3, markdown: without-title(read("/" + entry.path)), anchor: false)
  if entry.hint != none {
    block(above: 1em, context {
      let target = label(entry.hint.label)
      let page-number = counter(page).at(locate(target)).first()
      link(target, text(fill: accent)[→ Hint on page #page-number])
    })
  }
  // A little more room before the next exercise than the 2em above a doc's
  // subsection: adjacent weak spacings collapse to the largest. Placed after
  // the exercise, not before, so the first one stays close to its heading.
  v(3em, weak: true)
}

#let hint(exercise) = {
  [#heading(level: 3, outlined: false, bookmarked: true)[
      Hint for #text(fill: accent)[Exercise #exercise.number] #h(0.3em)#exercise.title
    ]#label(exercise.hint.label)]
  render-md(
    exercise.hint,
    h1-level: 3,
    markdown: without-title(read("/" + exercise.hint.path)),
    anchor: false,
  )
  block(above: 1em, link(label(exercise.label), text(fill: accent)[← Back to Exercise #exercise.number]))
}

#let title-page(title, subtitle) = page(header: none, footer: none)[
  #set align(center)
  #v(1fr)
  #text(size: 3em, weight: "bold", title)
  #v(1.5em)
  #block(width: 75%, text(size: 1.3em, fill: muted, subtitle))
  #v(2fr)
]

// The build stamp: `just book` and the Book workflow pass these as
// `--input`s, so every PDF says which commit it was built from. The date is
// the commit's, not the build's, so rebuilding a commit gives the same PDF.
#let colophon(title) = page(header: none, footer: none)[
  #set text(size: 0.9em, fill: muted)
  #v(1fr)
  *#title* \
  #let date = sys.inputs.at("date", default: none)
  Built from commit #raw(sys.inputs.at("commit", default: "unknown"))#if date != none [ of #date]. \
  #let repo = sys.inputs.at("repo", default: none)
  #if repo != none [
    Generated from the markdown in #link(repo), which also holds the tests and
    the latest version of this book.
  ]
]

// Starts a chapter (or a front- or back-matter part) on a fresh page. The
// break must precede the heading rather than live in its show rule, or the
// heading's location lands on the previous page.
#let open-chapter(title) = {
  pagebreak(weak: true)
  heading(level: 1, title)
}

// The book has two: a one-page overview of its chapters, then every chapter
// with its sections.
#let contents(title, depth: 1) = {
  show outline.entry.where(level: 1): it => {
    v(1em, weak: true)
    strong(it)
  }
  outline(title: title, depth: depth, indent: auto)
}

// Each `matter` starts a fresh page so its page-number style begins there.
#let front-matter(body) = {
  set page(numbering: "i")
  set heading(numbering: none)
  body
}

// Page 1 is a right-hand page, so odd pages stay on the right throughout.
#let main-matter(body) = {
  pagebreak(weak: true, to: "odd")
  set page(numbering: "1")
  counter(page).update(1)
  set heading(numbering: numbered("1.1"))
  body
}

#let back-matter(body) = {
  pagebreak(weak: true)
  counter(heading).update(0)
  set heading(numbering: numbered("A.1"))
  show heading.where(level: 1): set heading(supplement: [Appendix])
  body
}

#let book(title: none, body) = {
  set document(title: title)
  set page(
    paper: "a4",
    margin: (x: 3cm, top: 3cm, bottom: 2.8cm),
    // The page number on the outer edge: left on a left-hand (even) page,
    // right on a right-hand (odd) one. On the inner edge, above a rule, the
    // current chapter's name, except on the page where a chapter starts.
    header: context {
      let physical-page = here().page()
      let outer = if calc.odd(physical-page) { right } else { left }
      let page-number = counter(page).display()
      let chapters = query(heading.where(level: 1))
      let opens = chapters.any(chapter => chapter.location().page() == physical-page)
      let current = chapters.filter(chapter => chapter.location().page() < physical-page).at(-1, default: none)
      set text(size: 0.85em)
      if opens or current == none {
        align(outer, page-number)
      } else {
        let number = if current.numbering != none {
          numbering(current.numbering, ..counter(heading).at(current.location())) + " "
        }
        let title = text(fill: muted)[#number#current.body]
        block(width: 100%, inset: (bottom: 5pt), stroke: (bottom: 0.5pt + muted), if outer == right {
          [#title #h(1fr) #page-number]
        } else {
          [#page-number #h(1fr) #title]
        })
      }
    },
    footer: none,
  )
  set text(font: "Libertinus Serif", size: 11pt, lang: "en")
  set par(leading: 0.68em, spacing: 1.15em)
  show raw: set text(font: mono)
  show link: set text(fill: accent)

  set table(stroke: 0.5pt + luma(185), inset: (x: 6pt, y: 5pt))
  show table.cell.where(y: 0): set text(weight: "bold")

  show heading.where(level: 1): set heading(supplement: [Chapter])
  show heading.where(level: 1): it => {
    v(2cm)
    if it.numbering != none {
      text(size: 1.1em, fill: accent, tracking: 0.06em)[
        #it.supplement #counter(heading).display(it.numbering)
      ]
      v(0.3em)
    }
    text(size: 2.2em, weight: "bold", it.body)
    v(1cm)
  }
  show heading.where(level: 2): it => block(above: 2.2em, below: 1em, sticky: true, text(size: 1.45em)[
    #if it.numbering != none {
      text(fill: accent, counter(heading).display(it.numbering))
      h(0.6em)
    }
    #it.body
  ])
  show heading.where(level: 3): it => block(above: 2em, below: 0.8em, sticky: true, text(size: 1.2em, it.body))
  // An exercise's own "Task" / "Examples" headings: in the PDF, but too many
  // for the bookmarks panel.
  show heading.where(level: 4): set heading(outlined: false)
  show heading.where(level: 4): it => block(above: 1.4em, below: 0.7em, sticky: true, text(size: 1.05em, it.body))
  show heading.where(level: 5): set heading(outlined: false)

  // github-light's own frame is #f6f8fa: invisible on white.
  show: codly.theme("github-light", stroke: frame)
  // Each row already has about 3pt of inset; the padding brings the code as
  // far from the side of the frame as a console block's text.
  show: codly.set_(number-enabled: false, lang-position: none, padding: (x: 5pt))
  // One rule for every code block: with several, the order they are written
  // in decides which wins.
  show raw.where(block: true): it => {
    if it.lang == "mermaid" {
      diagram(it.text)
    } else if it.lang != none {
      codly.new(it)
    } else if it.at("label", default: none) == <example-io> {
      // A cell of an example table, which draws the frame itself.
      it
    } else {
      console(it)
    }
  }
  show raw.where(block: false): box.with(fill: luma(242), inset: (x: 2pt), outset: (y: 2pt), radius: 2pt)

  body
}
