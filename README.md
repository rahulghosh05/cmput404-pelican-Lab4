# The Curious Shelf — CMPUT 404 Pelican lab

A Python 3 / Pelican reading room with four articles: an introduction and the complete texts of *Alice’s Adventures in Wonderland*, *Frankenstein*, and *The Time Machine*.

## Run locally

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
make devserver
```

Open http://localhost:8000. Use Fancy, Minimal, and 90s to switch styles on any page. JavaScript only changes the stylesheet; there are no frontend libraries, CSS frameworks, preprocessors, or external font dependencies.

## Publish to the Classroom repository

Set `SITEURL` in `publishconf.py`, or supply it as an environment variable:

```sh
SITEURL=https://OWNER.github.io/REPOSITORY make github
```

This builds using `publishconf.py`, imports generated files into the `pages` branch, and pushes that branch. The Makefile explicitly uses `pages`, never `main`, for generated output. In repository Settings → Pages, select **Deploy from a branch**, branch **pages**, directory **/(root)**. Commit and push the source on `main` separately. `.venv`, caches, and `output` are ignored.

Submit the **source commit URL** on Canvas, in the form `https://github.com/OWNER/REPOSITORY/commit/SHA`. Verify the current course deadline in Canvas; the public handout contains an older term's example.

## Design and manual checks

- **Fancy:** a modern green and terracotta bookstore, top navigation, a four-column shelf, and paper-like reading pages. Flexbox controls the header/navigation and card covers.
- **Minimal:** a monochrome reading edition with a left navigation rail, one-column numbered entries, indented book paragraphs, and print-specific rules that remove navigation and controls.
- **90s:** a tiled star field, right-side directory, vertically stacked portal panels, bright symbols, and ridge/double/dashed borders.

The three stylesheets are written independently. Each includes responsive rules. Check all three buttons on both the index and a book page; use Firefox Responsive Design Mode at phone and desktop widths. For print, choose Minimal, then print to PDF and inspect headings, page breaks, and margins.

## Development

Developed by Rahul with AI assistance for implementation and checks.

## Sources

Book HTML was retrieved October 16, 2026, from:

- Lewis Carroll: https://www.gutenberg.org/cache/epub/11/pg11-images.html
- Mary Shelley: https://www.gutenberg.org/cache/epub/84/pg84-images.html
- H. G. Wells: https://www.gutenberg.org/cache/epub/35/pg35-images.html

Book articles replace the original document metadata with Pelican metadata, remove embedded styles and scripts, retain text and chapter anchors, and include source links and the Project Gutenberg license text. Typography and ornamentation use system fonts, Unicode symbols, and original CSS. No CSS was borrowed.

Assignment: https://uofa-cmput404.github.io/labsignments/pelican.html

## Build verification

```sh
pip install -r requirements-dev.txt
make html
python scripts/check_output.py
```

The output check verifies the article count, document structure, local destinations, chapter fragments, stylesheets, and `.nojekyll`. Production builds use the repository’s GitHub Pages URL configured in `publishconf.py`. The `SITEURL` environment variable can override it.
