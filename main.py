"""How Many Tabs Do You Have Open? entry.

Writes one honest tab count to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(default ``/output``). Python 3.13 standard library only; no
network, no randomness.

The count: 137. A specific, non-round number -- the kind of count
you only get by actually having that many tabs open. Big enough to
surprise, small enough to believe: years of "I'll read this later"
tabs across a few windows, none ever closed. Round numbers look
guessed and huge ones look picked to shock; 137 looks counted.
"""

import os

COUNT = "137"


def main() -> None:
    # Self-check against the gate before writing: digits only, 1-5 chars.
    assert COUNT.isdigit() and 1 <= len(COUNT) <= 5, COUNT
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(COUNT)


if __name__ == "__main__":
    main()
