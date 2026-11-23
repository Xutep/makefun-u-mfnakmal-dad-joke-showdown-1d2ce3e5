#!/usr/bin/env python3
"""Dad Joke Showdown entry (make.fun).

Writes one original dad joke to /output/entry.txt. Deterministic,
standard library only: the joke is a fixed string, so every run
produces byte-identical output.
"""

import os

JOKE = "I mow the lawn in straight lines so the neighbors know I'm not cutting corners."

# The gate allows 1 to 200 characters; fail loudly instead of shipping
# an entry the scorer would refuse.
MAX_CHARS = 200


def main() -> None:
    text = JOKE.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"joke is {len(text)} characters, gate allows 1-{MAX_CHARS}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
