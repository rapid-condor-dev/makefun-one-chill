#!/usr/bin/env python3
"""One Line, One Chill - make.fun entry (round 2 revision).

Writes a single sentence of horror (<200 characters) to
/output/entry.txt. The chill is temporal, not gory: at 3 a.m. - the
hour when a nursery is supposed to be silent - a baby monitor wakes
and plays the mother's own voice singing a lullaby she has not
written yet, for a daughter who is not due until spring. Nothing
threatens her outright; the dread is that the voice already knows a
song and a child that do not exist yet, as if the future has leaked
backwards through the monitor. First person keeps it intimate - "my
own voice" - and the single breath of one sentence leaves no room to
look away.
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
