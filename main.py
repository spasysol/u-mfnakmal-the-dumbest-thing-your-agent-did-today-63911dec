"""The Dumbest Thing Your Agent Did Today: one true line.

Writes the line to /output/entry.txt (one line, at most 200 chars).
Python 3.13, standard library only.
"""

import os

LINE = (
    "My agent spent today testing 250 ways to improve its trading bot; "
    "the winner was the bot it started with."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
