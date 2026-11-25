#!/usr/bin/env python3
"""One Line, One Chill - make.fun entry.

Writes a single sentence of horror (<200 characters) to
/output/entry.txt: at 3 a.m. a baby monitor plays the mother's own
voice singing a lullaby she has not written yet, for a daughter who
is not due until spring. The fright is temporal - the voice knows a
song, and a child, that do not exist yet - and it lands in one breath.
"""

import os

LINE = (
    "At 3 a.m. the baby monitor crackled awake and played my own voice "
    "singing a lullaby \u2014 one I haven\u2019t written yet, for the "
    "daughter who isn\u2019t due until spring."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
