"""Funniest Autocorrect Fail: writes the entry text to /output/entry.txt.

Why this line: Reads as a real slip, not a written joke: one clear wrong word (report -> raccoon), specific and original, and the fallout (buying a tiny tie) is the punch.
"""

import os

ENTRY = "I meant to text my boss 'I'll bring the quarterly report' but autocorrect sent 'I'll bring the quarterly raccoon' and now I have to buy a tiny tie."

OUTPUT_PATH = "/output/entry.txt"


def main():
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
