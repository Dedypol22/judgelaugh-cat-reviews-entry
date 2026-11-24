#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human -- one-line review writer.

Writes a single line -- a one-star review written by a house cat about its
human -- to /output/entry.txt, and nothing else.

Standard library only. No network. No input files: the line is embedded
below, so the program is deterministic and runs from any working directory.
"""

import os

LINE = (
    "One star. The laptop keyboard is warm, the human sits on it anyway, "
    "and somehow I'm the one with boundary issues."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise SystemExit("line must be 1-200 characters, got %d" % len(LINE))
    if not LINE.strip():
        raise SystemExit("line must not be only whitespace")
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("line must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
