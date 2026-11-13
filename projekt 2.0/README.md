# Sonnendach-Potenzial Winterthur — Projekt 2.0

## Forschungsfrage

Wie hängen Dachfläche, Ausrichtung und Neigung mit dem vom BFE geschätzten
jährlichen Solarstromertrag zusammen, und wie gut lässt sich dieser Wert für
bisher ungesehene Gebäude vorhersagen?

Das Untersuchungsgebiet ist die gesamte aktuelle Gemeinde Winterthur
(rund 68 km²). `stromertrag` ist ein modellierter Potenzialwert der
Solarkarte, keine Messung tatsächlich produzierten Stroms.

## Aktueller stadtweiter Lauf

Am 13. November 2026 wurden 333 Kacheln innerhalb der aktuellen
Gemeindegrenze abgefragt. Der Abruf ergab **55’277 eindeutige Dachflächen**
und **20’831 Gebäude**. Ein Dach wird mitgezählt, wenn sein Repräsentativpunkt
innerhalb der Gemeindegrenze liegt. Die ursprüngliche Liste mit sechs
PLZ-Gebieten wäre unvollständig gewesen; deshalb wird die amtliche
Gemeindegrenze verwendet.

Der gebäudeweise Testsplit enthielt 11’055 Dächer aus 4’167 bisher ungesehenen
Gebäuden. Ergebnisse auf diesem Lauf:

| Modell | R² | RMSE (kWh/Jahr) | MAE (kWh/Jahr) |
|---|---:|---:|---:|
| Random Forest | 0.992 | 2’886.7 | 988.6 |
| Multiple lineare Regression | 0.821 | 13’857.4 | 2’282.3 |
| Median-Baseline | -0.049 | 33’556.6 | 12’021.6 |

Die Spearman-Korrelation zwischen Dachfläche und BFE-Ertrag beträgt 0.977
(p < 0.001). Diese Werte beschreiben BFE-Potenzialschätzungen im Testgebiet,
nicht reale Stromproduktion; bei einem erneuten API-Lauf können sie variieren.

## Schnellstart

```bash
python -m pip install -r "projekt 2.0/requirements.txt"
```

Danach `sonnendach_projekt.ipynb` öffnen und von oben nach unten ausführen. Die
geo.admin.ch-API muss erreichbar sein; Zahlen können sich bei späteren
API-/Datenversionen ändern. Die vollständige Stadtabfrage kann mehrere Minuten
dauern. Alternativ:

```bash
python "projekt 2.0/sonnendach_projekt.py"
```

Das Skript schreibt seine Ergebnisse immer in diesen Projektordner.

## PostgreSQL (Zusatzpunkt)

Standardmässig wird SQLite lokal verwendet. Für eine Demonstration mit
PostgreSQL zuerst eine Datenbank bereitstellen und `DATABASE_URL` setzen,
bevor Notebook oder Skript gestartet wird:

```bash
export DATABASE_URL="postgresql+psycopg://USER:PASSWORD@HOST:5432/DATABASE"
```

Unter PowerShell:

```powershell
$env:DATABASE_URL = "postgresql+psycopg://USER:PASSWORD@HOST:5432/DATABASE"
```

Die Zugangsdaten nicht in Notebook, Git oder Abgabe-ZIP speichern. Bei
gesetztem `DATABASE_URL` werden Tabelle `roof_analysis` und die SQL-Auswertung
in PostgreSQL ausgeführt. Ohne PostgreSQL-Verbindung erfüllt der SQLite-Modus
die Mindestanforderung, aber nicht den PostgreSQL-Zusatzpunkt. SQL-Abfragen
werden in beiden Modi aus Python ausgeführt.

## Inhalt und Bewertungsevidenz

| Bewertungskriterium | Evidenz in diesem Projekt |
|---|---|
| Quantitative Datenanalyse | Kennzahlen, Verteilungen, Tests und Prognosemodelle im Notebook |
| Web-API | geo.admin.ch REST API, dokumentierter Layer und paginierter Abruf |
| Datenbereinigung | Sentinel-IDs, Duplikate, fehlende Modellwerte und neue Merkmale |
| Datenbank + SQL aus Python | SQLite lokal; PostgreSQL-Unterstützung über `DATABASE_URL` |
| Nicht-grafische und grafische EDA | Kennzahlen, Tabellen, Verteilungen, Klassenvergleiche, Heatmap |
| Regression und Modellevaluation | Lineare Regression + Random Forest; R², RMSE, MAE und Baseline |
| Interpretation | dynamische Ergebnisinterpretation und dokumentierte Einschränkungen |
| Geografische Daten | LV95-Geometrien, nach WGS84 transformierte interaktive Karte |
| Statistischer Zusatztest | Spearman-Rangkorrelation inklusive p-Wert |
| Kreativität | interaktives Offline-Quiz für die Lehrperson (`quiz_dozent.html`) |
| Mehrere Modelle | zwei Regressionsmodelle, verglichen mit Median-Baseline |

Die Modellmerkmale sind Fläche, Neigung und zirkuläre Kodierung der
Ausrichtung. Zielnahe Ertragskomponenten, Einstrahlung und Eignungsklasse
werden ausgeschlossen, um Datenleckage zu vermeiden. Der Testsplit erfolgt
gebäudeweise.

## Dateien

- `sonnendach_projekt.ipynb` — Analyse, Visualisierungen und Modellierung
- `sonnendach_projekt.py` — ausführbare Skriptfassung
- `quiz_dozent.html` — interaktives Quiz mit Auswertung und Erklärungen
- `praesentation.md` — Folienstruktur, Videoplan und Bewertungsnachweise
- `solar_winterthur_stadt_raw.csv` — Rohdaten für die ganze Gemeinde
- `solar_winterthur_stadt_clean.csv` — bereinigte Analysedaten
- `sonnendach_winterthur.sqlite` — reproduzierbare lokale Datenbank
- `sonnendach_winterthur_karte.html` — interaktive Karte

## Präsentation und Moodle

Die Folienstruktur und das Beleg-Appendix stehen in
[praesentation.md](./praesentation.md). Gruppennamen, aktuelle Kennzahlen und
Gruppennummer vor dem Export ergänzen. Die Gruppe muss die Folien als PDF
exportieren, ein Video mit `5 Minuten × Anzahl Gruppenmitglieder` aufnehmen
und beide Dateien zusammen mit den Projektmaterialien selbst auf Moodle
hochladen; persönliche Moodle-Anmeldung/Upload kann dieses Projekt nicht
automatisieren.

Vor der Abgabe das Notebook vollständig ausführen und mit den frischen Outputs
speichern. Keine Datenbankpasswörter oder sonstigen Zugangsdaten mit abgeben.

## Quelle

geo.admin.ch REST API, MapServer-Layer
`ch.bfe.solarenergie-eignung-daecher`; die aktuelle Gemeindegrenze wird aus
`ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill` geladen und in
500-m-Kacheln abgefragt. Das Abrufdatum wird bei jeder Ausführung ausgegeben.
