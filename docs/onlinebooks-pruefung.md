# Onlinebücher: Prüfung für WS 2026/27

Stand der Erstprüfung: 07.11.2026. Die folgenden Befunde dokumentieren die veröffentlichte Fassung vor der lokalen Korrektur. Der Stand der anschließenden Umsetzung und Ausführungsprüfung steht am Ende dieses Dokuments.

## Belegte Befunde

| Buch / Kapitel | Befund | Auswirkung und Korrektur |
|---|---|---|
| [Data Science with Python: Model](https://kirenz.github.io/ds-python/docs/model.html) | `mean_squared_error(..., squared=False)` verwendet einen inzwischen entfernten Parameter. | Bei aktuellem scikit-learn scheitert der Aufruf. `root_mean_squared_error` verwenden und Beispiele in der Kursumgebung ausführen. |
| Regression Onlinebook | Derselbe RMSE-Aufruf steht in acht geprüften Kapiteln: [Splines](https://kirenz.github.io/regression/docs/splines.html), [Random Forest](https://kirenz.github.io/regression/docs/randomforest.html), [Gradient Boosting](https://kirenz.github.io/regression/docs/gradientboosting.html), [XGBoost](https://kirenz.github.io/regression/docs/xgboost-regression.html), [Gradient Boosting mit XGBoost](https://kirenz.github.io/regression/docs/gradientboosting-xgboost.html), [Duke](https://kirenz.github.io/regression/docs/case-duke-sklearn.html), [Happy](https://kirenz.github.io/regression/docs/ds-happy-scikit.html), [California Housing](https://kirenz.github.io/regression/docs/case-ca-housing.html). | API-Kompatibilität vor praktischer Nutzung herstellen. Fortgeschrittene Verfahren müssen dafür nicht in den Pflichtpfad aufgenommen werden. |
| [Data Science with Python: Data](https://kirenz.github.io/ds-python/docs/data.html) | `df_train.drop(y_label)` soll die Zielspalte entfernen, verwendet aber standardmäßig die Zeilenachse. | Bei üblichen numerischen Indizes entsteht ein KeyError. Explizit `drop(columns=[y_label])` verwenden. |
| [Toolkit: Umgebungen](https://kirenz.github.io/toolkit-de/python/python-umgebung.html), [uv-Projekt](https://kirenz.github.io/toolkit-de/uv/uv-projekt.html), [uv-Installation](https://kirenz.github.io/toolkit-de/uv/uv.html) | Umgebungsgrundlagen verwenden Conda; das uv-Projekt Python 3.11. Installation und Aktivierung orientieren sich an Shell-Befehlen, ohne eigenen PowerShell-Pfad. | Kein genereller technischer Fehler, aber nicht mit uv/Python 3.12/Kernel data-analytics im Kurs abgestimmt. Kursanleitung und https://github.com/kirenz/uv-setup als Ausgangspunkt verwenden. |
| [Regression: Lasso](https://kirenz.github.io/regression/docs/lasso.html) | Text beschreibt die ersten 70 Prozent als Training; `train_test_split` mischt standardmäßig zufällig. | Text und Code beschreiben unterschiedliche Aufteilungen. Erklärung an das tatsächliche Verfahren anpassen. |
| [Regression: Basics](https://kirenz.github.io/regression/docs/basics.html) | `np.sqrt(R_squared)` wird als Korrelation bezeichnet. | Im positiven Beispiel passend. Allgemein geht das Vorzeichen verloren; Geltungsbereich erklären. |

## Fachliche Einordnung

Der Lifecycle mit Plan, Data, Model und Deployment passt zur Kursstruktur. Im Data-Kapitel werden Testdaten früh getrennt und Datenleckage erklärt. Daraus folgt kein Anlass, die fachliche Struktur neu aufzubauen. Die Übersicht aus Grafik und Folien ersetzt keine schrittweise Erläuterung.

Datensatzabhängiges Risiko: Der Isolation-Forest-Abschnitt benötigt eine geeignete Behandlung kategorialer und fehlender Werte. Die konkrete Laufzeitwirkung wurde nicht ausgeführt.

Die statischen API-Befunde belegen Probleme mit aktuellen Bibliotheken. Welche älteren, festgelegten Paketversionen die veröffentlichten Beispiele gegebenenfalls benötigen, wurde nicht vollständig geprüft. Eine Freigabe sämtlicher Codebeispiele für Python 3.12 ist mit dieser Stichprobe nicht verbunden.

## Herstellerquellen

- [scikit-learn: mean_squared_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html)
- [scikit-learn: root_mean_squared_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.root_mean_squared_error.html)
- [pandas: DataFrame.drop](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html)
- [scikit-learn: train_test_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)
- [Astral: uv-Installation](https://docs.astral.sh/uv/getting-started/installation/)

## Lokale Aktualisierung auf uv und Python 3.14

Die drei Bücher werden lokal in `/Users/jankirenz/code/archive/books/` gepflegt. Jede Arbeitskopie enthält jetzt `pyproject.toml`, `.python-version` und `uv.lock`. Notebook-Kernel werden projektlokal registriert. Die bestehenden Buchformate bleiben erhalten. Die Onlinefassung wurde nicht veröffentlicht.

Toolkit: zentraler Einrichtungsweg über uv und Python 3.14; macOS-/Linux- und PowerShell-Befehle. Python 3.13.7, temporäres Projekt, Paketinstallation, Programmlauf und tatsächliche Notebook-Ausführung geprüft. Quarto rendert alle 36 Kapitel. Zwei bestehende Warnungen im unveränderten PostgreSQL-Kapitel bleiben. Prüfprotokoll: `/Users/jankirenz/code/archive/books/toolkit-de/docs/pruefung-python314.md`.

Data Science with Python: RMSE, IsolationForest mit Vorverarbeitung, numerische pandas-Zusammenfassungen, Variablenname und Fehlerauswahl korrigiert. Die betroffenen echten Codeblöcke laufen mit gemischten Testdaten einschließlich fehlender Werte und unbekannter Kategorie. Der vollständige digits-Gridsearch läuft; der Buchbuild besteht ohne Warnungen. Prüfprotokoll und Grenzen: `/Users/jankirenz/code/archive/books/ds-python/VALIDATION.md`.

Python 3.14: Zusätzlich isoliert mit CPython 3.14.9 geprüft. Toolkit: alle Abhängigkeiten installiert; echte Notebook-Ausführung über eigenen Kernel mit NumPy, pandas, SciPy, Matplotlib und Altair erfolgreich. Data Science with Python: alle 153 Laufzeit-/Build-Pakete installiert; identischer vollständiger Codeharness einschließlich digits-Gridsearch und Buchbuild erfolgreich. Die Hersteller weisen Unterstützung für aktuelle scikit-learn-, statsmodels- und pyGAM-Versionen aus. Nach den erfolgreichen isolierten Prüfungen wurde Python 3.14 ausdrücklich als verbindliche Zielversion gewählt. Projektkonfiguration, Lockdateien und Einrichtung sind entsprechend angepasst. Alle drei lokalen Projektumgebungen verwenden Python 3.14.9. Die ersten 3.13-Prüfungen bleiben als zusätzlicher Nachweis dokumentiert.

Unterstützungszeitraum laut [Python Developer Guide](https://devguide.python.org/versions/): Python 3.13 bis Oktober 2029, Python 3.14 bis Oktober 2030. Für längere Nutzbarkeit ist 3.14 bei bestandenen Anwendungstests vorzuziehen. Bibliotheks- und Inhaltswartung bleibt unabhängig davon erforderlich.

Die erste Umstellung betraf die drei Onlinebücher. Anschließend wurden auch Statistik-Labor und Kursvorlagen auf Python 3.14 migriert; siehe [Prüfung der Kursvorlagen](pruefung-kursvorlagen-python314.md). Windows-Befehle sind dokumentiert, aber nicht auf einem Windows-System ausgeführt.

Regression: Alle zehn betroffenen Notebooks wurden unter Python 3.13 vollständig ausgeführt, einschließlich der vollständigen California-Housing-Suchen. Unter Python 3.14.9 liefen neun Notebooks vollständig; California Housing wurde mit allen Zellen, aber reduziertem Suchumfang erfolgreich geprüft. Der reduzierte Lauf prüft API-Kompatibilität und ist kein Vergleich gleicher Modellgüte. Zusätzlich wurde pyGAM unter 3.14 mit fit/predict geprüft. Korrigiert wurden neben RMSE auch XGBoost early stopping, entfernte pandas-/GradientBoosting-Aufrufe, positionsbasierte Zugriffe, Boxplot-Parameter und HTML-Tabellenimport. Die Korrekturen und Suchgrenzen sind unter `/Users/jankirenz/code/archive/books/regression/VALIDATION.md` dokumentiert.

Der lokale Regressionsbuch-Build ist erfolgreich. Bestehende Plotly-MIME- und Archivnotebook-Warnungen bleiben. macOS benötigt für XGBoost die OpenMP-Laufzeit; im Test wurde diese ausschließlich unter dem ignorierten Prüfverzeichnis bereitgestellt. Es fand keine globale Systeminstallation statt. Die Einrichtung dokumentiert diese Voraussetzung.
