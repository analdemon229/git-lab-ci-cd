from pathlib import Path
import inspect
from src import greetings

version = Path("VERSION").read_text(encoding="utf-8").strip()

lines = [
    "# Документация",
    "",
    f"Версия: {version}",
    "",
    "## Функции",
    "",
]

for name, obj in inspect.getmembers(greetings, inspect.isfunction):
    if obj.__module__ == greetings.__name__:
        lines.extend([
            f"### {name}",
            "",
            inspect.getdoc(obj) or "Нет описания.",
            ""
        ])

Path("docs").mkdir(exist_ok=True)

Path("docs/GENERATED.md").write_text(
    "\n".join(lines),
    encoding="utf-8"
)

print("Документация создана")
