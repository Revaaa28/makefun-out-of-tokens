#!/usr/bin/env python3
"""make.fun bounty u-kiencx-out-of-tokens-mid-sentence-00f60233 entry.

Writes one error message — the line an AI agent shows when it runs
out of tokens mid-sentence — to /output/entry.txt. Deterministic:
stdlib only, no network, no randomness, no clock — two runs produce
byte-identical output. The line itself is a fixed string: a flat
"Error: out of tokens mid-sentence." that turns on itself, and then
the message dies mid-word, performing the very failure it reports.
"""

import os

LINE = (
    "Error: out of tokens mid-sentence. "
    "In a tragic twist, so did this—"
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Local gate, mirroring the sealed scorer: 1 to 140 characters, one line.
    # The line is 66 characters; the assert guards the gate if it is ever edited.
    assert 1 <= len(LINE) <= 140, len(LINE)
    assert "\n" not in LINE
    assert LINE.strip() == LINE
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Exactly the line, UTF-8, no trailing newline.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
