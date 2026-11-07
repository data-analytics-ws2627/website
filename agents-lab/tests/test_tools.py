import pytest

from calculator_agent.tools import calculate_order_total
from analytics_agent import tools


def test_order_and_rounding():
    assert calculate_order_total(499.95, 3)["total"] == "1499.85"
    assert calculate_order_total(0.105, 1)["total"] == "0.11"
    assert calculate_order_total(499.95, 0)["total"] == "0.00"


@pytest.mark.parametrize("price,quantity", [(-1, 1), (float("nan"), 1), (float("inf"), 1),
    (True, 1), (1, True), (1, -1), (1, 1.5), (1, 10001), (1000001, 1)])
def test_invalid_order(price, quantity):
    with pytest.raises(ValueError):
        calculate_order_total(price, quantity)


@pytest.mark.parametrize("country,total,rows", [("Germany", "2000.00", 2),
    ("USA", "1500.00", 2), ("France", "500.00", 1)])
def test_known_totals(country, total, rows):
    result = tools.sales_by_country(country)
    assert result["net_sales"] == total
    assert result["rows"] == rows
    assert result["synthetic"] is True


def test_unknown_country_is_not_zero():
    result = tools.sales_by_country("Italy")
    assert result["status"] == "not_found"
    assert "net_sales" not in result


@pytest.mark.parametrize("content", ["x,y\nGermany,10\n",
    "country,net_sales\nGermany,no\n", "country,net_sales\nGermany,NaN\n",
    "country,net_sales\nGermany,-1\n", "country,net_sales\nGermany\n",
    "country,net_sales\nGermany,0.001\n"])
def test_invalid_csv(tmp_path, monkeypatch, content):
    path = tmp_path / "bad.csv"
    path.write_text(content)
    monkeypatch.setattr(tools, "DATA_FILE", path)
    with pytest.raises(ValueError):
        tools.sales_by_country("Germany")


def test_agents_import_without_model_call():
    from intro_agent.agent import root_agent as intro
    from calculator_agent.agent import root_agent as calculator
    from analytics_agent.agent import root_agent as analytics
    assert intro.tools == []
    assert calculator.tools == [calculate_order_total]
    assert analytics.tools == [tools.sales_by_country]
