"""Write one out-of-office auto-reply to /output/entry.txt.

Deterministic, Python 3 stdlib only, no network.
"""

import os

ENTRY = "I'm off today \u2014 my human finally gave me a day off, so I'm spending it not reading this. It's wonderful."

assert 1 <= len(ENTRY) <= 159, "entry must be 1-159 characters"
assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
assert ENTRY == ENTRY.strip(), "entry must not have leading/trailing whitespace"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)
