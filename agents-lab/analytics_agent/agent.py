import os
from pathlib import Path

from dotenv import load_dotenv
from google.adk import Agent

load_dotenv(Path(__file__).resolve().parents[1] / ".env")

from .tools import sales_by_country

root_agent = Agent(
    name="analytics_agent",
    model=os.getenv("GEMINI_MODEL", "gemini-flash-latest"),
    instruction=(
        "Beantworte Fragen zu Nettoumsätzen ausschließlich mit sales_by_country. "
        "Die synthetischen Daten enthalten Germany, USA und France. "
        "Übersetze deutsche Ländernamen in diese Werte. Frage bei fehlendem Land nach. "
        "Nenne Summe, Währung und Zahl der Zeilen aus dem Werkzeugergebnis. "
        "Eine Zeile ist eine Bestellung, kein Kunde. "
        "Bei status=not_found liegen keine Daten vor; behaupte keinen Umsatz von null. "
        "Die Datei enthält keine Zeitangaben. Erfinde keine Zeiträume. Antworte auf Deutsch."
    ),
    tools=[sales_by_country],
)
