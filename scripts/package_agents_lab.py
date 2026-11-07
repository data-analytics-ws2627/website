"""Packe ausschließlich die Kursquellen des ADK-Labors."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

root = Path(__file__).resolve().parents[1]
lab = root / "agents-lab"
files = [
    ".env.example", ".gitignore", ".python-version", "README.md",
    "pyproject.toml", "uv.lock",
    "intro_agent/__init__.py", "intro_agent/agent.py",
    "calculator_agent/__init__.py", "calculator_agent/agent.py", "calculator_agent/tools.py",
    "analytics_agent/__init__.py", "analytics_agent/agent.py", "analytics_agent/tools.py",
    "analytics_agent/sales.csv", "tests/test_tools.py",
]
with ZipFile(root / "downloads/agents-lab.zip", "w", ZIP_DEFLATED) as archive:
    for name in files:
        archive.write(lab / name, "agents-lab/" + name)
print(f"ADK-Labor: {len(files)} Dateien gepackt.")
