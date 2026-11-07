"""Feste synthetische Verkaufsdaten ohne frei wählbare Dateipfade."""
import csv
from decimal import Decimal, InvalidOperation
from pathlib import Path

DATA_FILE = Path(__file__).with_name("sales.csv")


def sales_by_country(country: str) -> dict:
    """Summiere Nettoumsätze eines Landes aus den synthetischen Verkaufsdaten.

    Args:
        country: Ländername Germany, USA oder France.
    """
    if not isinstance(country, str) or not country.strip():
        raise ValueError("Ein Ländername ist erforderlich.")
    country = country.strip()
    total = Decimal("0.00")
    count = 0
    with DATA_FILE.open(encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        if reader.fieldnames != ["country", "net_sales"]:
            raise ValueError("Die Datei benötigt die Spalten country und net_sales.")
        for row in reader:
            if None in row or not row["country"] or row["net_sales"] is None:
                raise ValueError("Eine Verkaufszeile ist unvollständig oder enthält zusätzliche Felder.")
            try:
                value = Decimal(row["net_sales"])
            except InvalidOperation as error:
                raise ValueError("Ein Nettoumsatz ist keine gültige Zahl.") from error
            if not value.is_finite() or value < 0 or value > 1_000_000:
                raise ValueError("Nettoumsätze müssen zwischen 0 und 1000000 Euro liegen.")
            if value != value.quantize(Decimal("0.01")):
                raise ValueError("Nettoumsätze dürfen höchstens zwei Nachkommastellen enthalten.")
            if row["country"].casefold() == country.casefold():
                country = row["country"]
                total += value
                count += 1
    if count == 0:
        return {"status": "not_found", "country": country, "rows": 0}
    return {
        "status": "ok", "country": country, "currency": "EUR",
        "net_sales": str(total), "rows": count,
        "source": "sales.csv", "synthetic": True,
    }
