# Sonnendach-Potenzial Winterthur

## Projektfrage

Wie hängen Dachfläche, Ausrichtung und Neigung mit dem vom BFE geschätzten
jährlichen Solarstromertrag zusammen, und wie gut lässt sich dieser Wert für
bisher ungesehene Gebäude vorhersagen?

Das Untersuchungsgebiet umfasst rund 500 x 500 m in der Winterthurer Altstadt.
Die Zielvariable `stromertrag` ist ein Potenzialwert aus der BFE-Solarkarte,
keine Messung tatsächlich produzierten Stroms.

## Ausführen

1. Im Repository-Root die Abhängigkeiten installieren: `pip install -r requirements.txt`.
2. `sonnendach_projekt.ipynb` öffnen und alle Zellen der Reihe nach ausführen.
3. Die geo.admin.ch-API muss erreichbar sein. Das Notebook lädt die Daten und
   Geometrien live neu; bei API-Änderungen können Anzahl oder Ergebnisse
   abweichen.

Alternativ lässt sich `python Project/sonnendach_projekt.py` aus dem
Repository-Root ausführen. Für Diagramme und interaktive Karten empfiehlt sich
das Notebook.

## Im Notebook enthalten

- Web-API-Abfrage mit Seitenabruf, BBOX in LV95 und API-Fehlerprüfung
- Bereinigung ungültiger Sentinel-IDs und Duplikate sowie Winkel- und
  Log-Merkmale
- Explorative Kennzahlen, Verteilungen, Klassenvergleiche und Korrelationen
- SQLite-Speicherung der bereinigten Daten und SQL-Abfrage aus Python
- Interaktive Karte mit nach WGS84 transformierten Dachgeometrien
- Spearman-Korrelation inklusive p-Wert
- Multiple lineare Regression und Random-Forest-Regression; gebäudeweiser
  Train/Test-Split und Auswertung mit R², RMSE und MAE
- Dynamische Interpretation und Grenzen der Ergebnisse

Das Notebook schließt `gstrahlung`, Eignungsklasse und Ertragsteilsummen als
Modellmerkmale aus, weil sie dem Zielwert zu nahe oder aus ihm abgeleitet sind.
Es entfernt keine gültigen Ausreißer ohne fachliche Begründung.

## Erzeugte Dateien

Nach dem Ausführen liegen in diesem Ordner:

- `solar_test_winterthur_altstadt_raw.csv` – API-Rohdaten einschließlich Geometrie
- `solar_test_winterthur_altstadt_clean.csv` – bereinigte Analysedaten
- `sonnendach_winterthur.sqlite` – SQLite-Tabelle `roof_analysis`
- `sonnendach_winterthur_karte.html` – interaktive Karte

## Bezug zur Bewertung

| Kriterium | Umsetzung |
|---|---|
| Data Analysis / quantitative Methoden | EDA, statistischer Test, Regression |
| Web Scraping / Web API | geo.admin.ch REST API |
| Datenbereinigung und neue Variablen | IDs, fehlende Modellwerte, Winkel- und Log-Merkmale |
| Datenbank und SQL in Python | SQLite |
| Nicht-grafische und grafische EDA | Kennzahlen, Tabellen, Verteilungen, Heatmap |
| Regressionsmodell und Evaluation | Lineare Regression und Random Forest; R², RMSE, MAE |
| Interpretation | automatisch ausgegebene Einordnung der Modellmetriken und Grenzen |
| Geografische Daten | LV95-Dachgeometrien, WGS84-Folium-Karte |
| Statistischer Zusatztest | Spearman-Korrelation mit p-Wert |
| Mehrere Prognosemodelle | zwei Modelle plus Median-Baseline |

SQLite erfüllt die Mindestanforderung, aber nicht den Zusatzpunkt für
MySQL/PostgreSQL. Moodle-Upload und Videoaufnahme müssen von der Gruppe selbst
vorgenommen werden; das Notebook enthält dafür eine Abgabe- und
Präsentationscheckliste.

## Abgabe

Vor der Moodle-Abgabe das Notebook von oben nach unten ausführen und mit den
Outputs speichern. Notebook, Roh- und bereinigte CSV, SQLite-Datei sowie
optional die HTML-Karte hochladen. Vor der Präsentation die Kennzahlen aus dem
neuesten API-Lauf übernehmen und die Aufnahme auf `Gruppengröße x 5 Minuten`
auslegen. Eine ausformulierte Struktur ist in [praesentation.md](./praesentation.md)
enthalten.

## Datenquelle

geo.admin.ch REST API, MapServer-Layer
`ch.bfe.solarenergie-eignung-daecher`; API-URL und BBOX sind im Notebook
dokumentiert. Der Abrufzeitpunkt wird bei jeder Ausführung ausgegeben.
