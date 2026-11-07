# Leitfaden für die Video-Präsentation

## Dauer und Aufbau

Die geforderte Gesamtdauer beträgt **5 Minuten x Anzahl der Gruppenmitglieder**.
Die Abschnitte können entsprechend der Gruppengröße verlängert oder auf mehrere
Sprecherinnen und Sprecher verteilt werden. Proportionen beziehen sich auf die
Gesamtdauer:

1. **Fragestellung und Motivation (15%)** – Winterthurer Altstadt, Forschungsfrage
   und Unterschied zwischen BFE-Potenzial und tatsächlich erzeugtem Strom.
2. **Datenquelle und Aufbereitung (20%)** – geo.admin.ch-API, LV95-BBOX,
   Seitenabfragen, ungültiger Sentinel, fehlende Werte und erzeugte Merkmale.
3. **EDA und Geografie (20%)** – Verteilung der Dachflächen und Erträge,
   Gebäudecluster, Eignungsklassen und interaktive Karte.
4. **Statistik und Modellierung (25%)** – Spearman-rho mit p-Wert,
   gebäudeweiser Train/Test-Split und Begründung für den Ausschluss
   zielnaher Variablen.
5. **Resultate, Interpretation und Grenzen (20%)** – Kennzahlen beider Modelle,
   Vergleich mit der Baseline, Bedeutung für ungesehene Gebäude und
   Einschränkungen der Analyse.

## Aktueller Lauf als Ausgangspunkt

Die folgenden Ergebnisse stammen aus dem API-Lauf vom 7. November 2026 und
müssen nach einer erneuten Notebook-Ausführung aktualisiert werden:

- 1'313 API-Ergebnisse einschließlich einer ungültigen Sentinel-Zeile;
  1'312 analysierte Dachflächen und 308 Gebäude.
- Spearman-rho zwischen Dachfläche und BFE-Ertrag: 0.966, p < 0.001.
  Das ist ein starker monotoner Zusammenhang, aber kein Kausalitätsnachweis.
- Gebäude-holdout-Test: 1'030 Dachflächen / 246 Gebäude im Training,
  282 Dachflächen / 62 Gebäude im Test, keine Gebäudeüberschneidung.
- Random Forest: R² = 0.970, RMSE = 5'024.5 kWh/Jahr,
  MAE = 2'090.1 kWh/Jahr.
- Multiple lineare Regression: R² = 0.952, RMSE = 6'366.9 kWh/Jahr,
  MAE = 2'601.9 kWh/Jahr.
- Median-Baseline: R² = -0.046, RMSE = 29'826.6 kWh/Jahr.

R² beschreibt erklärte Varianz, RMSE bestraft große Fehler stärker und MAE
entspricht dem durchschnittlichen absoluten Fehler. Die Werte beziehen sich
auf BFE-Potenzialschätzungen im Testgebiet, nicht auf Messdaten realer Anlagen.

## Präsentationshinweise

- Frei sprechen und wenige, gut lesbare Folien statt Notebook-Code zeigen.
- Eine Karte und höchstens zwei zentrale Diagramme auswählen.
- Ein Gruppenmitglied erklärt Daten und EDA, ein weiteres Modell und
  Interpretation; bei größeren Gruppen Abschnitte sinnvoll aufteilen.
- Aussagen wie „Das Modell prognostiziert die reale Stromproduktion“ vermeiden.
- Die aktuelle API-Version, Abrufdatum, Kennzahlen und Einheiten vor der
  Aufnahme aus dem Notebook kontrollieren.

Dieses Dokument ist ein Ablaufvorschlag, keine Videoaufnahme. Die Gruppe muss
die Aufnahme selbst erstellen und in Moodle hochladen.
