# Data Analytics with Generative AI · WS 2026/27

Kurswebsite auf Grundlage von [Data Analytics WS 2024/25](https://github.com/data-analytics-ws2425/website). Die bestehenden Folien, Buchverweise und Python-Notebooks bilden die Statistik-Grundlage. Ergänzt werden uv, die Arbeit mit Coding-Agenten und BPMN für Data-Science-Prozesse.

Die Startseite zeigt direkt den Kursplan mit den Unterlagen in Vorlesungsreihenfolge. Die Quelle `course-materials.qmd` erzeugt `index.html`; die bisherige Adresse `course-materials.html` leitet einschließlich Abschnittsanker dorthin weiter. Onlinebücher stehen unter einem eigenen Menüpunkt. Einordnung und Arbeitsformen stehen unter „Kursinformationen → Überblick“.

## Lokal ansehen

```bash
quarto preview --port 4200 --no-browser
```

```bash
quarto render
```

Die Ausgabe liegt in `_site/`. Die Website erscheint unter https://data-analytics-ws2627.github.io/website/. Der Workflow „Quarto Publish“ wird ausschließlich manuell über GitHub Actions ausgelöst. Er rendert die Website und veröffentlicht die Ausgabe über GitHub Pages.

Die ursprüngliche Organisation bleibt unverändert. Persönliche Abgaben und frühere Classroom-Einladungen werden nicht übernommen. Aktuelle Termine, Moodle-Zuordnung und Prüfungsmodalitäten werden im aktuellen Moodle-Kurs gepflegt.
