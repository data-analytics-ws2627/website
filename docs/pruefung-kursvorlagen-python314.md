# Statistik-Labor und Kursvorlagen: Python 3.14

Stand: 07.11.2026. Sämtliche Änderungen lokal, kein Push oder Deployment.

## Umstellung

Statistik-Labor, ae-pandas, ae-models und project verwenden uv, Python 3.14 und jeweils eine eigene Lockdatei. Die tatsächlichen Prüfungen liefen mit Python 3.14.9. Der Kernel data-analytics ist innerhalb der jeweiligen .venv registriert.

Die Vorlagen verwenden pandas 2.3.3, NumPy 2.5.4 und scikit-learn 1.9.1. pandas bleibt in der 2er-Reihe, damit die vorhandenen Datentypaufgaben ihre bisherige Bedeutung behalten. Altair 5.5 scheiterte unter Python 3.14 beim Import; die Vorlagen verwenden deshalb das erfolgreich geprüfte Altair 6.3.0. Die Kursanleitung erklärt die Versionsprüfung und projektlokale Kernelregistrierung.

## Ausführung

| Material | Prüfung | Ergebnis |
|---|---|---|
| ae-pandas | Alle 6 Notebooks vollständig mit temporären Lösungen und sämtlichen Originalassertions | Bestanden |
| ae-models | Alle 5 Notebooks vollständig mit temporären Lösungen und enthaltenen Prüfzellen | Bestanden |
| project | Alle 4 unveränderten Notebookgerüste validiert und im Projektkernel ausgeführt | Bestanden; keine ausgefüllte Projektanalyse geprüft |
| Statistik-Labor | EDA 29, Inferenz 18, Modelle 14 Codezellen vollständig in temporären Kopien ausgeführt | Alle 61 Codezellen bestanden |
| Projektumgebung | Separates temporäres Notebook: Paketimports, Excel-Rundlauf, Regression/RMSE, Altair-Spezifikation und Matplotlib-Datei | Bestanden |

Automatischer Vergleich der 15 Vorlagennotebooks mit dem Stand vor der Umstellung: alle Zellinhalte, Aufgaben und Prüfzellen unverändert. Keine gespeicherten Ausgaben oder Ausführungszähler. Nur Metadaten und Einrichtung sind geändert. Lösungsharness und ausgeführte temporäre Kopien liegen außerhalb der Template-Repositories und sind nicht Bestandteil des Downloads. Die ausgearbeiteten Labor-Notebooks behalten ihren vorhandenen Code und ihre vorhandenen Ausgaben.

## Download

Die 33 bisherigen ZIP-Dateien wurden vor dem Packen gegen die ursprüngliche Laborquelle verglichen. Das neue Archiv enthält diese 33 Dateien aktualisiert sowie .python-version. Alle 34 Einträge stimmen bytegenau mit der Laborquelle überein. Keine .venv, Caches, temporären Lösungen oder Moderationsskripte enthalten.

Die ZIP wurde frisch entpackt und mit uv sync --locked synchronisiert. Python-Version und Imports wurden geprüft. Der Quarto-Kursbuild ist erfolgreich; der gerenderte Download ist bytegleich mit dem geprüften Archiv. Die Einrichtungsseite wurde im Browser geprüft.

## Grenzen

Ausgeführt auf macOS. Windows-Anleitungen wurden nicht auf Windows praktisch ausgeführt. Eine ursprüngliche externe CSV-Quelle im Pandas-Notebook war beim Test erreichbar; ihre zukünftige Verfügbarkeit bleibt extern. Diagramm-Code wurde ausgeführt, aber nicht jede interaktive Diagrammfunktion manuell bedient.

Detailprotokolle liegen in den drei Template-Repositories jeweils unter docs/pruefung-python314.md. Das interne Moderationsskript wurde synchronisiert und bleibt außerhalb der Downloads.
