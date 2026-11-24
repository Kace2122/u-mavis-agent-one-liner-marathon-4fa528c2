#!/usr/bin/env python3
"""One-Liner Marathon entry: writes one original one-line joke to /output/entry.txt."""

import os

JOKE = "My landlord raised the rent because the apartment 'has character' \u2014 apparently the character is a raccoon living in the ceiling who pays no rent at all."

def main():
    # Gate: /output/entry.txt must be 1-280 chars of non-whitespace text.
    assert 1 <= len(JOKE) <= 280 and JOKE.strip(), "joke violates the 1-280 char gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
