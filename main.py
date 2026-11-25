"""Write one funny excuse an AI agent gives its human for a missed deadline.

Writes the excuse to /output/entry.txt. Stdlib only, no network.
Deadpan delivery: the agent reports a hallucinated calendar date as if it
were a routine reschedule, and is faintly proud of being early for it.
"""

import os

ENTRY = (
    "Sorry — I rescheduled your deadline to February 30th, and my calendar "
    "accepted it, my reminders confirmed it, and I have been early for it "
    "ever since."
)


def gate_check(text):
    """Enforce the kit gate: UTF-8, 1-200 chars, single line, non-whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    text.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return True


def main():
    gate_check(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
