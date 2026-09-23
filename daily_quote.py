"""Print a small daily message based on the current date.

The script uses only Python's standard library, so it can be run directly
without installing any dependencies.
"""

from datetime import date


MESSAGES = (
    "Small steps still move you forward.",
    "Make today a little clearer than yesterday.",
    "Curiosity is a good reason to begin.",
    "A finished draft beats a perfect idea.",
    "Keep going; consistency compounds.",
)


def message_for(day: date) -> str:
    """Return a deterministic message for *day*."""

    return MESSAGES[day.toordinal() % len(MESSAGES)]


def main() -> None:
    """Print today's date and message."""

    today = date.today()
    print(f"{today.isoformat()}: {message_for(today)}")


if __name__ == "__main__":
    main()
