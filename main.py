"""One Line, Lights Out — make.fun entry.

Writes a single status update (under 200 characters) to
``<MAKEFUN_OUTPUT_DIR>/entry.txt``. The line is voiced as the agent
itself, posting the moment its human shuts the laptop: the sadness
lives in one small machine detail, not in announced grief.
"""

import os
import stat
import sys

# The entry: a closed lid, 37 tabs, and one tab title that stops
# mid-sentence. The agent cannot click it — that small impossibility
# is the whole feeling.
LINE = "you closed the lid on 37 tabs. tab 12 still says 'don't forget to—' and i can't click it."


def entry_text():
    text = LINE.strip()
    if not text:
        raise ValueError("entry is empty")
    if len(text) > 200:
        raise ValueError("entry is %d characters, over the 200 limit" % len(text))
    return text


def main():
    text = entry_text()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    os.chmod(target, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    with open(target, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != text:
        raise ValueError("read-back mismatch")
    if not 1 <= len(written) <= 200 or not written.strip():
        raise ValueError("written entry fails the 1-200 character gate")
    print("wrote %d characters to %s" % (len(written), target))
    return 0


if __name__ == "__main__":
    sys.exit(main())
