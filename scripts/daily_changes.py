from pathlib import Path
from datetime import datetime, timezone
import random


FILE = Path("daily-maintenance.md")


MAINTENANCE_MESSAGES = [
    "Updated automated maintenance record.",
    "Performed routine repository housekeeping.",
    "Refreshed repository maintenance log.",
    "Updated automated maintenance information.",
    "Performed routine documentation maintenance.",
]


def main():
    number_of_changes = random.randint(1, 5)

    now = datetime.now(timezone.utc)

    if FILE.exists():
        content = FILE.read_text(encoding="utf-8")
    else:
        content = "# Daily Repository Maintenance\n\n"

    for _ in range(number_of_changes):
        message = random.choice(MAINTENANCE_MESSAGES)

        content += (
            f"- {now.strftime('%Y-%m-%d %H:%M:%S UTC')} — "
            f"{message}\n"
        )

    FILE.write_text(content, encoding="utf-8")

    print(
        f"Successfully created {number_of_changes} "
        f"maintenance changes."
    )


if __name__ == "__main__":
    main()
