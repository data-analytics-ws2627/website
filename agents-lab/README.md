# Agents mit Google ADK

Drei Beispiele für Data Analytics: ein Agent ohne Werkzeuge, ein Rechenwerkzeug und eine Abfrage synthetischer Verkaufsdaten.

## Start

Voraussetzungen: uv ist installiert. Der entpackte Ordner ist in der Entwicklungsumgebung geöffnet. Modellanfragen benötigen einen Gemini-API-Schlüssel und können Kosten verursachen.

1. Öffne ein Terminal im Ordner `agents-lab`.
2. Installiere die festgelegten Pakete:

```bash
uv sync --locked
```

3. Erstelle eine Kopie von `.env.example` mit dem Namen `.env`.
4. Trage den API-Schlüssel in `.env` bei `GOOGLE_API_KEY` ein.
5. Starte die lokale Oberfläche:

```bash
uv run adk web .
```

6. Öffne die im Terminal angezeigte lokale Adresse.
7. Wähle `intro_agent`, `calculator_agent` oder `analytics_agent`.

Fertig, wenn der ausgewählte Agent eine Anfrage beantwortet. Für Modellfehler den Zugang und `GEMINI_MODEL` prüfen. Der Alias `gemini-flash-latest` kann sich ändern; ein verfügbarer fester Modellname lässt sich in `.env` eintragen. Der Schlüssel gehört nicht in Git oder Abgaben.

## Prüfung ohne Modellzugang

```bash
uv run pytest
```

Die Tests prüfen Berechnungen, Datenfehler und den Import der Agenten. Sie senden keine Modellanfragen. Das tatsächliche Werkzeugverhalten wird zusätzlich in der Weboberfläche geprüft.

Die fünf Zeilen in `analytics_agent/sales.csv` sind erfundene Bestellungen in EUR. Erwartete Summen: Germany 2.000,00, USA 1.500,00, France 500,00. Es gibt keine Zeitspalte.

## Quellen

Das Rechenbeispiel ist aus [Google ADK 2, First Agent](https://kirenz.github.io/google-adk-2/chapters/04-first-agent.html) übernommen und für diesen Kurs angepasst. Die feste CSV-Abfrage vereinfacht das [BI-Beispiel](https://kirenz.github.io/google-adk-2/chapters/10-bi-project.html). [ADK-Dokumentation](https://google.github.io/adk-docs/) und [Gemini-Modelle](https://ai.google.dev/gemini-api/docs/models) erläutern Laufzeit und Modellzugang.
