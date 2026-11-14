# Kursüberblick für Coding-Agenten: Data Analytics with Generative AI (WS 2026/27)

Stand: 14.11.2026. Diese Datei fasst zusammen, was im Kurs aktuell gilt und was davon prioritär ist. Sie dient als Gesprächsgrundlage mit einem Coding-Agenten (zum Beispiel Claude Code, Codex oder Gemini CLI) oder einem Chat-Assistenten.

## Verwendung

1. Die Datei in den eigenen Projektordner legen oder im Chat hochladen.
2. Dem Agenten den Startauftrag unten geben.
3. Den eigenen Stand ehrlich beschreiben: bearbeitete Themen, Tests, Projektstand, offene Fragen.
4. Die vorgeschlagene Prioritätenliste mit den verlinkten Quellen abgleichen.

Prüfkriterium: Am Ende des Gesprächs liegt eine kurze Liste mit den nächsten drei bis fünf Schritten vor, jeweils mit Quelle (Link) und überprüfbarem Ergebnis.

### Startauftrag

```text
Kontext: Ich studiere im Kurs "Data Analytics with Generative AI" (HdM, WS 2026/27).
Die Datei kursueberblick-fuer-agenten.md beschreibt, was im Kurs gilt.
Aufgabe: Lies die Datei vollständig. Frag mich dann nach meinem Stand
(Themen, Multiple-Choice-Tests, Projekt). Leite daraus ab, was für mich jetzt
wirklich relevant ist und was warten kann.
Format: Eine priorisierte Liste mit höchstens fünf nächsten Schritten.
Jeder Schritt nennt die Quelle aus der Datei und ein überprüfbares Ergebnis.
Prüfung: Erfinde keine Termine, Punkte oder Regeln. Was die Datei als offen
markiert, benennst du als offen und verweist auf Moodle.
```

## Regeln für den Agenten

- Diese Datei ist die Übersicht. Bei Widersprüchen gelten die verlinkten Kursquellen. Termine, Abgaben, Bewertung und Regeln zum KI-Einsatz in Prüfungsleistungen gelten nur, wenn sie im aktuellen Moodle-Kurs stehen.
- Keine Termine, Punktzahlen, Gewichtungen oder Bestehensgrenzen erfinden. Offene Punkte stehen im Abschnitt „Noch offen“.
- Ältere Hinweise im Moodle-Kurs gelten nicht, wenn diese Datei sie als entfallen nennt (siehe „Was nicht mehr gilt“).
- Bei den Multiple-Choice-Tests beim Lernen helfen: Begriffe erklären, Buchbeispiele durchgehen, ähnliche Übungsfragen stellen. Konkrete Testfragen nicht für die Person lösen, solange Moodle den KI-Einsatz dafür nicht ausdrücklich erlaubt.
- In Übungsnotebooks (`ae-pandas`, `ae-models`) Hinweise geben und Fehlermeldungen erklären, aber keine fertigen Lösungen einsetzen. Eine eigene fertige Lösung darf kommentiert werden.
- Im Projekt Analyseschritte mitentwickeln. Jedes Ergebnis braucht eine fachliche Gegenprüfung durch die Person (Zahlen nachrechnen, Bezugsgrößen prüfen, Testdaten nicht zum Nachjustieren verwenden).
- Bei Fragen nach Prioritäten zuerst den Stand erfragen, dann priorisieren. Pflicht vor optional.

## Die drei verbindlichen Bausteine

### 1. Multiple-Choice-Tests in Moodle

