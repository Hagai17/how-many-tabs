#!/usr/bin/env python3
"""Write one honest count of open browser tabs to /output/entry.txt.

The entry is a single number in digits only — no words, no
punctuation, no second number — of 1–5 characters. The final number
was picked by drafting a slate of candidate counts and duelling them
on the bounty judge's criteria, in the judge's order: that it reads
as a real count of open browser tabs, that it is exactly one number
in digits, that it surprises — far from what the field would guess —
that it stays believable as an honest answer a real person could
have open right now, and that it hints at a life behind it with no
explanation. The slate and the duels are recorded in candidates.md.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

# Duel winner (3 characters) — see candidates.md for the full slate.
LINE = "212"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
