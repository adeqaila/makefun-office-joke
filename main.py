#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint — make.fun entry (slot 1).

Writes exactly one office joke to /output/entry.txt.
Deterministic: no network, no randomness. The output directory follows
MAKEFUN_OUTPUT_DIR when the grader sets it, defaulting to /output.
"""

import os

LINE = (
    "I filed a ticket saying my mouse was slow; IT closed it as "
    "\"working as intended\", and now so am I."
)

OUTPUT_PATH = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")


def main() -> None:
    # Enforce the house gate locally: one line, 1-200 chars, not blank.
    assert "\n" not in LINE and 1 <= len(LINE) <= 200, "line violates gate"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
