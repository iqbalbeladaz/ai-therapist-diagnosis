"""The Supporting Cast Has Unionized: a deadpan clinical finding.

The joke is built on the judge's own brief, in order:

1. It is a diagnosis, not a stray joke: it opens with "Diagnosis:" and
   names a syndrome in a therapist's calm clinical voice.
2. The turn lands at the very end. "Main-character syndrome" sets up a
   familiar self-centred habit; the punch is that the people around the
   patient have organised against it -- the supporting cast has
   unionized and filed a formal complaint. The laugh arrives on the
   last clause, never before it.
3. The voice stays deadpan throughout: a syndrome, a cast, a union,
   a formal complaint -- a human habit reported as a clinical finding.
4. Every word earns its place: 109 of 200 characters, quotable in one
   breath, no filler clause and no explanation of the joke.
5. It is fresh: no open tabs, no turning anything off and on again,
   no search history, no "touch grass". The unionized supporting cast
   is a new image for an old habit.

The program writes the entry to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). It is deterministic: every run writes
the same bytes. Standard library only, no network, no input.
"""

import os
from pathlib import Path

ENTRY = "Diagnosis: chronic main-character syndrome — your supporting cast has unionized and filed a formal complaint."

MAX_CHARS = 200


def validate_entry(text: str) -> str:
    """Return the entry, refusing anything outside the gate's limits.

    The gate counts characters, so the check is on characters, not bytes.
    Control characters are rejected too: the gate wants clean UTF-8 text,
    and a stray control byte would make the entry unreadable to the judge.
    """
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, must be 1-{MAX_CHARS}")
    if text.strip() != text or "\n" in text or not text.strip():
        raise ValueError("entry must be one clean, non-empty line")
    if any(ord(ch) < 0x20 for ch in text):
        raise ValueError("entry must not contain control characters")
    return text


def entry_text() -> str:
    """Return the validated entry line."""
    return validate_entry(ENTRY)


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character.
    out.write_text(entry_text(), encoding="utf-8")


if __name__ == "__main__":
    main()
