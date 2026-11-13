# Folien- und Videovorlage: Sonnendach-Potenzial Winterthur

## Vor dem Export ausfüllen

- **Gruppe:** [Gruppennummer]
- **Studierende:** [Vor- und Nachname aller Gruppenmitglieder]
- **Aktueller API-Abruf:** [Datum aus dem Notebook]
- **Video-Dateiname:** `video_recording_group_[NN].mp4`
- **Material-ZIP:** `materials_group_[NN].zip`
- **PDF-Dateiname:** `presentation_group_[NN].pdf`

Die Zahlen und Screenshots nach dem letzten vollständigen Notebook-Lauf
aktualisieren. Die Folien als PDF exportieren. Keine festen Kennzahlen aus
älteren API-Läufen ungeprüft übernehmen.

## Empfohlene Folienstruktur

| Folie | Inhalt | Beleg / Visual |
|---|---|---|
| 1. Titel | Projekttitel, Namen, Gruppe und Datum | Titelbild oder Kartenausschnitt |
| 2. Einführung | Hintergrund, Problem, Ziel und Forschungsfrage | Forschungsfrage gross hervorheben |
| 3. Material und Daten | BFE-Solarkarte, geo.admin.ch-API, Gebiet und Zielvariable | API-Layer und BBOX aus dem Notebook |
| 4. Methoden | Abruf, Bereinigung, neue Variablen, SQLite/PostgreSQL und SQL | kurzer Codeausschnitt oder Datenfluss |
| 5. EDA und Raum | Verteilungen, Eignungsklassen und räumliche Muster | eine zentrale Grafik und ein Kartenausschnitt |
| 6. Statistik | Spearman-rho, p-Wert und Interpretation | aktuelles Notebook-Ergebnis |
| 7. Modelle | Lineare Regression und Random Forest, gruppierter Split | Ergebnis-Tabelle mit R², RMSE, MAE und Baseline |
| 8. Diskussion und Fazit | Antwort auf Forschungsfrage, Grenzen und nächste Schritte | Kernaussage statt Code |
| 9. Bewertungsnachweise (Appendix) | Screenshots und Codebelege für die bewerteten Kriterien | Evidenzliste unten |

Die Forschungsfrage bezieht sich auf BFE-Potenzialschätzungen. Nicht behaupten,
dass das Modell reale Stromproduktion oder Kausalität nachweist. Beim
PostgreSQL-Zusatzpunkt einen Screenshot der tatsächlich verwendeten
PostgreSQL-Verbindung und SQL-Abfrage zeigen; ein SQLite-Lauf allein belegt
diesen Zusatzpunkt nicht.

## Video-Zeitplan

Gesamtdauer: **5 Minuten × Anzahl Gruppenmitglieder**. Abschnitte proportional
skalieren und sinnvoll auf alle Vortragenden verteilen:

1. Forschungsfrage und Motivation — 15 %
2. Datenquelle und Aufbereitung — 20 %
3. EDA und geografische Darstellung — 20 %
4. Statistik und Modellierung — 25 %
5. Resultate, Interpretation und Grenzen — 20 %

Frei sprechen, gut lesbare Folien nutzen und Code nur zeigen, wenn er eine
Methode oder ein Resultat verständlicher macht. Nicht durch Notebook-Zellen
scrollen. Die HTML-Karte und höchstens zwei ausgewählte Diagramme eignen sich
für eine kurze Live-Demo.

## Appendix: Nachweise für die Bewertung

Die Lehrperson bewertet die tatsächliche Arbeit, nicht nur diese Liste. Für
jeden Nachweis einen Screenshot mit sichtbarem Titel oder Notebook-Abschnitt
einfügen; Zugangsdaten und personenbezogene Daten ausblenden.

| Kriterium | Geeigneter Screenshot / Codeausschnitt |
|---|---|
| Data Analysis | Forschungsfrage und quantitative Ergebnisübersicht |
| Web-API | API-URL, Layer, paginierter Abruf und Anzahl abgerufener Datensätze |
| Datenaufbereitung | Sentinel-/Duplikatfilter und erzeugte Winkelmerkmale |
| Datenbank und SQL | Python-SQL-Abfrage plus Datenbankausgabe; für Zusatzpunkt PostgreSQL-Verbindung |
| Nicht-grafische EDA | `describe()`, fehlende Werte und Klassen-Tabelle |
| Grafische EDA | Verteilungen, Klassenvergleich und Korrelations-Heatmap |
| Geografische Daten | Folium-Karte mit Dachgeometrien und Legende |
| Statistischer Test | Spearman-rho und p-Wert samt Interpretation |
| Modellierung | Merkmalsdefinition und gebäudeweiser Train/Test-Split |
| Modellevaluation | Vergleichstabelle für beide Modelle und Median-Baseline mit R², RMSE, MAE |
| Ergebnisinterpretation | dynamische Schlussfolgerung plus Grenzen / keine Kausalitätsbehauptung |
| Kreativität | Quizseite, beantwortete Quizfrage und automatische Auswertung |
| Präsentation | PDF-Folien und Videodatei in der vorgesehenen Dauer |

## Moodle-Checkliste

- [ ] Video als MP4, Dateiname mit Gruppennummer, Dauer `Gruppengröße × 5 Minuten`
- [ ] ZIP mit Notebook, Skript, Roh-/Analysedaten, Datenbank und nötigen Ressourcen
- [ ] Präsentation als PDF mit Titel/Namen, Einführung, Materialien/Methoden,
      Resultaten/Diskussion, Schlussfolgerungen und Bewertungs-Appendix
- [ ] Persönliche Abgabe durch jedes Gruppenmitglied wie vorgegeben
