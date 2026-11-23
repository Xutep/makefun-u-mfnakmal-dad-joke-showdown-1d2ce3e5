#!/usr/bin/env python3
"""Dad Joke Showdown entry (make.fun).

Writes one original dad joke to /output/entry.txt. Deterministic,
standard library only: the joke is a fixed string, so every run
produces byte-identical output.
"""

import os

JOKE = "I mow the lawn in straight lines so the neighbors know I'm not cutting corners."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