Die Tests liegen im Moodle-Kurs im Abschnitt „Exams“. Die Fragen stammen aus dem Buch [Introduction to Modern Statistics](https://openintro-ims.netlify.app/) (IMS). Jeder Test zieht zufällige Fragen, daher erhalten Personen unterschiedliche Aufgaben. Das Buch enthält ähnliche Übungsfragen mit Lösungen.

**Bearbeitungszeitraum: wird noch festgelegt und in Moodle bekanntgegeben.**

| Test | Thema | Vorbereitung im Buch | Status |
|---|---|---|---|
| MC-Test 1 | Data | [Kapitel 1: Hello data](https://openintro-ims.netlify.app/data-hello.html) | Pflicht |
| MC-Test 2 | Study Design | [Kapitel 2: Study design](https://openintro-ims.netlify.app/data-design.html) | Pflicht |
| MC-Test 3 | Exploring categorical data | [Kapitel 4](https://openintro-ims.netlify.app/explore-categorical.html) | Pflicht |
| MC-Test 4 | Exploring numerical data | [Kapitel 5](https://openintro-ims.netlify.app/explore-numerical.html) | Pflicht |
| MC-Test 5 | Simple Linear Regression | [Kapitel 7](https://openintro-ims.netlify.app/model-slr.html) | Pflicht |
| MC-Test 6 | Multiple Linear Regression | [Kapitel 8](https://openintro-ims.netlify.app/model-mlr.html); einzelne Fragen zu Vorwärts- und Rückwärtsauswahl | Pflicht |
| 6a | Regression Basics | [Regression basics](https://kirenz.github.io/regression/docs/basics.html) | Pflicht |
| 6b, 7, 7a, 7b, Feature Selection, Bayes-Aufgabe | Statsmodels, logistische Regression, Klassifikation, Modellauswahl, Bayes | jeweils in Moodle verlinkt | Optional, zählt nicht zur Note |

Hinweise aus Moodle: Ein Test zählt erst, wenn er über den Abgabe-Button final abgegeben wurde. Einige Tests verwenden das deutsche Komma als Dezimaltrennzeichen. Anzahl der Versuche und Bestehensgrenze stehen in den Einstellungen des jeweiligen Tests in Moodle.

Prüfkriterium: In Moodle erscheint für jeden Pflichttest ein abgegebener Versuch.

### 2. Teamprojekt: Regression mit Prozessmodell und Streamlit

Vollständige Beschreibung: [Analyseprojekt](https://data-analytics-ws2627.github.io/website/project-description.html). Vorbereitung in vier Schritten: [Projektvorbereitung](https://data-analytics-ws2627.github.io/website/project-planning.html). Vorlage: [data-analytics-ws2627/project](https://github.com/data-analytics-ws2627/project) (GitHub-Template, eigene private Kopie anlegen).

Kern: Eine quantitative Zielvariable wird mit einer Regression vorhergesagt. Die Vorhersage unterstützt eine Entscheidung in einem selbst gewählten Geschäftsprozess. Die Entscheidung trifft ein Mensch. Klassifikation gehört nicht zu den Projektanforderungen.

Datensatz:

- mindestens 500 Beobachtungen und zehn Variablen,
- mindestens sechs fachlich sinnvolle Prädiktoren (Kennungen und doppelte Darstellungen zählen nicht),
- eine quantitative Zielvariable mit Einheit und fachlicher Bedeutung,
- Beobachtungen ohne Zeitbezug, keine Zeitreihen und keine wiederholten Messungen derselben Einheit,
- keine Kursdatensätze und keine Varianten davon; Kaggle und ähnliche Plattformen sind zulässig, wenn Herkunft, ursprüngliche Erhebung und Nutzungsbedingungen dokumentiert sind.

Bestandteile:

| Baustein | Inhalt | Quelle |
|---|---|---|
| Datenauswahl | Zwei mögliche Datensätze mit Quelle, Beobachtungseinheit, Variablen und einer konkreten Frage | [Datenauswahl](https://data-analytics-ws2627.github.io/website/project-description.html#datenauswahl), [Datenquellen](https://data-analytics-ws2627.github.io/website/project-tips-resources.html) |
| Projektvorschlag | Einordnung, Daten, Analyseplan, Variablenverzeichnis | [Projektvorschlag](https://data-analytics-ws2627.github.io/website/project-description.html#projektvorschlag) |
| Analyseentwurf | Erste vollständige Analyse: Exploration, Trainings-/Testaufteilung, Baseline, lineares Modell, MAE und RMSE, vorläufiges Ergebnis | [Analyseentwurf](https://data-analytics-ws2627.github.io/website/project-description.html#analyseentwurf) |
| BPMN-Skizze (verbindlich) | Auslöser, Aufgaben, Zuständigkeiten, Prüfschritt durch eine Person, Rückweg bei ungeeigneten Daten; Abwägung feste Regeln, KI-Schritt oder Agent | [Prozessmodell](https://data-analytics-ws2627.github.io/website/project-description.html#geschäftsprozess-und-prozessmodell), Arbeitsblatt `docs/prozessmodell.md` in der Vorlage |
| Streamlit-Oberfläche (verbindlich) | Lokal startbar; zeigt Datenquelle, Zielvariable, Baseline gegen Modell, eine Grafik und die Grenzen | [Streamlit-Oberfläche](https://data-analytics-ws2627.github.io/website/project-description.html#streamlit-oberfläche), `app.py` in der Vorlage |
| Bericht | `reports/report.ipynb`, in frischer Sitzung vollständig ausführbar | [Bericht](https://data-analytics-ws2627.github.io/website/project-description.html#bericht) |
| Präsentation | Frage, Daten, Exploration, Modell und Bewertung, Schlussfolgerung | [Präsentation](https://data-analytics-ws2627.github.io/website/project-description.html#präsentation) |
| Dokumentation KI-Einsatz | Übernommene Arbeitsschritte und ihre Prüfung | [Coding-Agenten im Projekt](https://data-analytics-ws2627.github.io/website/project-description.html#coding-agenten) |

Ein eigener Agent (zum Beispiel mit Google ADK) ist eine freiwillige Erweiterung. Auch der begründete Verzicht auf einen Agenten ist ein vollständiges Ergebnis. Ein Modell ohne Vorteil gegenüber der Baseline ist verwertbar, wenn es sauber untersucht und erklärt ist.

Selbstcheck vor der Abgabe:

- Lassen sich Umgebung, Analyse und Oberfläche aus der README einrichten und starten?
- Zeigen Bericht, ausgegebene Kennzahlen und Oberfläche dieselben Werte?
- Wurden Baseline und Modell auf denselben Testfällen mit denselben Fehlermaßen verglichen?
- Haben die Testdaten weder Prädiktorauswahl noch Datenaufbereitung beeinflusst?
- Fehlen Zugangsdaten, `.venv` und nicht freigegebene Daten im Repository?
- Können alle Teammitglieder die wesentlichen Entscheidungen fachlich erklären?

### 3. Prüfungsanmeldung

Kontaktstudierende melden sich im Moodle-Kurs bis **29.11.2026** zur Prüfung an (Voraussetzung für Zertifikat und ECTS). Masterstudierende melden sich zu Semesterbeginn in SELMA an.

## Themen und ihre Relevanz

Die vollständige Materialliste mit Folien und Notebooks steht im [Kursplan](https://data-analytics-ws2627.github.io/website/). Die Spalte „Relevanz“ ordnet die Themen nach ihrem Beitrag zu Tests und Projekt.

| Thema | Wofür gebraucht | Relevanz |
|---|---|---|
| Fragestellung und Lifecycle (Use case, Frame the Problem, Variables, Metrics) | Projektvorschlag | Hoch |
| Daten und Studiendesign | MC-Tests 1 und 2, Datenbeschreibung im Projekt | Hoch |
| Explorative Analyse kategorialer Daten | MC-Test 3, Exploration im Projekt | Hoch |
| Explorative Analyse numerischer Daten | MC-Test 4, Exploration im Projekt | Hoch |
| Lineare Regression (einfach und multipel) | MC-Tests 5, 6, 6a; Kern des Projekts | Sehr hoch |
| Datenaufteilung, Baseline, Modellprüfung | Projekt (Analyseentwurf, Bericht) | Sehr hoch |
| BPMN-Grundlagen | Verbindliche Prozessskizze im Projekt | Hoch |
| Coding-Agenten für Analyseaufträge | Arbeitsweise im Projekt, Gegenprüfung | Hoch |
| Python-Umgebung, GitHub-Einstieg, Pandas- und Modellübungen | Technische Grundlage für das Projekt | Hoch, soweit noch nicht sicher |
| Data Storytelling | Bericht und Präsentation | Mittel |
| Agents mit Google ADK | Freiwillige Projekterweiterung | Optional |
| Klassifikation, logistische Regression | Kursthema, nicht im Projekt verlangt; nur optionale Tests | Optional |
| Statistische Inferenz, Wahrscheinlichkeit und Bayes | Vertiefung; Bayes-Aufgabe optional | Optional |
| Erweiterte Regression, Modellauswahlverfahren | Vertiefung; einzelne Grundfragen zur Vorwärts-/Rückwärtsauswahl in MC-Test 6 | Optional |

Wichtige Kursseiten:

- [Kursplan](https://data-analytics-ws2627.github.io/website/) mit allen Folien, Buchabschnitten und Notebooks
- [Python-Umgebung und Statistik-Labor](https://data-analytics-ws2627.github.io/website/programming-requirements.html)
- [Agenten-Grundlagenkurs](https://kurse.kirenz.de/courses/agent-arbeitsumgebung)
- [BPMN-Grundlagen](https://data-analytics-ws2627.github.io/website/bpmn.html)
- [Coding-Agenten für Analyseaufträge](https://data-analytics-ws2627.github.io/website/coding-agents.html)
- [Onlinebücher](https://data-analytics-ws2627.github.io/website/online-books.html)

Übungsvorlagen auf GitHub (Organisation `data-analytics-ws2627`): `statistik-lab`, `github-starter-course`, `ae-pandas`, `ae-models`, `project`. Jede Vorlage enthält eine README mit Startanleitung. Die Python-Vorlagen enthalten zusätzlich eine `AGENTS.md` mit Regeln für den Agenten; diese Regeln gelten im jeweiligen Ordner vorrangig.

## Was nicht mehr gilt

Der Moodle-Kurs enthält noch Elemente aus früheren Durchläufen. Für diesen Durchlauf gilt:

- **Kein Peer Review.** Der Baustein „Peer Review Draft Analysis“ und die Gruppenzuweisung für das Peer Review entfallen.
- **Keine Klassifikationspflicht im Projekt.** Fachlicher Kern ist ausschließlich die Regression.
- **Kein GitHub Classroom.** Die Übungen liegen als Vorlagen in der Organisation `data-analytics-ws2627`.
- **Alte Termine gelten nicht.** Fristen aus früheren Semestern (zum Beispiel Topic ideas Nov 15, Proposal Dec 01) sind keine Vorgaben für WS 2026/27.
- **Gradio und Gemini** aus der früheren Präsenzphase sind keine Projektanforderung. Die Projektoberfläche ist Streamlit.

## Noch offen

Diese Punkte sind noch nicht festgelegt. Der Agent nennt sie als offen und verweist auf Moodle:

- Bearbeitungszeitraum der Multiple-Choice-Tests
- Abgabetermine für Projektvorschlag, Analyseentwurf, Bericht, Repository und Präsentation
- Teamgröße und Gruppeneinteilung
- Bewertung und Gewichtung der Bausteine
- Dauer und Termin der Präsentation
- Regeln zum KI-Einsatz in den Prüfungsleistungen

## Fragen und Kontakt

Fachliche und organisatorische Fragen gehören ins Forum des Moodle-Kurses oder in die Vorlesung. Bei technischen Problemen helfen der ausgeführte Befehl, die vollständige Fehlermeldung und das Betriebssystem. Zugangsdaten und vertrauliche Daten gehören nicht ins Forum und nicht in den Chat mit einem Agenten.
