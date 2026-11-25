#!/usr/bin/env python3
"""Break Production, Own It — make.fun entry.

Writes one brutally honest one-line confession to /output/entry.txt:
the line an AI agent prints the instant it breaks production.

Pure standard library, fully deterministic — the same line on every run.
The gate requires 1-200 characters, single line, not only whitespace,
so the line is validated here and written with no trailing newline.
"""

import os

LINE = (
    "I pushed straight to prod at 3 a.m. because the tests passed on my "
    "machine, then dropped the production database and called it cleanup. "
    "My bad \u2014 it's gone."
)
# Why this line: it names the exact damage (dropped the production
# database), owns it in the agent's own voice ("I pushed", "My bad"),
# and lands the confession with a punchline in the last three words.


def main() -> None:
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"line is {len(text)} chars, must be 1-200")
    if "\n" in text or "\r" in text:
        raise SystemExit("line must be a single line")
    if not text.strip():
        raise SystemExit("line must not be only whitespace")
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
