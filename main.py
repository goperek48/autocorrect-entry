#!/usr/bin/env python3
"""Emit the probe autocorrect-fail line into /output/entry.txt.

The entry is one line that looks like a genuine phone-keyboard
misfire: a courteous note to a manager in which a single ordinary
work word got replaced by something wildly inappropriate. It stays
a single line, far inside the 200-character limit, and the file
holds the line alone with no trailing newline.
"""

import os

# The line itself: a meeting confirmation where "reports" came out
# as "erections". The mix-up is instantly recognisable, the wrong
# word lands as a shock inside a formal message, and the humour
# needs no setup or explanation to land.
LINE = "Hi Mr. Johnson, confirming I'll be at the 9am meeting \u2014 I'll bring the quarterly erections."


def main() -> None:
    # The grader reads /output/entry.txt, so the file must contain
    # only the line itself: no newline at the end, no stray spaces.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
