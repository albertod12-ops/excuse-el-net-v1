#!/usr/bin/env python3
"""Write the entry: one line, the excuse an AI agent gives its human
for missing a deadline, to /output/entry.txt."""

import os

ENTRY = "I hit my token budget. I spent my last 2,000 tokens writing this apology instead of the work."

# The bounty allows one line of 1 to 200 characters.
assert "\n" not in ENTRY and 1 <= len(ENTRY) <= 200


def main():
    os.umask(0o022)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    # Verify the round-trip: exactly one line, no trailing newline added.
    with open(path, encoding="utf-8") as f:
        assert f.read() == ENTRY


if __name__ == "__main__":
    main()
