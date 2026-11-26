#!/usr/bin/env python3
"""Rename the Planet — make.fun entry (program/v1).

Writes one line (<200 chars) to /output/entry.txt: a funny new name
for a planet in our solar system, plus the why, in the same breath.
Fully deterministic: no randomness, no clock, no network.
"""

import os

LINE = (
    "Mercury is now 'The Intern' \u2014 it laps the Sun every 88 days "
    "and still gets called 'the small one'."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) < 200, f"entry length {len(text)} out of range"
    assert "\n" not in text, "entry must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
