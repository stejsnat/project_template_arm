# %% [markdown]
# # Test-Abruf Sonnendach-Daten (BFE) für ein Gebiet in Winterthur
#
# Ziel: herausfinden, welche Felder die geo.admin-API pro Dachfläche liefert,
# wie viele Dachflächen und Gebäude es in einem kleinen Gebiet gibt,
# und ob die seitenweise Abfrage (max. 200 pro Abfrage) funktioniert.
#
# In VS Code kann diese Datei Zelle für Zelle ausgeführt werden ("Run Cell"
# über jeder # %% -Zeile) oder in ein Notebook kopiert werden.

# %%
import requests
import pandas as pd

URL = "https://api3.geo.admin.ch/rest/services/ech/MapServer/identify"
LAYER = "ch.bfe.solarenergie-eignung-daecher"
PAGE_SIZE = 200
MAX_OFFSET = 20_000
TIMEOUT_SECONDS = 60

# Testgebiet: ca. 500 m x 500 m um die Winterthurer Altstadt,
# Koordinaten im Schweizer System LV95 (EPSG:2056): xmin, ymin, xmax, ymax
BBOX = (2696600, 1261600, 2697100, 1262100)

session = requests.Session()

# %%
def abfrage(bbox, offset=0, limit=PAGE_SIZE):
    """Eine Seite Dachflächen für ein Rechteck abfragen."""
    if not 1 <= limit <= PAGE_SIZE:
        raise ValueError(f"limit muss zwischen 1 und {PAGE_SIZE} liegen.")

    params = {
        "geometry": ",".join(str(value) for value in bbox),
        "geometryType": "esriGeometryEnvelope",
        "layers": f"all:{LAYER}",
        "tolerance": 0,
        "sr": 2056,
        "returnGeometry": "false",
        "limit": limit,
        "offset": offset,
    }
    response = session.get(URL, params=params, timeout=TIMEOUT_SECONDS)
    response.raise_for_status()
    payload = response.json()
    results = payload.get("results") if isinstance(payload, dict) else None
    if not isinstance(results, list):
        raise ValueError("Die API-Antwort enthält keine gültige 'results'-Liste.")
    return results


# Erste Seite holen und anschauen
erste_seite = abfrage(BBOX)
print("Anzahl Dachflächen auf Seite 1:", len(erste_seite))
print(
    "Schlüssel eines Resultats:",
    list(erste_seite[0].keys()) if erste_seite else "keine Resultate",
)

# %%
# Welche Attribute gibt es pro Dachfläche? (die eigentliche Frage des Test-Abrufs)
if erste_seite:
    for key, value in erste_seite[0].get("attributes", {}).items():
        print(f"{key:25} {value}")

# %%
# Alle Seiten holen. Die bereits geladene erste Seite wird wiederverwendet.
alle = []
gesehen = set()
offset = 0

while offset < MAX_OFFSET:
    limit = min(PAGE_SIZE, MAX_OFFSET - offset)
    seite = erste_seite if offset == 0 else abfrage(BBOX, offset=offset, limit=limit)
    if not seite:
        break

    neue = []
    for result in seite:
        feature_id = result.get("featureId")
        if feature_id is None or feature_id not in gesehen:
            neue.append(result)
            if feature_id is not None:
                gesehen.add(feature_id)

    if not neue:
        break

    alle.extend(neue)
    print(f"offset {offset}: {len(neue)} neue Dachflächen, total {len(alle)}")

    if len(seite) < limit:
        break
    offset += limit
else:
    print(f"Sicherheits-Stopp bei offset {MAX_OFFSET}.")

df_roofs = pd.DataFrame([result.get("attributes", {}) for result in alle])
df_roofs["featureId"] = [result.get("featureId") for result in alle]
print("Dachflächen total:", len(df_roofs))
print("Spalten:", list(df_roofs.columns))

# %%
# Wie viele Gebäude sind das? Dafür braucht es eine Gebäude-ID
# (z. B. building_id oder gwr_egid).
id_spalten = [
    column
    for column in df_roofs.columns
    if "egid" in column.lower() or "building" in column.lower()
]
print("Mögliche Gebäude-ID-Spalten:", id_spalten)
for column in id_spalten:
    print(
        f"{column}: {df_roofs[column].nunique()} verschiedene Werte, "
        f"{df_roofs[column].isna().sum()} fehlend"
    )

# %%
# Fehlende Werte und Datentypen auf einen Blick
print(df_roofs.isna().sum())
df_roofs.head()

# %%
# Speichern für die weitere Arbeit
output_path = "solar_test_winterthur_altstadt.csv"
df_roofs.to_csv(output_path, index=False)
print(f"Gespeichert: {output_path}")
