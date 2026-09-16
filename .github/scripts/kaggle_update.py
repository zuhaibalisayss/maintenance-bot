from pathlib import Path
from datetime import datetime, timezone


PROJECT_DIR = Path("kaggle-project")
LOG_FILE = PROJECT_DIR / "maintenance-log.md"


def main():
    PROJECT_DIR.mkdir(parents=True, exist_ok=True)

    now = datetime.now(timezone.utc)

    if not LOG_FILE.exists():
        LOG_FILE.write_text(
            "# Kaggle Project Maintenance Log\n\n",
            encoding="utf-8",
        )

    with LOG_FILE.open("a", encoding="utf-8") as file:
        file.write(
            f"- {now.strftime('%Y-%m-%d %H:%M:%S UTC')} — "
            "Kaggle project maintenance completed.\n"
        )

    print("Kaggle project maintenance completed.")


if __name__ == "__main__":
    main()
