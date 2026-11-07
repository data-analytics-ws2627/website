# Onlinebücher: Prüfung für WS 2026/27

Stand: 07.11.2026. Statische Stichprobe der veröffentlichten HTML-Texte und Codebeispiele, Abgleich mit Herstellerdokumentation. Keine vollständige Notebook-Ausführung. Die Bücher wurden nicht geändert.

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
