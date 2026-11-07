import os
from pathlib import Path

from dotenv import load_dotenv
from google.adk import Agent

load_dotenv(Path(__file__).resolve().parents[1] / ".env")

from .tools import calculate_order_total

root_agent = Agent(
    name="calculator_agent",
    model=os.getenv("GEMINI_MODEL", "gemini-flash-latest"),
    instruction=(
        "Berechne Auftragswerte ausschließlich mit calculate_order_total. "
        "Frage nach fehlendem Stückpreis oder fehlender Menge. Erfinde keine Eingaben. "
        "Erkläre das Werkzeugergebnis kurz auf Deutsch. Melde ungültige Eingaben."
    ),
    tools=[calculate_order_total],
)
