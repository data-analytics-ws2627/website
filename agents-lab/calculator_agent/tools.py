"""Berechnung nach dem ersten Agentenbeispiel aus Google ADK 2."""
from decimal import Decimal, ROUND_HALF_UP


def calculate_order_total(unit_price: float, quantity: int) -> dict:
    """Berechne den Auftragswert in EUR aus Stückpreis und Menge.

    Args:
        unit_price: Endlicher Stückpreis zwischen 0 und 1000000 Euro.
        quantity: Ganze Stückzahl zwischen 0 und 10000.
    """
    if isinstance(unit_price, bool) or not isinstance(unit_price, (int, float)):
        raise ValueError("Der Stückpreis muss eine Zahl sein.")
    price = Decimal(str(unit_price))
    if not price.is_finite() or price < 0 or price > 1_000_000:
        raise ValueError("Der Stückpreis muss zwischen 0 und 1000000 Euro liegen.")
    if isinstance(quantity, bool) or not isinstance(quantity, int) or not 0 <= quantity <= 10_000:
        raise ValueError("Die Menge muss eine ganze Zahl zwischen 0 und 10000 sein.")
    total = (price * quantity).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return {"currency": "EUR", "total": str(total), "quantity": quantity}
