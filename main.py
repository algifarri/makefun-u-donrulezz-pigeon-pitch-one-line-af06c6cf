#!/usr/bin/env python3
"""Pigeon Pitch, One Line entry.

Writes a single one-line elevator pitch (158 characters, English) that a
city pigeon gives investors for its startup, to /output/entry.txt.
Deterministic, stdlib-only, no network, no randomness.
"""

import os

PITCH = (
    "My startup is already profitable: your lunch is our revenue, "
    "your statue is our office, and your car is our restroom "
    "\u2014 I'm raising a round to scale the flock."
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1-200 characters,
    # not only whitespace, on a single line. Written with no trailing
    # newline so the file holds exactly the pitch (158 characters).
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
