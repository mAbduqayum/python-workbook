// The book's entry point. `just book` builds it: book/manifest.py first
// writes build/manifest.json -- the chapters, docs, exercises and hints it
// finds by following README.md to each topic's table of contents -- and this
// file lays them out. The markdown itself is read straight from the repo.

#import "template.typ": *

#let manifest = json("build/manifest.json")

// The `## heading` section of a markdown file, heading included.
#let section(markdown, heading) = {
  let start = markdown.position("## " + heading + "\n")
  let rest = markdown.slice(start)
  let end = rest.slice(3).position("\n## ")
  if end == none { rest } else { rest.slice(0, end + 3) }
}

#let mindmap(toc) = {
  let found = read("/" + toc).match(regex("(?s)```mermaid\n(.*?)\n```"))
  if found != none { concept-map(found.captures.first()) }
}

#show: book.with(title: manifest.title)

#show: front-matter
#title-page(manifest.title, manifest.subtitle)
#colophon(manifest.title)
#contents([Brief Contents])
#pagebreak(weak: true)
#contents([Contents], depth: 2)
#pagebreak(weak: true)
#render-md(manifest.readme, h1-level: 0, markdown: section(read("/README.md"), "Getting Started"))

#show: main-matter
#for chapter in manifest.chapters {
  open-chapter(chapter.title)
  mindmap(chapter.toc)
  for doc in chapter.docs {
    render-md(doc, h1-level: 2)
  }
  if chapter.exercises.len() > 0 {
    heading(level: 2)[Exercises]
    for entry in chapter.exercises {
      exercise(entry)
    }
  }
}

#show: back-matter
#open-chapter[Hints]
#for chapter in manifest.chapters {
  let hinted = chapter.exercises.filter(entry => entry.hint != none)
  if hinted.len() > 0 {
    heading(level: 2, chapter.title)
    for entry in hinted {
      hint(entry)
    }
  }
}

#pagebreak(weak: true)
#[
  #set heading(numbering: none)
  #render-md(manifest.references)
]
