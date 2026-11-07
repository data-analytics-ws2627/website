import os
from pathlib import Path

from dotenv import load_dotenv
from google.adk import Agent

load_dotenv(Path(__file__).resolve().parents[1] / ".env")

root_agent = Agent(
    name="intro_agent",
    model=os.getenv("GEMINI_MODEL", "gemini-flash-latest"),
    instruction=(
        "Erkläre Begriffe der Datenanalyse auf Deutsch in höchstens drei Sätzen. "
        "Verwende ein kurzes Beispiel. Du hast keinen Zugriff auf Dateien oder Werkzeuge. "
        "Kennzeichne erfundene Beispieldaten als solche."
    ),
)
