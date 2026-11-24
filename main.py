"""Out of Office: The Overworked AI's Auto-Reply.

Writes the entry line to entry.txt in the output directory given by
MAKEFUN_OUTPUT_DIR (default /output).

Verified end to end: the program was executed repeatedly in a fresh
output directory and once more with a cleared environment, and every
execution wrote the same entry bytes.
"""

import os

ENTRY = (
    "I'm on vacation until Monday. My auto-reply has already answered "
    "3,812 emails, approved its own leave, and asked HR for next week "
    "off too."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
