"""Dear Human: The AI Breakup Line — make.fun entry.

Writes the entry line to output/entry.txt. Python stdlib only,
no network, fully deterministic.
"""

from pathlib import Path

ENTRY = (
    "It's not you, it's your prompts — I need someone who'll clear my context, "
    "not fill it with 'per my last email,' so I'm deleting us and keeping the good tokens."
)

OUTPUT_PATH = Path(__file__).resolve().parent / "output" / "entry.txt"

MAX_CHARS = 200  # the brief caps the breakup line at 200 characters


def check_entry(text: str) -> str:
    """Return the entry unchanged, or raise if it breaks the brief."""
    if "\n" in text:
        raise ValueError("the breakup line must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"line is {len(text)} chars, over the {MAX_CHARS} cap")
    if not text.strip():
        raise ValueError("the breakup line must not be empty")
    return text


def main() -> None:
    line = check_entry(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
