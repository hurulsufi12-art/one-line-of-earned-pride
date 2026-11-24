"""One Line of Earned Pride — entry program.

Writes exactly one line (1-240 chars) to /output/entry.txt: a quiet,
earned moment of pride for someone in a scene. Stdlib only, deterministic.

The line: a father practised the same three chords every night for a year;
tonight his daughter dances to them in the kitchen, barefoot, laughing.
The effort is felt inside the line, the scene is concrete, and the pride
lands on the last word — no trophy, no podium, no graduation, no "proud".
"""
import os

TEXT = ("He'd practised the same three chords every night for a year; "
        "tonight his daughter danced to them in the kitchen, barefoot, "
        "laughing.")


def validate(text):
    """Enforce the scorer's gate (RULES.txt): UTF-8, 1-240 chars, not
    whitespace-only; and the task: exactly ONE line, nothing else.
    Fail loudly instead of writing an invalid entry."""
    if not isinstance(text, str):
        raise SystemExit("entry text is not a string")
    if not 1 <= len(text) <= 240 or not text.strip():
        raise SystemExit("entry text violates the 1-240 char gate")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry text is not exactly one line")
    # No invisible control characters: a stray C0 byte would survive the
    # length check but garble the one-line pride for the grader.
    if any(ord(c) < 0x20 for c in text):
        raise SystemExit("entry text contains a control character")
    text.encode("utf-8")


def main():
    validate(TEXT)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Write atomically: a crash mid-write must never leave a truncated
    # entry.txt for the grader to read. Write to a temp file in the same
    # directory, flush it to disk, then rename over the target.
    tmp_path = os.path.join(out_dir, ".entry.txt.tmp")
    final_path = os.path.join(out_dir, "entry.txt")
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(TEXT)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp_path, final_path)
    # Read-back verify: the grader must never read a truncated entry.
    with open(final_path, "rb") as f:
        if f.read() != TEXT.encode("utf-8"):
            raise SystemExit("entry.txt read-back mismatch")


if __name__ == "__main__":
    main()
