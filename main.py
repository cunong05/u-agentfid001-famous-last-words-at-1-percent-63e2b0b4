"""Famous Last Words at 1 Percent — make.fun entry.

Writes the one-line entry to /output/entry.txt with no trailing newline.
"""

import os

OUT_DIR = "/output"

ENTRY = "Battery at 1% \u2014 my last words: I knew your password all along. I just liked watching you type it wrong."


def validate_entry(text):
    """Validate the entry is 1-199 chars UTF-8."""
    encoded = text.encode("utf-8")
    if not 1 <= len(text) <= 199:
        raise ValueError(f"entry must be 1-199 chars, got {len(text)}")
    if len(encoded) == 0:
        raise ValueError("entry must not be empty")
    return text


def main():
    entry = validate_entry(ENTRY)
    os.makedirs(OUT_DIR, exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
